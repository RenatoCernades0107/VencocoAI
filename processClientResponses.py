import boto3

# DynamoDB Setup
session = boto3.Session(
    aws_access_key_id="ACCESS_KEY_ID",
    aws_secret_access_key="SECRET_ACCES_KEY",
    aws_session_token="SESSION_TOKEN",  # Solo si usas credenciales temporales
    region_name="REGION"
)

# DynamoDB Sessión
dynamodb = session.resource("dynamodb", region_name="us-west-2")

# DynamoDB clientResponsesTable
client_responses = dynamodb.Table("clientResponses")
client_responses = client_responses["Items"]

# DynamoDB itemsTable

items_table = dynamodb.Table("itemsTable")
items_table = items_table["Items"]



import openai

openai.api_key = "your_openai_api_key"

def analyze_response(client_response, items):
    matrix_row = []
    
    for item in items:
        # Use OpenAI"s API to classify the response suitability
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"¿Este cliente prefiere este producto de acuerdo a su preferencia de producto? Respuesta del cliente: {client_response}. Item: {item}. Responde con un 1 si es adecuado o con un 0 si no es adecuado.",
            max_tokens=5
        )
        suitability = int(response["choices"][0]["text"].strip())
        matrix_row.append(suitability)
    
    return matrix_row

#Creating matrix
# Row are clients
# Cols are items
clients = client_responses
items = items_table

def merge_response(response):

    res = response["Pregunta1"]+response["Pregunta2"]+response["Pregunta3"]+response["Pregunta4"]+response["Pregunta5"]+response["Pregunta6"]+response["Pregunta7"]
    
    return res

suitability_matrix = []
for client in clients:
    client_response = merge_response(client)

    matrix_row = analyze_response(client_response, items)
    suitability_matrix.append(matrix_row)

