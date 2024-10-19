import json
from GetProducts import get_all_products

# TODO: Use chatgpt api to ask a question

import requests
import json


def get_skin_advisor_features(): 
    # Tu clave de API de OpenAI
    API_KEY = "tu-clave-de-api-aqui"

    # Endpoint de la API de OpenAI
    url = "https://api.openai.com/v1/chat/completions"

    # Configuración de los headers
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    # El cuerpo de la solicitud, donde defines el modelo y el mensaje
    jfile = json.load(open('mock_skin_advisor.json', 'r', encoding='utf-8'))
    data = {
        "model": "gpt-3.5-turbo",  # Modelo que deseas utilizar
        "messages": [
            {"role": "system", "content": f"Which of these products: ({get_all_products()} are the best for these skin characteristics {jfile.dumps()}). Give me the answer as a list separated by comma"},
        ],
        "temperature": 0.5  # Controla la creatividad de la respuesta
    }

    # Realizar la solicitud POST a la API de OpenAI
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Convertir la respuesta a JSON
        response_data = response.json()
        
        # Obtener la respuesta de ChatGPT
        reply = response_data['choices'][0]['message']['content']
        
        product_names = reply.split(',')

        vec = []
        for product in get_all_products():
            if product == product_names:
                vec.append(1)
            else:
                vec.append(0)
        return vec
            
    else:
        # Mostrar el error en caso de que la solicitud falle
        print(f"Error: {response.status_code}")
        print(response.text)
        return [0 for i in range(get_all_products())]
