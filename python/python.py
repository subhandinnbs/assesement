import boto3
import os
import json

s3_client = boto3.client("s3")
S3_BUCKET = os.environ.get("S3_BUCKET_NAME")


def lambda_handler(event, context):
    dict = {}
    resources = event.get('resources')

    object_key = "terraform.tfstate"
    file_content = s3_client.get_object(
        Bucket=S3_BUCKET,
        Key=object_key
    )["Body"].read()
    file = json.loads(file_content)
    outputs = file['outputs']

    if resources:
        for i in outputs:
            if i in resources:
                dict.update({i: outputs[i]['value']})
    else:
        for i in outputs:
            dict.update({i: outputs[i]['value']})

    return dict
