import boto3
from time import sleep
from json import dumps

lam_client = boto3.client('lambda')

while 1:
    sleep(3)
    print(
        lam_client.invoke(
            FunctionName='matt-rookout',
            Payload=bytes(dumps({"apple": 11, "pineapple": 232}), 'utf-8')
        )
    )
