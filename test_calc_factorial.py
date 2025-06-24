import math

#print(math.factorial(5))

def compute_factorial(number):
    # Calcule o fatorial de "number" usando a função fatorial interna do Python no módulo math.
    return math.factorial(number)



def test_compute_factorial():
    # Defina o número de entrada
    input_number = 5

    # Realize o cálculo fatorial
    result = compute_factorial(input_number)

    # Verifique se o resultado é igual ao valor fatorial esperado
    assert result == 120

    print("Teste aprovado! O fatorial de " + str(input_number) + " é " + str(result))