import boto3
import json


idp_client = boto3.client('cognito-idp')

def lambda_handler(event, context):

    username = json.loads(event.get('body', '{}')).get('username')
    password = json.loads(event.get('body', '{}')).get('password')
    
    response = idp_client.admin_initiate_auth(
        UserPoolId = "us-east-1_eFKDdUrMd",
        ClientId = "6am1ndih6o0vdfsagrppca1p8",
        AuthFlow = "ADMIN_NO_SRP_AUTH",
        AuthParameters={
           "USERNAME": username,
           "PASSWORD": password
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }

