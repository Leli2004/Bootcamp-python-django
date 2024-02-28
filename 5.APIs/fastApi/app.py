'''
############ EXEMPLO 1 - OLÁ, MUNDO ############

from fastapi import FastAPI 
from typing import Union 

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Olá, mundo!"}

@app.get("/item/{item.id}")
async def read_item(item_id: int, busca: Union[str, int] = None):
    return {"item_id": item_id, "busca": busca} 
'''

############ EXEMPLO 2 - HTTP ############
# get, post, delete

from fastapi import FastAPI
from uuid import UUID, uuid4 
from typing import List
from models import User, Role

app = FastAPI()

# db instancia 3 objetos, funcionando como um dicionario de dados
db: List[User] = [
    User(
        #id=uuid4(),
        id = UUID("82cebf8c-b4f8-427d-aa5c-63cf65f7ea93"),
        first_name = "Ana",
        last_name = "Maria",
        email = "anamaria@gmail.com",
        role = [Role.role_1]
    ),
    User(
        #id=uuid4(),
        id = UUID("31f4365f-534f-4e5d-ba12-1b3635f55a8e"),
        first_name = "Dani",
        last_name = "Nasc",
        email = "dani@gmail.com",
        role = [Role.role_2]
    ),
    User(
        #id=uuid4(),
        id = UUID("5140526d-f965-4a36-b4bd-d66e3f7535ed"),
        first_name = "Camila",
        last_name = "Silva",
        email = "silva@gmail.com",
        role = [Role.role_3]
    )
]

@app.get("/")
async def root():
    return {"message": "Aulas HTTP"}

# listar todos os usuarios em JSON
@app.get("/api/users")
async def get_users():
    return db

# Pegar usuario pelo id descrito na url
@app.get("/api/users/{id}")
async def get_user():
    for user in db:
        return user
    return {"message":"Usuário não encontrado."}

# Criando usuários na listagem
@app.post("/api/users")
async def add_user(user: User):
    db.append(user)
    return {"id":user.id}

# remover usuário
app.delete("/api/users/{id}")
async def remove_user(id: UUID):
    for user in db:
        if user == id:
            db.remove(user)
            return {"message":"Usuário deletado com sucesso!"}
