import json
import boto3
import os

users_table = os.environ['USERS_TABLE']
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(users_table)

def getMovieInfo(event, context):
    path = event["path"]
    movie_id = path.split("/")[-1]
    response = table.get_item(
    Key={
            'pk': movie_id,
            'sk': 'info'
        }
    )
    item = response['Item']
    return {
        'statusCode': 200,
        'body': json.dumps("OK")
    }
    
def putMovieInfo(event, context):
    path = event["path"]
    movie_id = path.split("/")[-1]
    body = json.loads(event["body"])
    
    table.put_item(
      Item={
            'pk': movie_id,
            'sk': 'info',
            'title': body["title"],
            'main_actor': body["main_actor"],
            'year': body["year"]
        }
    )
    print(json.dumps({"state":"ok"}))
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
