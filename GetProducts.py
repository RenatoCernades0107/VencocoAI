# TODO: Select all the products name of dynamodb called BelcorpProducts

import boto3

def get_products_table():
    """Returns the DynamoDB table for BelcorpProducts"""
    dynamodb = boto3.resource('dynamodb')
    return dynamodb.Table('BelcorpProducts')

def get_all_products():
    """Returns all products name from the BelcorpProducts table"""
    table = get_products_table()
    response = table.scan()
    products = []
    for item in response['Items']:
        products.append(item['name'])
    return products
