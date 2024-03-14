# conexão com DBeaver

import sqlite3  # usar python junto com banco de dados

conexao = sqlite3.connect('bd-dbeaver')  # nome do arquivo criado no Dbeaver
cursor = conexao.cursor()

####################  Para alterar uma tabela

## Create
#cursor.execute('CREATE TABLE usuarios(id INT, nome VARCHAR(50));') 
#cursor.execute('CREATE TABLE produtos(id INT, nome VARCHAR(50));') 

## alter
#cursor.execute('ALTER TABLE usuarios RENAME TO usuario;') 
#cursor.execute('ALTER TABLE usuario ADD COLUMN telefone INT;') 

## drop
#cursor.execute('DROP TABLE produtos')

conexao.commit() # chama a conexão
conexao.close()  # encerra o processo

#################### Para alterar atributos da tabela
## delete
#cursor.execute('DELETE FROM usuario where id=1')

## select
# dados = cursor.execute('SELECT nome FROM usuario')
#for usuario in dados:
#    print(usuario)

## update
#cursor.execute('UPDATE usuario SET Endereco="Abc" WHERE nome="Danieli"')


#################### Outros comandos
## order by
# dados = cursor.execute('SELECT * FROM usuario ORDER BY nome DESC')
#for usuario in dados:
#    print(usuario)

## limit e distinct
# dados = cursor.execute('SELECT DISTINCT * FROM usuario LIMIT 3 ')
#for usuario in dados:
#    print(usuario)

## group by 
# dados = cursor.execute('SELECT nome FROM usuario GROUP BY nome')
#for usuario in dados:
#    print(usuario)

## having
# dados = cursor.execute('SELECT nome FROM usuario GROUP BY nome HAVING id>3')
#for usuario in dados:
#    print(usuario)
