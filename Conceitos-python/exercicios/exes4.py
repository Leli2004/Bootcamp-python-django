## 1
# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
def somando():
    # Solicita 3 input
    num1 = float(input('Informe o 1° número: '))
    num2 = float(input('Informe o 2° número: '))   
    num3 = float(input('Informe o 3° número: '))  

    # Calculando a soma
    soma = num1+num2+num3

    # Imprimindo o resultado
    print(f'O resultado da soma é: {soma}')

# Chamando a função
somando()

######################################################
## 2
''' Reverso do número. 
    Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.
'''
def inverte(numero):
    # Convertendo para string para facilitar a inversão
    numero_str = str(numero)
    
    # Invertendo a string
    numero_invertido = numero_str[::-1]
    
    # Convertendo de volta para inteiro
    numero_invertido = int(numero_invertido)
    
    return numero_invertido

numero_original = str(input('\nInforme um número inteiro: '))

numero_reverso = inverte(numero_original)

print(f'\nO reverso de {numero_original} é {numero_reverso}')

######################################################
## 3
''' Escreva um script que pergunta ao usuário se ele deseja converter uma temperatura de grau Celsius para Fahrenheit ou vice-versa. 
    Para cada opção, crie uma função.  
    Crie uma terceira, que é um menu para o usuário escolher a opção desejada, onde esse menu chama a função de conversão correta.
'''
# Definindo um valor padrão na variável
temp = 50
print(f'\nA temperatura definida inicialmente é de {temp} °C.')

# Função Celcius para Fahrenheit
def CparaF(temp):
    return temp * 1.8 + 32

# Função Fahrenheit para Celcius
def FparaC(temp):
    return (temp - 32) / 1.8

# Função para escolher a medida a converter
def escolher():
    print('\n-> Deseja converter para qual medida?')
    print('C - para Celcius')
    print('F - para Fahrenheit')
    escolha = str(input('Digite sua escolha: '))
    
    if escolha == 'C':
        resultado = FparaC(temp)
        print(f'\nA temperatura em Celsius é {resultado} °C.')

    elif escolha == 'F':
        resultado = CparaF(temp)
        print(f'\nA temperatura em Fahrenheit é {resultado} °F.')

# Função principal 
def main():
    # loop que solicita o tipo de conversão
    while True:
        print('\n-> Deseja converter a temperatura?')
        print('S - para sim')
        print('N - para não')
        converte = str(input('Digite sua escolha: '))

        # Condicional para chamar a função correta em cada conversão
        if converte == 'S':
            escolher()
        elif converte == 'N':
            print('\nOk, sem conversão.')
            break  # quebra do loop

# Chamando a função main
main()
