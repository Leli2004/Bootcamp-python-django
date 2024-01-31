### Exercícios banco de dados

## 1. Crie uma tabela chamada "alunos" com os seguintes campos: id (inteiro), nome (texto), idade (inteiro) e curso (texto).
import sqlite3 
conexao = sqlite3.connect('bd_exercicios')  # nome do arquivo criado no Dbeaver
cursor = conexao.cursor()

#cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(50), idade INT, curso VARCHAR(50));') 

## 2. Insira pelo menos 3 registros de alunos na tabela que você criou no exercício anterior
#cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES("1","Danieli","19","Téc Info"),("2","Marli","48","Adm"),("3","Xena","8","Dormir") ')

conexao.commit()

## 3. Consultas Básicas: Escreva consultas SQL para realizar as seguintes tarefas:
# a - Selecionar todos os registros da tabela "alunos"
#dados = cursor.execute('SELECT nome FROM alunos')
#for usuarios in dados:
#    print(dados)

# b - Selecionar o nome e a idade dos alunos com mais de 20 anos
#dados = cursor.execute('SELECT nome, idade FROM alunos WHERE idade>20')

# c - Selecionar os alunos do curso de "Engenharia" em ordem alfabética
#cursor.execute( 'INSERT INTO alunos (id, nome, idade, curso) VALUES("4","Daiane","27","Engenharia")')
#dados = cursor.execute('SELECT nome FROM alunos WHERE curso="Engenharia" ORDER BY nome DESC')

# d - Contar o número total de alunos na tabela

## 4. Atualização e Remoção: Atualize a idade de um aluno específico na tabela e Remova um aluno pelo seu ID
# dados = 
# cursor.execute('UPDATE alunos SET idade="20" WHERE nome="Danieli"')
#cursor.execute('DELETE FROM alunos where id=1')

########################################################################
## 5. Criar uma Tabela e Inserir Dados: Crie uma tabela chamada "clientes" com os campos: 
# id (chave primária), nome (texto), idade (inteiro) e saldo (float). 

# Insira alguns registros de clientes na tabela


## 6. Consultas e Funções Agregadas: Escreva consultas SQL para realizar as seguintes tarefas
# a - Selecione o nome e a idade dos clientes com idade superior a 30 anos
# b - Calcule o saldo médio dos clientes
# c - Encontre o cliente com o saldo máximo
# d - Conte quantos clientes têm saldo acima de 1000


## 7. Atualização e Remoção com Condições: Atualize o saldo de um cliente e Remova um cliente pelo seu ID


#for usuarios in dados:
#    print(dados)

conexao.close()

########################################################################
## 8. Junção de Tabelas: Crie uma segunda tabela chamada "compras" com os campos: id (chave primária), 
# cliente_id (chave estrangeira referenciando o id da tabela "clientes"), produto (texto) e valor (real). 
# Insira algumas compras associadas a clientes existentes na tabela "clientes". Escreva uma 
# consulta para exibir o nome do cliente, o produto e o valor de cada compra
