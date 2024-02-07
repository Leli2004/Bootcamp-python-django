'''
    pasta .venv criada pelo terminal para usar o flask
    vídeo que explica como fazer: https://www.youtube.com/watch?v=ZnhwLx5sGjE
    comandos: 
        py -m venv my-venv
        my-venv\Scripts\activate
        pip install Flask
        set FLASK_APP=app
        flak run
        (seguir url e pronto)
'''

#importar flask:
from flask import Flask

import urllib.request, json

app = Flask(__name__)

#criar rota:
@app.route("/")

#def hello():
#    return '<h1>Olá, mundo!</h1>'

def get_list_characters():

    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    characters = response.read()
    dicionario = json.loads(characters) #formata para json
    characters = [] 

    for character in dicionario["results"]:
        character = {
            "name": character["name"],
            "status": character["status"]
        }
        characters.append(character)
    
    return {"characters": characters}

##este código acima puxa da API publica usada e lista em formato json na tela

