import boto3

dynamodb = boto3.resource('dynamodb')
table    = dynamodb.Table('demo_test')

def get_persons():
    response = table.scan()
    return response['Items']

def lambda_handler(event, context):
    return get_persons() 
