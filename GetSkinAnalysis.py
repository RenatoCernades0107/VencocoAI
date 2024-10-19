from bs4 import BeautifulSoup

from bs4 import BeautifulSoup

with open("C:/Users/Jose/Downloads/Sofia.html", encoding="utf-8") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

tipo_piel = soup.body.find(style="flex: 1 1 0%;").div.get_text()

if tipo_piel == "Normal":
    tipo_piel_en = "Normal"

elif tipo_piel == "Sensible":
    tipo_piel_en = "Sensitive"

elif tipo_piel == "Seca":
    tipo_piel_en = "Dry"

elif tipo_piel == "Grasa":
    tipo_piel_en = "Oily"

elif tipo_piel == "Seca sensible":
    tipo_piel_en = "Dry & Sensitive"

elif tipo_piel == "Grasa sensible":
    tipo_piel_en = "Oily & Sensitive"

elif tipo_piel == "Mixta":
    tipo_piel_en = "Combination"

elif tipo_piel == "Mixta sensible":
    tipo_piel_en = "Combination & Sensitive"

items = soup.body.find_all(style="display: contents;")

def concern_es_to_en(word):
    if word == "Manchas":
        return "Spots"#
    
    elif word == "Arrugas":
        return "Wrinkles"#
    
    elif word == "Humedad":
        return "Moisture"#
    
    elif word == "Rojeces":
        return "Redness"#
    
    elif word == "Oleosidad":
        return "Oiliness"#
    
    elif word == "Canal lagrimal":
        return "tearThrough"
    
    elif word == "Textura":
        return "Texture"
    
    elif word == "Ojeras":
        return "darkCircles"
    
    elif word == "Bolsas de Ojos":
        return "eyeBags"
    elif word == "Firmeza":
        return "skinFirmness"
    elif word == "Párpado superior caído":
        return "droopyUpperEyelid"
    elif word == "Párpado inferior caído":
        return "droopyLowerEyelid"
    elif word == "Brillo":
        return "radiance"
    elif word == "Poros":
        return "visiblePores"
    
    else:
        return word

consumer_skin_concerns = {}

for item in items:
    score = item.div.div.get_text()

    concern = item.div.get_text()
    concern = concern_es_to_en(concern.replace(score, ""))

    # Meanwhile, score above 80 is false. No concern
    consumer_skin_concerns[concern] = True if int(score) < 80 else False


consumer_analysis = {
    "skinType": tipo_piel_en,
    "skinConcerns": consumer_skin_concerns
}

#Convert to json and show result
import json
print(json.dumps(consumer_analysis, indent=4))