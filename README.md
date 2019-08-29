## Project mys3buckets
### Florian Meyer 29 August 2019
playing with S3 buckets in python

# List all buckets
```
import boto3
s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
  print(bucket.name)
```
