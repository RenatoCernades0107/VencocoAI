# TODO: For each product, request for Graph API with the product name
import requests
import json

def request_graph_api(product_name):
    """Requests the Graph API for the given product name"""
    token = '<YOUR_FACEBOOK_TOKEN>'
    url = f'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{product_name}&type=ad&access_token={token}'
    response = requests.get(url)
    return json.loads(response.text)


def get_product_data(product_name):
    """Returns the data for the given product name from the Graph API"""
    data = request_graph_api(product_name)
    if 'data' in data:
        return data['data']
    else:
        return []

def get_product_likes(product_name):
    """Returns the number of likes for the given product name"""
    data = get_product_data(product_name)
    likes = 0
    for item in data:
        likes += item['likes']
    return likes

def get_product_shares(product_name):
    """Returns the number of shares for the given product name"""
    data = get_product_data(product_name)
    shares = 0
    for item in data:
        shares += item['shares']
    return shares