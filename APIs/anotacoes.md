Documentação sobre JSON:
- https://json-schema.org/ 
- https://www.json.org/json-pt.html 

Construir uma aplicação consumindo uma API pública
- Postman: http://postman.com/ 
- API pública: https://rickandmortyapi.com/ 
- Flask: https://flask.palletsprojects.com/en/3.0.x/ 
- FastAPI: https://fastapi.tiangolo.com/tutorial/ 

Flask:
1. py -m venv my-venv  #'my-venv' é o nome criado
2. my-venv\Scripts\activate
3. pip install Flask
4. set FLASK_APP=app  #app é o arquivo py
5. flask run

FastAPI
1. py -m venv my-venv  #'my-venv' é o nome criado
2. my-venv\Scripts\activate
3. pip install "fastapi[all]"
4. uvicorn app:app --reload  #app é o arquivo py
