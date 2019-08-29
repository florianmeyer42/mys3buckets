#!/usr/bin/python
import boto3
from boto3 import client

conn = client('s3')  # again assumes boto.cfg setup, assume AWS S3
for key in conn.list_objects(Bucket='bucket_name')['Contents']:
    print(key['Key'])
