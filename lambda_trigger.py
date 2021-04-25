'''
Lambda trigger
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
order_status = 'order-status'
