# Criar um aplicativo Web de IA usando Python e Flask
- Prática do bootcamp envolvendo Python, Flask e serviços de IA do Microsoft Azure.
- Base: https://learn.microsoft.com/pt-br/training/modules/python-flask-build-ai-web-app/

### Proposta 
* Neste módulo, você compilará um site usando Flask e Serviços Cognitivos para traduzir texto.

### Objetivos 
* Aprender a configurar um ambiente de desenvolvimento Flask
* Aprender a usar o Flask para criar um formulário
* Aprender a usar o serviço de Tradução para traduzir texto

### Passos
###### 1. Configurar um ambiente de desenvolvimento: 
    - Configurar e ativar o ambiente virtual que utilizarei nesta prática, utilizando os comandos via terminal para Flask vistos anteriormente;
    - py -m venv my-venv 
    - my-venv\Scripts\activate 
    - pip install -r requirements.txt (baixar flask e bibliotecas)

###### 2. Criar o aplicativo principal: 
    - Nomeado 'app.py'
    - Foram adicionados no arquivo as importações e rota

###### 3. Criar o modelo HTML para o formulário:
    - Criar pasta template para arquivos HTML, para o front-end da rota definida

###### 4. Testar o aplicativo:
    - set FLASK_APP=app (definir o runtime do Flask para desenvolvimento)
    - flask run  (executar)
    - Visualizar no localhost

###### 5. Tradução (configurar):
    - Usa-se os serviços de IA do Azure, especificamente o serviço de tradução
    - É preciso logar na conta do Azure, para utilizar a chave da conta para conectar ao aplicativo Python
    - O arquivo .env é responsável por armazenar a chave que será utilizada neste aplicativo
    - No Azure: criar um recurso de tradutor e acessar 'Keys and Endpoint' para copiar a Key 1
    - Criar o arquivo .env e informar as credenciais retiradas do Azure

###### 6. Chamar o serviço de Tradução
    - Alterações no código para chamar o serviço, criar as rotas e adicionar a lógica para traduzir.
    - De modo geral, o código têm as seguintes funções: 
        a) Lê o texto que o usuário inseriu e o idioma selecionado no formulário
        b) Lê as variáveis ambientais que criamos anteriormente no arquivo .env
        c) Cria o caminho necessário para chamar o serviço de Tradução, que inclui o idioma de destino (o idioma de origem é detectado automaticamente)
        d) Cria as informações de cabeçalho, que incluem a chave para o serviço de Tradução, o local do serviço e uma ID arbitrária para a tradução
        e) Cria o corpo da solicitação, que inclui o texto que queremos traduzir
        f) Chama post em requests para chamar o serviço de Tradução
        g) Recupera a resposta JSON do servidor, que inclui o texto traduzido
        h) Recupera o texto traduzido (confira a nota a seguir)
        i) Chama render_template para exibir a página de resposta

###### 7. Criar o modelo para exibir resultados
    - Criar um HTML na pasta templates, chamado 'results.html'

###### 8. Testar a página
    - Comando flask run
    - Visualizar no localhost
    - Testar inserindo texto 
    - Registros na pasta 'prints' 
