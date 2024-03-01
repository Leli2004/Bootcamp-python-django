# outra forma de criar urls, criando um arquivo de urls para cada aplicativo a fim de facilitar a organização

from django.urls import path
from cursos.views import criar_curso

app_name = 'Cursos'
urlpatterns = [
    path('criar_curso/', criar_curso, name='criar_curso')
    #outras
]
