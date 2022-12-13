import json
import boto3

def lambda_handler(event, context):
    
    #connect to dynamodb resource
    
    client = boto3.resource('dynamodb')
    
    #create a dynamodb client to visitor_count table
    table = client.Table('visitor_count')
    
    #increment visitorcount
    
    response = table.update_item(
        Key={
            'path': 'index.html'},
            
        AttributeUpdates={
            'visitor_count':{
                'Value': 1,
                'Action': 'ADD'
            }
        }
    )
    
    #get visitor_count

    response = table.get_item(
        Key={
            'path': 'index.html'}
    
    )
    visitor_count = (response['Item']['visitor_count'])

    
    


    # TODO implement
    return {
        'statusCode': 200,
        'headers':{
            'Access-Control-Allow-Origin': '*'
        },
        'body': visitor_count
    }
