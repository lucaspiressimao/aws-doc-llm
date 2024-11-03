# Makefile

# Variáveis de ambiente
VENV_DIR = venv
PYTHON = $(VENV_DIR)/bin/python
PIP = $(VENV_DIR)/bin/pip
OLLAMA_PORT = 11434
FLASK_PORT = 8888

# Checagem do Ollama e seu modelo
OLLAMA_MODEL = $(shell ollama list | grep 'llama3.2' || echo "not_installed")

# Define os comandos para configurar o ambiente
setup: check_ollama_model clean virtualenv requirements

# Verifica se o modelo Ollama llama3.2 está instalado
check_ollama_model:
	@if [ "$(OLLAMA_MODEL)" = "not_installed" ]; then \
		echo "Modelo Ollama 'llama3.2' não está instalado. Por favor, instale-o usando 'ollama pull llama3.2'."; \
		exit 1; \
	else \
		echo "Modelo Ollama 'llama3.2' encontrado."; \
	fi

# Cria o ambiente virtual
virtualenv:
	@echo "Criando o ambiente virtual em $(VENV_DIR)..."
	python3 -m venv $(VENV_DIR)

# Instala as dependências do projeto
requirements:
	@echo "Instalando as dependências..."
	$(PIP) install -r requirements.txt

# Inicia a aplicação localmente e o Ollama em modo run
run:
	@echo "Verificando se as portas já estão em uso..."
	@if lsof -i :$(OLLAMA_PORT) >/dev/null; then \
		echo "Porta $(OLLAMA_PORT) já está em uso para Ollama. Parando o processo."; \
		make stop_ollama; \
	fi
	@if lsof -i :$(FLASK_PORT) >/dev/null; then \
		echo "Porta $(FLASK_PORT) já está em uso para Flask. Parando o processo."; \
		make stop_flask; \
	fi
	@echo "Iniciando o Ollama e a aplicação Flask..."
	# Executa o Ollama em modo background
	nohup ollama serve & echo $$! > ollama.pid
	# Executa o Flask na porta especificada diretamente
	FLASK_APP=app.py FLASK_RUN_PORT=$(FLASK_PORT) $(PYTHON) -m flask run --port=$(FLASK_PORT) & echo $$! > flask.pid
	@echo "Aplicação e Ollama estão em execução."

# Para o Ollama e a aplicação Flask
stop: stop_ollama stop_flask

stop_ollama:
	@if [ -f ollama.pid ]; then \
		kill -9 $$(cat ollama.pid) && rm ollama.pid; \
		echo "Ollama parado."; \
	else \
		echo "Ollama não está em execução."; \
	fi

stop_flask:
	@if [ -f flask.pid ]; then \
		kill -9 $$(cat flask.pid) && rm flask.pid; \
		echo "Aplicação Flask parada."; \
	else \
		echo "Aplicação Flask não está em execução."; \
	fi

# Limpa o ambiente virtual
clean:
	@echo "Limpando o ambiente..."
	rm -rf $(VENV_DIR) flask.pid ollama.pid
