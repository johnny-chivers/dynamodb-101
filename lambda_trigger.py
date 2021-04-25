import json
import boto3 

'''
Lambda function to act as trigger to populate the order status table
'''

# client for dynamoDB 
dynamodb_client = boto3.client('dynamodb')

# set table 
customer_table = 'customer'
product_table = 'product'
address_table = 'address'
order_table = 'order'
order_status = 'order_status'


def lambda_handler(event, context):
    
    'The dynamoDB records are in nested inside the Record key'
    for record in event["Records"]:
        print(record)                   # prints to see what is going on in the logs
        print(record['eventName'])
        
        new_image = record["dynamodb"]["NewImage"]      # get the new image of the how the table item looks 
        item  = {
                    'order_status_id': {'S':'1'}
                    ,'order_id' :   new_image["order_id"]
                    ,'status': {'S':"order being processed"}
                }
        # put the item 
        resp = dynamodb_client.put_item(TableName = order_status, Item = item)
        print(resp)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
