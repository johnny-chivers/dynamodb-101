'''
The following script adds data to the product, cusomter, address, and order table. 

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
Set up customer_table
'''

# item for table
item  = {
        'customer_id':{'S':'1'}
        ,'first-name':{'S':'John'}
        ,'last-name':{'S':'Doe'}
                
        }
    
# put item into dynamo 
resp = dynamodb_client.put_item(TableName = customer_table, Item = item)

# item for table
item  = {
        'customer_id':{'S':'2'}
        ,'first-name':{'S':'Jane'}
        ,'last-name':{'S':'Doe'}
                
        }
    
# put item into dynamo 
resp = dynamodb_client.put_item(TableName = customer_table, Item = item)


# item for table
item  = {
        'customer_id':{'S':'3'}
        ,'first-name':{'S':'Jack'}
        ,'last-name':{'S':'Sparrow'}
                
        }
    
# put item into dynamo 
resp = dynamodb_client.put_item(TableName = customer_table, Item = item)


'''
Set up product_table
'''

# item for table
item  = {
        'product_id':{'S':'1'}
        ,'description':{'S':'Ipad'}
        ,'stock':{'N': '5'}
        }
    
# put item into dynamo 
resp = dynamodb_client.put_item(TableName = product_table, Item = item)

# item for table
item  = {
        'product_id':{'S':'2'}
        ,'description':{'S':'Iphone'}   
        ,'stock':{'N': '5'}
        }
    
# put item into dynamo 
resp = dynamodb_client.put_item(TableName = product_table, Item = item)

# item for table
item  = {
        'product_id':{'S':'3'}
        ,'description':{'S':'Imac'}     
        ,'stock':{'N': '5'}
        }
    
# put item into dynamo 
resp = dynamodb_client.put_item(TableName = product_table, Item = item)

# item for table
item  = {
        'product_id':{'S':'4'}
        ,'description':{'S':'Air Pods'}     
        ,'stock':{'N': '5'}
        }
    
# put item into dynamo 
resp = dynamodb_client.put_item(TableName = product_table, Item = item)



'''
Set up address_table
'''

# item for table
item  = {
        'address_id':{'S':'1'}
        ,'customer_id':{'S':'1'}     
        ,'street':{'S':'123 made up st'}     
        }
    
# put item into dynamo 
resp = dynamodb_client.put_item(TableName = address_table, Item = item)

# item for table
item  = {
        'address_id':{'S':'4'}
        ,'customer_id':{'S':'1'}     
        ,'street':{'S':'123 shipping st'}     
        }
    
# put item into dynamo 
resp = dynamodb_client.put_item(TableName = address_table, Item = item)


# item for table
item  = {
        'address_id':{'S':'2'}
        ,'customer_id':{'S':'2'}     
        ,'street':{'S':'456 no where land'}     
        }
    
# put item into dynamo 
resp = dynamodb_client.put_item(TableName = address_table, Item = item)

# item for table
item  = {
        'address_id':{'S':'3'}
        ,'customer_id':{'S':'3'}   
        ,'street':{'S':'78 near the port'}     
        }
    
# put item into dynamo 
resp = dynamodb_client.put_item(TableName = address_table, Item = item)



