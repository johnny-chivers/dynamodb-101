'''
The following script executes a dynamodb transaction an item using the product, cusomter, address, and order tables. 

These tables were set up in lesson 1

The partition key, sort key and table names must all align for the following scripts to work. 

The below is  wrote as a simple linear script so it is easy to follow 
'''


# boto3 libary for interacting with AWS 
import boto3 

# client for dynamoDB 
dynamodb_client = boto3.client('dynamodb')

# set table 
customer_table = 'customer'
product_table = 'product'
address_table = 'address'
order_table = 'order'



response = dynamodb_client.transact_write_items(
    TransactItems=[
        {
            'Update': {
                'TableName':product_table,
                'Key': {
                    'product_id': { 'S': '1' }
                },
                'UpdateExpression': 'SET stock = stock - :decr',
                'ExpressionAttributeValues': {
                  ':decr': { 'N': '1' }
                },
                 'ConditionExpression': 'stock >= :decr'
            }
        },
        {
            'Put': {
                'TableName': order_table,
                'Item': {
                    'order_id': { 'S': '2' },
                    'product_id':{'S':'1'},
                    'customer_id':{'S':'1'},
                    'address_id':{'S':'1'}
                }
            }
        }
    ]
)

print(response)