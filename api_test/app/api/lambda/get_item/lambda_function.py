import boto3
import json

dynamodb = boto3.resource('dynamodb')
table    = dynamodb.Table('demo_test')

def get_person(id):
    response = table.get_item(
            Key={
                 'test_id': id
            }
        )
    return response['Item']

def lambda_handler(event, context):
    print(event)
    body =  get_person(event['pathParameters']['test_id'])
    print(body)
    return {
        'statusCode': 200,
        'body': json.dumps(body)
    }

    def fibonacci(n):
        if n <= 0:
            return "Input should be a positive integer"
        elif n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            a, b = 0, 1
            for _ in range(2, n):
                a, b = b, a + b
            return b
