import pytest
from main import somar_dois_numeros
# Teste

def testar_somar_dois_numeros():
    # - 1 - Configuração
    #  Dados / Valores
    # Entrada / Input
     num1 = 4
     num2 = 5
    # Saida / Output
    resultado_esperado = 9

    # - 2 - Executar
    resultado_atual = somar_dois_numeros(num1, num2)

    # - 3 - Confirmar / Check / Valida
    assert resultado_atual == resultado_esperado
