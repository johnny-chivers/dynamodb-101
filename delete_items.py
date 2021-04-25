'''
The following script deletes an item using the product, cusomter, address, and order tables. 

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

'''
Delete from product_table
'''
# need to set a key to elete 
key ={
    'product_id':{'S':'4'}
}

# delete
resp = dynamodb_client.delete_item(
    TableName = product_table,
    Key = key)
    
# print response 
print(resp)