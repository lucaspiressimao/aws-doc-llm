
# aws_config.py - Gerencia as configurações das contas AWS

import boto3

def get_aws_session(profile_name=None, region_name="us-east-1"):
    if profile_name:
        session = boto3.Session(profile_name=profile_name, region_name=region_name)
    else:
        session = boto3.Session(region_name=region_name)
    return session
