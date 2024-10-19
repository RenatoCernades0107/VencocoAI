# TODO: TOP k products with the highest values in the vector
from EmbedingProducts import create_product_vector, get_all_products
from SkinAdvisorFeatures import get_skin_advisor_features

def top_k_products(k):
    """Returns the top k products with the highest values in the vector"""
    product_vector = create_product_vector()
    product_vector += get_skin_advisor_features()
    sorted_products = sorted(zip(product_vector, get_all_products()), reverse=True)
    top_k = [product for _, product in sorted_products[:k]]
    return top_k


