# AWS CLI config

`aws configure --profile <profile_name>`

eg: `aws configure --profile farooq.tfora`

sample region: ap-south-1

## Obtain the Access Key ID and Secret Access Key for your AWS account

To obtain the Access Key ID and Secret Access Key for your AWS account, you can follow these steps:

1. Sign in to the AWS Management Console using your AWS account credentials.
2. Open the IAM (Identity and Access Management) service.
3. In the IAM dashboard, click on "Users" in the left navigation pane.
4. Select the IAM user for which you want to generate the Access Key ID and Secret Access Key.
5. Click on the "Security credentials" tab for the selected IAM user.
6. Scroll down to the "Access keys" section and click on the "Create access key" button.
7. A dialog box will appear displaying the Access Key ID and Secret Access Key. It is important to note that the Secret Access Key is only displayed once. Make sure to copy and securely store the Secret Access Key in a safe place. If you lose it, you will need to generate a new Access Key pair.
8. Click on the "Download .csv file" button to download a CSV file containing the Access Key ID and Secret Access Key. This file can be useful for keeping a backup or sharing the credentials with other users, but be cautious about storing it securely.

## Batch write items to DynamoDB

`aws dynamodb batch-write-item --request-items file://<file_name>.json --profile <profile_name>`

eg: `aws dynamodb batch-write-item --request-items file://output.json --profile farooq.tfora`
