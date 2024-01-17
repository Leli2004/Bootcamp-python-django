### Funções

def funcao():  # definição da função
    calculo = 10+3
    print(f'O resultado é: {calculo}')

funcao()  # chamar função

# definindo parametros
num1 = int(input('Informe o num1: '))
num2 = int(input('Informe o num2: '))

def multiplicacao(num1,num2):
    mult = num1*num2
    print(f'Resultado multiplicação é {mult}')

multiplicacao(num1,num2)  # passando parametros
