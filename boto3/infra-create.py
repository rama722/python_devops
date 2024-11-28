import boto3 
# botocore - exceptions(msg, *args, **kwargs)

client = boto3.client('s3')

response = client.create_bucket(
    Bucket = "smartsclar-hr2024"
)
response = client.get_bucket_acl(
    Bucket = "smartsclar-hr2024"
)

print(response)