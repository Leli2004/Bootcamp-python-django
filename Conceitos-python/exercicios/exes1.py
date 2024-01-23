# 2
# Peça ao usuário para informar o ano de nascimento.Em seguida, calcule e imprima a idade atual
ano = int(input('\nInforme seu ano de nascimento: '))

idade = 2024 - ano

print(f'\nSua idade em 2024 é {idade} anos.')

#####################################################
# 4
# Receba do usuário a quantidade de litros de combustível consumidos e a distância percorrida. 
# Calcule e imprima o consumo médio em km/l
litros = float(input('\nInforme a quantia de litros consumidos: '))
distancia = float(input('\nInforme a distância percorrida, em KM: '))

consumo = distancia / litros

print(f'\nO consumo médio é de {consumo} Km/l')

#####################################################
# 10
# Faça um Programa que utilize 4 variáveis como preferir e no final print uma mensagem amigável utilizando as variáveis criadas. 
nome = str(input('\nSeu nome: '))
local = str(input('Seu local: '))
profissão = str(input('Sua profissão: '))

print(f'\nOlá, {nome}!! Bom saber que você é de {local}, eu sou de Chapecó. Aqui é possível você encontrar vagas de {profissão}!')