import boto3
import time
import json

# Create SQS client
session = boto3.session.Session(region_name='us-east-1', profile_name='fm')
sqs = session.client('sqs')

queue_url = 'https://sqs.us-east-1.amazonaws.com/XXXXXXXXXXXX/the-cloud'

while True:
    # Receive message from SQS queue
    response = sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=10,
        WaitTimeSeconds=10
    )

    if 'Messages' in response:
        message = response['Messages'][0]
        receipt_handle = message['ReceiptHandle']

        # Delete received message from queue
        sqs.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=receipt_handle
        )

        print(json.loads(message['Body']))
    else:
        print('Queue is empty')
