# Use um diretório testes para posicionar arquivos de teste e diretórios de teste aninhados.
# Usar o prefixo test nos arquivos de teste. O prefixo indica que o arquivo contém código de teste.

def test_main():
    assert "a string value" == "a string value"

def test_main():
    assert True

# tests for-loop
def test_string_is_digit():
    items = ["1", "10", "33"]
    for item in items:
        assert item.isdigit()

#########################################
# trabalhando com fixtures
import pytest
import tempfile

@pytest.fixture
def tmp_file():
    def create():
        temp = tempfile.NamedTemporaryFile(delete=False)
        return temp.name
    return create

#########################################
