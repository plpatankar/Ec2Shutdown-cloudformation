# Ec2Shutdown-cloudformation
This cloudformation template will create  -
- lambda fuction to shutdown all running ec2 instances except those which has tag "AutoOff:False".
- Cloudwatch event with schedule to trigger lambda fuction.
- Create required IAM roles.

## Python code Ec2Shutdown-lambda-code.py
Before executing cloudformation template, upload the python script Ec2Shutdown-lambda-code.py to S3 and specify bucket names in template -

        "Ec2Shutdown": {
            "Type": "AWS::Lambda::Function",
            "Properties": {
                "Handler": "Ec2Shutdown-lambda-code",
                "MemorySize": 128,
                "Runtime": "python2.7",
				"Role": {
                    "Fn::GetAtt": [
                        "LambdaExecutionRole",
                        "Arn"
                    ]
                },
                "Code": {
                    "S3Bucket": "ec2shutdownlambdacode",
                    "S3Key": "Ec2Shutdown-lambda-code.zip"
                },
                "Timeout": 300
            }
