# pasta .venv criada pelo terminal para usar o flask

#importar flask:
from flask import flask

app = Flask(__name__)
#criar rota:
@app.route('/')
#classe hello:
def hello():
    return '<h1>Olá, mundo!</h1>'

# comando para ativar o servidor local e rodar o arquivo:
# flask --app app run
# aí levanta o localhost na web
