# nome do arquivo e da função é padrão test_*.py
def test_config():
    assert 1==1

####### testar a model de cursos -> se os dados instanciados salvam corretamente no banco
from datetime import date
from model_bakery import baker
from cursos.models import Curso
import pytest 

@pytest.fixture
def curso():
    curso = baker.make(
        Curso,
        titulo = 'Java',
        data_do_curso = date.today(),
        carga_horaria = '20'
    )
    return curso

@pytest.mark.django_db
def test_str_deve_retornar_string(curso):
    assert str(curso) == 'Java: 2024-03-13 - 20'
