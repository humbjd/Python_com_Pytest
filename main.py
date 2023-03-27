import pytest

# Definições

def somar_dois_numeros(num1, num2):
    return num1 + num2

def subtrair_dois_numeros(num1, num2):
    return num1 - num2

def multiplicar_dois_numeros(num1, num2):
    return num1 * num2

def dividir_dois_numeros(num1, num2):
    return num1 / num2

def elevar_um_numero_pelo_outro(num1, num2):
    return num1 ** num2

# Calcular e testar a area de um quadrado
# area = lado

def calcular_quadrado(num1, num2):
    return num1 ** num2


# Calcular e testar a area de um retangulo
# area = lado1 * lado2

def calcular_retangulo(num1, num2):
    return num1 * num2


# Calcular a area de um triangulo
# area = lado1 * lado2 / 2

def calcular_triangulo(num1, num2):
    return num1 * num2 / 2


if __name__ == '__main__':

# Requisições

    resultado = somar_dois_numeros(5, 7)
    print(f'A soma é {resultado}')

    resultado = subtrair_dois_numeros(7, 5)
    print(f' A subtração é {resultado}')

    resultado = multiplicar_dois_numeros(3, 5)
    print(f'A multiplicação é {resultado}')

    resultado = dividir_dois_numeros(8, 4)
    print(f'A divisão é {resultado}')

    resultado = elevar_um_numero_pelo_outro(2, 3)
    print(f'A exponeciação é {resultado}')

    resultado = calcular_quadrado(5, 5)
    print(f'O resultado do calculo é {resultado}')

    resultado = calcular_retangulo(4, 7)
    print(f'O resultado do calculo é {resultado}')

    resultado = calcular_triangulo(4, 5)
    print(f'O resultado do calculo é {resultado}')

# Teste

def testar_somar_dois_numeros():
    # - 1 - Configuração
    #  Dados / Valores
    # Entrada / Input
     num1 = 8
     num2 = 9
    # Saida / Output
    resultado_esperado = 17

    # - 2 - Executar
    resultado_atual = somar_dois_numeros(num1, num2)

    # - 3 - Confirmar / Check / Valida
    assert resultado_atual == resultado_esperado




