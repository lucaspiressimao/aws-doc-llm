import subprocess

def generate_documentation(query, data):
    prompt = f"{query}"  # Define o prompt a ser enviado para o modelo

    try:
        # Executa o Ollama localmente e passa o prompt diretamente
        result = subprocess.run(
            ["ollama", "run", "llama3.2", prompt],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return f"Error: {result.stderr.strip()}"
    except Exception as e:
        return f"Exception occurred: {str(e)}"
