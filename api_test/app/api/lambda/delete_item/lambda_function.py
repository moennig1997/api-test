import boto3
import json

dynamodb = boto3.resource('dynamodb')
table    = dynamodb.Table('demo_test')

def del_person(id):
    table.delete_item(Key ={'test_id':id})
    return 0

def get_person(id):
    response = table.get_item(
            Key={
                 'test_id': id
            }
        )
    return response['Item']


def get_all_persons():
    response = table.scan()
    return response['Items']


def lambda_handler(event, context):
    id =  event['pathParameters']['test_id']
    item = get_person(id)
    del_person(id)
    return {
        'statusCode': 200,
        'body': json.dumps(item)
    }

 
    
