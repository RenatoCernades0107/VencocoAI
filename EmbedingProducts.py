from EmbedingProducts import get_all_products, get_product_likes, get_product_shares
# TODO: Create a vector with the sum of all likes and shares for each product

def create_product_vector():
    """Creates a vector with the sum of likes and shares for each product"""
    products = get_all_products()
    product_vector = []
    for product in products:
        likes = get_product_likes(product)
        shares = get_product_shares(product)
        product_vector.append(likes + shares)
    return product_vector