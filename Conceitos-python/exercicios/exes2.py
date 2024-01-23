# 1 
# Faça um Programa que peça dois números e imprima o maior deles.
num1 = float(input('\nInforme o 1° número: '))
num2 = float(input('Informe o 2° número: '))

if num1>num2:
    print(f'Maior é {num1}')

elif num2>num1:
    print(f'Maior é {num2}')

##############################################################################
# 3
# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido
while True:
    nota_str = input('\nInforme a nota: ')

    if not nota_str.replace('.', '').isdigit():  # Verifica se a nota é um número válido
        print('\nValor informado é inválido.')  # Se a nota não for um valor numérico

    else:
        nota = float(nota_str) # converte para float
        
        if nota>10 or nota<0:
            print('\nValor informado é inválido.') 
    
        else:
            print('\nValor é inválido!')
            break

##############################################################################
# 6
# Crie um programa que solicite ao usuário um login e uma senha. O programa deve permitir o acesso apenas se o usuário for "admin" e a senha for "admin123", caso contrário imprima uma mensagem de erro.
user = "admin"
pwd = "admin123"

usuario = input('Usuário: ')
senha = input('Senha: ')

if usuario != user:
    print('\nErro. Usuário inválido"')
elif senha != pwd:
    print('\nErro. Senha inválida!')
else:
    print('Informações válidas!')

##############################################################################
# 9
# O programa deve calcular e apresentar a quantidade de números pares e ímpares inseridos. O processo de leitura deve ser encerrado quando o 
# usuário informar o valor zero. Certifique-se de incluir validações para garantir que apenas números positivos sejam considerados na contagem e cálculos.
def cont(num, numPar, numImpar):
    if num % 2 == 0:
        numPar += 1
        return numPar, numImpar
    else:
        numImpar += 1
        return numPar, numImpar

numPar = 0
numImpar = 0

while True:
    num = int(input('\nInforme um número inteiro: '))
    if num != 0:
        numPar, numImpar = cont(num, numPar, numImpar)
    elif num == 0:
        break

print(f'\nForam inseridos {numPar} números pares e {numImpar} números ímpares.')