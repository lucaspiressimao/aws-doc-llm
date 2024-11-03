
# query_handler.py - Lida com consultas e integra AWS e LLM

from utils.aws_helpers import get_ec2_instances  # Exemplo de função
from utils.llm_helpers import generate_documentation

def handle_query(account, region, query):
    # Exemplo: Obter instâncias EC2 e documentar
    ec2_data = get_ec2_instances(account, region)
    documentation = generate_documentation(query, ec2_data)
    return documentation
