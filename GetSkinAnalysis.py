from bs4 import BeautifulSoup

from bs4 import BeautifulSoup

with open("C:/Users/Jose/Downloads/Sofia.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

bars = soup.body.div.div.find_all(role="progressbar")

scores = [i["aria-valuenow"] for i in bars]
cutanea = scores[0]
canal_lagrimal = scores[1]
ojeras = scores[2]
parpado_inferior_caido = scores[3]
bolsa_de_ojos = scores[4]
poros = scores[5]
rojeces = scores[6]
humedad = scores[7]
parpado_superior_caido = scores[8]
brillo = scores[9]
firmeza = scores[10]
manchas = scores[11]
arrugas = scores[12]
textura = scores[13]
oleosidad = scores[14]

print(f"Tu puntuacion cutanea es {cutanea}")
print(f"Tu puntuacion canal lagrimal es {canal_lagrimal}")
print(f"Tu puntuacion ojeras es {ojeras}")
print(f"Tu puntuacion parpado inferior caido es {parpado_inferior_caido}")
print(f"Tu puntuacion bolsa de ojos es {bolsa_de_ojos}")
print(f"Tu puntuacion poros es {poros}")
print(f"Tu puntuacion rojeces es {rojeces}")
print(f"Tu puntuacion humedad es {humedad}")
print(f"Tu puntuacion parpado superior caido es {parpado_superior_caido}")
print(f"Tu puntuacion brillo es {brillo}")
print(f"Tu puntuacion firmeza es {firmeza}")
print(f"Tu puntuacion manchas es {manchas}")
print(f"Tu puntuacion arrugas es {arrugas}")
print(f"Tu puntuacion textura es {textura}")
print(f"Tu puntuacion oleosidad es {oleosidad}")