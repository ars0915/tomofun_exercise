import json
import os
import boto3

sqs = boto3.client('sqs')
QUEUE_URL = os.environ['QUEUE_URL']

def handler(event, context):
    try:
        # Parse the incoming JSON message
        body = json.loads(event['body'])
        
        # Send the message to SQS
        response = sqs.send_message(
            QueueUrl=QUEUE_URL,
            MessageBody=json.dumps(body)
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Message sent to queue', 'messageId': response['MessageId']})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }