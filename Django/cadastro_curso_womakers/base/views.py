# Views são funções que indicam quais funcionaldiades constarão no sistema, respondendo às rotas (urls)
# As urls são definidas no arquivo urls do projeto

from http.client import HTTPResponse
from django.shortcuts import render
#from django.http import HttpResponse
from base.forms import CadastroForm

# criando e definindo a view início
def inicio(request):
    html = '''
        <!DOCTYPE html>
            <head>
                <title>Cursos online </title>
            </head>
            <body>
                <h1>Olá, mundo!</h1>
            </body>
        </html>
    '''
    #return HttpResponse(html)
    #return HttpResponse('Olá, mundo!')
    return render(request, 'inicio.html') # retornando o html escolhido


# criando e definindo a view cadastro
def cadastro(request):
    sucesso = False

    form = CadastroForm(request.POST or None)

    if form.is_valid(): # se envio for válido
        sucesso = True  # sucesso é True
        form.save() # salvar os dados do form no banco

    contexto = {  # guardar o contexto do form
        'form': form,
        'sucesso': sucesso #variável para enviar uma mensagem de sucesso no front
    }

    return render(request, 'cadastro.html', contexto) # contexto 
