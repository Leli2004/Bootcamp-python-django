## Django web framework

#### Comandos no terminal
- pip install virtualenv (instalação local do ambiente virtual)
- python -m venv cadastro_curso_womakers (criação do ambiente virtual)
- .\Scripts\activate (ativação do ambiente - é preciso estar na pasta criada)

#### Comandos Django
- pip install django (instalar django)
- django-admin startproject projeto_womakers . (criar o projeto - 'projeto_womakers' é o nome escolhido)
- python manage.py runserver (rodar o servidor)
- python manage.py startapp base (começar novo aplicativo - 'base' é o nome escolhido)
- Por fim, é preciso registrar o novo aplicativo no projeto, acrescentando seu nome no arquivo 'settings'

#### Organização
- Na pasta do projeto criado ficam as configurações gerais no projeto e na pasta base ficam as funcionalidades
- Pasta base contém as funcionalidades com padrão MVT
- Pasta templates contém os arquivos HTML de front
- Pasta static contém CSS e JS (nesse projeto, foi importado direto do boostrap e colado aqui)
- Para o tópico acima, é preciso instalar o boostrap via terminal - comando: pip install django-bootstrap-v5 - e registrá-lo em 'settings'
- Form do django é composto por: classe principal, os fields (campos) e as widgets (como o campo será no html)

#### Banco de dados
- Utilimos o SQLite Viewer (extensão instalada pelo VsCode) - pode utilizar qualquer outro BD
- Arquivo criado por padrão: db.sqlite3 
- python manage.py makemigrations
- python manage.py migrate 
- Lógica na View para enviar os dados ao banco

#### O que faremos
- Projeto que simula um sistema de cadastro e gerenciamento de cursos online - pasta 'cadastro_curso_womakers'
- Integrando os conceitos abordados em todo o curso
