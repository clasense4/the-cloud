import json
import uuid
import time
from random import randint
from faker import Faker
fake = Faker()
from consumer import consume

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

for i in range(0,5):
    record = {
        'metadata_id': str(get_md5_id()),
        'name': fake.name(),
        'address': fake.address()
    }
    print(record)

    consume.delay(record)
