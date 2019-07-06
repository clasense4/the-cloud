from celery import Celery
import time
import json

BROKER_URL = 'redis://localhost:6379/0'
app = Celery('tasks', broker=BROKER_URL)

@app.task
def consume(metadata):
    # Consume with command
    # celery -A consumer worker --loglevel=info
    print(metadata)
