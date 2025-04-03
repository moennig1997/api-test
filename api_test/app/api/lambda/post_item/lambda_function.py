import boto3
import json

dynamodb = boto3.resource('dynamodb')
table    = dynamodb.Table('demo_test')

def put_person(id,name):
    item = {
      "test_id": id,
      "name": name,
    }
    table.put_item(Item=item)

    return 0

def lambda_handler(event, context):
    id =  event['pathParameters']['test_id']
    name = json.loads(event.get('body', '{}')).get('name')
    put_person(id,name)
    dict = {"test_id": id, "name": name}
    return {
        'statusCode': 200,
        'body': json.dumps(dict)
    }
    
