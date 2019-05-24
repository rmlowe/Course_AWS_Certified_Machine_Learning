import requests
import boto3
import uuid
import time
import random
import json

client = boto3.client('kinesis', region_name='us-east-1')
partition_key = str(uuid.uuid4())

while True:
        r = requests.get('https://randomuser.me/api/?exc=login')
        data = json.dumps(r.json())
        client.put_record(
                StreamName='streaming-data-collection-lab',
                Data=data,
                PartitionKey=partition_key)
        time.sleep(random.uniform(0, 1))
