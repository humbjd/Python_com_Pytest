# Definições

def somar_dois_numeros(num1, num2):
    return num1 + num2

def subtrair_dois_numeros(num1, num2):
    return num1 - num2

def multiplicar_dois_numeros(num1, num2):
    return num1 * num2

def dividir_dois_numeros(num1, num2):
    return num1 / num2

# Requisições

resultado = somar_dois_numeros(5, 7)
print(f'A soma é {resultado}')

resultado = subtrair_dois_numeros(7, 5)
print(f' A subtração é {resultado}')

resultado = multiplicar_dois_numeros(3, 5)
print(f'A multiplicação é {resultado}')

resultado = dividir_dois_numeros(8, 4)
print(f'A divisão é {resultado}')


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




