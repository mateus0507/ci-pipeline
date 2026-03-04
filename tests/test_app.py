# Importa a função soma que está no arquivo app.py
from app import soma


# Função de teste que o pytest vai executar automaticamente
def test_soma():

    # Verifica se 2 + 2 é igual a 4
    assert soma(2, 2) == 4