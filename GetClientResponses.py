import boto3
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheets API Setup
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('key.json', scope) #enter json key
client = gspread.authorize(creds)

# Open the Google Sheet
sheet = client.open('clientResponses').sheet1
data = sheet.get_all_records()  # Extracts all records


# DynamoDB Setup
session = boto3.Session(
    aws_access_key_id='your_access_key_id',
    aws_secret_access_key='your_secret_access_key',
    aws_session_token='your_session_token',  # Solo si usas credenciales temporales
    region_name='your_region'
)

# DynamoDB Setup
dynamodb = session.resource('dynamodb', region_name='us-west-2')
table = dynamodb.Table('clientResponses')

# Insert data into DynamoDB
for row in data:
    table.put_item(
        Item={
            'timestamp': row['Timestamp'], 
            'Email': str(row['Email']), # Primary key
            'pregunta1': row['Pregunta1'],
            'pregunta2': row['Pregunta2'],
            'pregunta3': row['Pregunta3'],
            'pregunta4': row['Pregunta4'],
            'pregunta5': row['Pregunta5'],
            'pregunta6': row['Pregunta6'],
            'pregunta7': row['Pregunta7']
        }
    )

