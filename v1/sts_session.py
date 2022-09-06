import boto3, logging, os

def sts_session(accountid):

    role_list = ["","",""]
    
    for role in role_list:

        role_arn = "arn:aws:iam::"+accountid+":role/"+role

        try:
            sts_client = boto3.client('sts')
            sts_session = sts_client.assume_role(RoleArn=role_arn, RoleSessionName='aws_cli_'+accountid)
            KEY_ID = sts_session['Credentials']['AccessKeyId']
            ACCESS_KEY = sts_session['Credentials']['SecretAccessKey']
            TOKEN = sts_session['Credentials']['SessionToken']
            os.system('aws configure set aws_access_key_id '+KEY_ID+' | aws configure set aws_secret_access_key '+ACCESS_KEY+' | aws configure set aws_session_token '+TOKEN)
            logging.info(f'Credenciais temporárias recebidas para {accountid} com a role {role}')
            return KEY_ID, ACCESS_KEY, TOKEN

        except Exception as e:
            logging.info(f'Erro ao acessar {accountid} com a role {role}')
            pass