import boto3
import json
import uuid
import time
from random import randint
from faker import Faker
fake = Faker()

# Create SQS client
session = boto3.session.Session(region_name='us-east-1', profile_name='fm')
sqs = session.client('sqs')

queue_url = 'https://sqs.us-east-1.amazonaws.com/XXXXXXXXXXXX/the-cloud'

def random_string(length):
    chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz';
    chars_len = len(chars)
    rand_str = ''

    for i in range(0, length):
        rand_str = rand_str + chars[randint(0, length-1)]

    return rand_str

def millis():
    return int(round(time.time() * 1000))

def get_md5_id():
    id = uuid.uuid3(uuid.NAMESPACE_OID, random_string(10) + str(millis()) )
    return id

for i in range(0,10):
    record = {
        'metadata_id': str(get_md5_id()),
        'name': fake.name(),
        'address': fake.address()
    }
    print(record)

    # Send message to SQS queue
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps(record)
    )
