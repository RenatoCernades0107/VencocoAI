# VencocoAI

## Solution Architecture
<img src="/home/renato/Documents/VencocoAI/hackaton_belcorp.jpg">

### EmbedingProducts.py

The provided code snippet defines a function called create_product_vector(), which constructs a normalized vector representing the popularity of products based on their total likes and shares.

### GetPosts.py:


The provided code snippet defines functions to interact with the Facebook Graph API to retrieve likes and shares for products

### GetProducts.py:

The provided code snippet defines functions to interact with a DynamoDB table named BelcorpProducts to retrieve the names of all products stored in that table.

### Knn.py:

The provided code snippet defines a function that identifies the top
k products with the highest values based on a vector representing their popularity or features

### SkinAdvisorFeatures.py:

The provided code snippet defines a function to interact with the OpenAI ChatGPT API to identify the best products for specific skin characteristics based on data retrieved from a JSON file.

### GetClientResponses.py:

The provided code snippet outlines a process to extract client responses from a Google Sheet and store them in an Amazon DynamoDB table.


### ProcessClientResponses.py:


The provided code snippet outlines a process for analyzing client responses to determine the suitability of various products using the OpenAI API. It connects to AWS DynamoDB to retrieve client response data and product items, then evaluates each client's preferences against the items.