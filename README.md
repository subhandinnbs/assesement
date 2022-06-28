after cloning this repo, run:

## terraform init
## terraform plan
## terraform apply

This will deploy an IAM role, an IAM policy and a lambda function

It will output 3 things as well in terraform state file:
1) IAM policy's arn
2) IAM Role name
3) Lambda function name

The deployed lambda function will be able to fetch these generated outputs from an S3 bucket(need to upload statefile in S3 manually as well as set S3 bucket name in Lambda's Environment)

Lambda function will return all the outputs of terraform if no parameters are passed,

and will return specific output if passed in event object as:
{
"resources": ["output_name","...","...."]
}
