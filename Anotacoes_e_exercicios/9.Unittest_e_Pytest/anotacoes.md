## Tipos de teste
- Função: validar uma aplicação.
- Teste de unidade = teste da menor parte da lógica de código possível;
- Teste de integração = testar módulos em grupos;
- Teste funcional = geralmente exigem a execução de um aplicativo como um todo;
- Teste não funcional = funcionalidades testadas sob carga;
- Teste de usabilidade = interação humano-computador;
- Teste de desempenho = velocidade, estabilidade e escalabilidade;

## Pytest e Unittest
Testes de unidade com Django:
- Instalações: python -m pip install pytest-django / python -m pip install pytest
- Arquivo 'pytest.ini' auxilia para fazer todos os testes
- Executar: pytest
- É possível testar arquivos em grupo, exemplo: as models, as views, etc

#### Códigos
- test_assertions.py = exemplos usando o Unittest 
