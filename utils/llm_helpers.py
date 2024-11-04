import subprocess
import boto3

def generate_and_execute_aws_query(query):
    # Novo prompt com região
    prompt = f"Write only the Python code using boto3, without wrinting python to the begining to answer the following AWS query, without any explanation or comments, I will not fill any code manually, you must generate everything needed to execute the asked code: '{query}'"

    result = subprocess.run(
        ["ollama", "run", "llama3.2", prompt],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        return f"Error generating code: {result.stderr.strip()}"

    code = result.stdout.strip()
    return code
    # try:
    #     # Execução do código gerado
    #     exec_locals = {}
    #     exec(code, {"boto3": boto3}, exec_locals)
    #     result = exec_locals.get("result", "No result returned from the generated code.")
    #     return result
    # except Exception as e:
    #     return f"Execution error: {str(e)}"
