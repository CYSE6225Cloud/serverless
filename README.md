# serverless

To create lambda function and other dependencies. Please execute below code

create stack for Assignment 8-
aws cloudformation create-stack  \
 --stack-name myteststack2  --template-body file://csye6225-infra.yml \
 --parameters ParameterKey=VpcCIDR,ParameterValue="10.0.0.0/16" ParameterKey=PublicSubnet1CIDR,ParameterValue="10.0.3.0/24" ParameterKey=PublicSubnet2CIDR,ParameterValue="10.0.4.0/24" ParameterKey=PublicSubnet3CIDR,ParameterValue="10.0.5.0/24" ParameterKey=PrivateSubnet1CIDR,ParameterValue="10.0.6.0/24" ParameterKey=PrivateSubnet2CIDR,ParameterValue="10.0.7.0/24" ParameterKey=PrivateSubnet3CIDR,ParameterValue="10.0.8.0/24" ParameterKey=AMIID,ParameterValue="ami-00baf275c49e0d94e" ParameterKey=MyKeyPair,ParameterValue="CSYE6225" --profile demo1 --region us-east-1 --capabilities CAPABILITY_NAMED_IAM

