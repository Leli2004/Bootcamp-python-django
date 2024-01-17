#### Manipulaçao de arquivos

num1 = int(input('Informe o num1: '))
num2 = int(input('Informe o num2: '))

### manipulação de arquivos

def multiplicacao(num1,num2):
    mult = num1*num2
    file = 'arquivo.txt'

    ### Abertura de arquivo

    #abertura para escrita
    arquivo_escrita = open(file, "w") # w de write
    ### Escrita
    # apenas um comando para escrita
    arquivo_escrita.write("Texto a ser escrito")
    arquivo_escrita.close()

    # abertura para leitura
    arquivo_leitura = open(file, "r")  # r de read
    ### Leitura de arquivos
    leitura = arquivo_leitura.read() 
    print(leitura)
    arquivo_escrita.close()
    
    #abertura de arquivo binário
    arquivo_binario = open(file, "wb") 
        
    #print(f'Resultado multiplicação é {mult}')
    
multiplicacao(num1,num2)