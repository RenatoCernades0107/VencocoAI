from EmbedingProducts import get_all_products, get_product_likes, get_product_shares
# TODO: Create a vector with the sum of all likes and shares for each product

def create_product_vector():
    """Creates a vector with the sum of likes and shares for each product"""
    products = get_all_products()
    product_vector = []
    maximum = -1
    for product in products:
        likes = get_product_likes(product)
        shares = get_product_shares(product)
        product_vector.append(likes + shares)

        if likes + shares > maximum:
            maximum = likes + shares
    
    for i in range(len(product_vector)):
        product_vector[i] /= maximum
        
    return product_vector