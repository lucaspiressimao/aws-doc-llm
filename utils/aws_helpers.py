
# aws_helpers.py - Funções auxiliares para conexão e obtenção de dados AWS

import boto3

def get_ec2_instances(profile_name, region_name):
    session = boto3.Session(profile_name=profile_name, region_name=region_name)
    ec2 = session.client("ec2")
    instances = ec2.describe_instances()
    return instances  # Devolve os dados brutos das instâncias
