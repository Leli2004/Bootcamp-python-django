#### Tratamento de erros
# Existem diversas except

def divisao(a,b):
    try:
        resultado = a/b 
        print(resultado)
    except ZeroDivisionError:
        print("\nErro: impossível dividir.")
    # 'as e' permite mostrar detalhes do erro ao uauário
    except TypeError as e:  
        print(f"\nErro: o tipo do dado informado está incorreto. Detalhes: {e}")

divisao(10,2)
divisao(10,0)
divisao(10,'texto')