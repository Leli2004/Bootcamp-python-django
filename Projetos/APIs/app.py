#########################
###### Desafio API ######
#########################

#importar flask:
from flask import Flask, render_template

import urllib.request, json

app = Flask(__name__)  #varíavel que trabalha com flask

@app.route("/")
def main():
    return '<h1>Hello with Flask!</h1> <p><a href="/characters">Ver listagem de personagens</a></p> <p><a href="/locations">Ver listagem de localizações</a></p> <p><a href="/episodes">Ver listagem de episódios</a></p> <br> <p><a href="/json_characters">Ver listagem de personagens em JSON</a></p> <p><a href="/json_episodes">Ver listagem de episódios em JSON</a></p> <p><a href="/json_locations">Ver listagem de localizações em JSON</a></p>'


# Rota para chama o arquivo listagem-character.html
@app.route("/characters")
def lista_characters():
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    data_c = response.read()
    dicionario = json.loads(data_c)

    return render_template("character.html", characters=dicionario["results"])

# Rota para listar personagens em JSON
@app.route("/json_characters")
def lista_character_json():
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    characters = response.read()
    dicionario = json.loads(characters)

    characters = []

    for character in dicionario["results"]:
        character = {
            "name": character["name"],
            "status": character["status"],
            "species": character["species"]
        }
        characters.append(character)

    return {"characters": characters}


# Rota para chama o arquivo listagem-episodes.html
@app.route("/episodes")
def lista_episodes():
    url = "https://rickandmortyapi.com/api/episode"
    response = urllib.request.urlopen(url)
    data_e = response.read()
    dicionario = json.loads(data_e)

    return render_template("episodes.html", episodes=dicionario["results"])

# Rota para listar episodios em JSON
@app.route("/json_episodes")
def lista_episodes_json():
    url = "https://rickandmortyapi.com/api/episode"
    response = urllib.request.urlopen(url)
    episodes = response.read()
    dicionario = json.loads(episodes)

    episodes = []

    for episode in dicionario["results"]:
        episode = {
            "name": episode["name"],
            "air_date": episode["air_date"],
            "episode": episode["episode"]
        }
        episodes.append(episode)

    return {"episodes": episodes}


# Rota para chama o arquivo listagem-locations.html
@app.route("/locations")
def lista_locations():
    url = "https://rickandmortyapi.com/api/location"
    response = urllib.request.urlopen(url)
    data_l = response.read()
    dicionario = json.loads(data_l)

    return render_template("locations.html", locations=dicionario["results"])

# Rota para listar localizações em JSON
@app.route("/json_locations")
def lista_locations_json():
    url = "https://rickandmortyapi.com/api/location"
    response = urllib.request.urlopen(url)
    locations = response.read()
    dicionario = json.loads(locations)

    locations = []

    for location in dicionario["results"]:
        location = {
            "name": location["name"],
            "type": location["type"],
            "dimension": location["dimension"]
        }
        locations.append(location)

    return {"locations": locations}
