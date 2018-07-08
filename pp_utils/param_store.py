import boto3
import os

class LambdaUtils:
    def __init__(self):
        #self.env = os.environ['ENV']
        pass
    def get_secret(self, keys):
        client = boto3.client('ssm', region_name='us-east-1')
        keylist = ','.join('"'+ item + '"' for item in keys)

        response = client.get_parameters(
            Names=keys,
            WithDecryption=True
        )
        return response
a = LambdaUtils()
vals = ['Test']
print(type(vals))
print(a.get_secret(vals))