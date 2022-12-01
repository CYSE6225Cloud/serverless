import json
import boto3
def send_email(email,token):
                # TODO implement 
                user = email
                email = [email]

                ses = boto3.client("ses")
                try:

                    response = ses.send_email(
                        Source = "Admin@demo.rishi-csye6225.me",
                        Destination={
                            'ToAddresses': email
                        },
                        Message={
                            'Subject': {
                                'Data': "verify the email"
                            },
                            'Body': {
                                'Text': {
                                    'Data': "click the link to verify \n   http://demo.rishi-csye6225.me/v1/verifyUserEmail?Email={0:}&Token={1:}".format(user,token)
                                }
                            }
                        }
                    )
                    print("Success")

                except Exception as e:
                    print(e)
def lambda_handler(event, context):        
                message= event['Records'][0]['Sns']['Message']
                attributes = event['Records'][0]['Sns']['MessageAttributes']
                Token = event['Records'][0]['Sns']['MessageAttributes']['Token']['Value']
                Email = event['Records'][0]['Sns']['MessageAttributes']['Email']['Value']
                print(message)
                print(attributes)
                send_email(Email,Token)
                return {
                    'message' : message,
                    'attributes':attributes,
                    'Email' : Email
                }