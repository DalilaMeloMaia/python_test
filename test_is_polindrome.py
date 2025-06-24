
def is_palindrome(word):
    # Inverta a string usando reversed() e join().
     reversed_str = ''.join(reversed(word))
    # Verifique se a palavra original é a mesma que sua versão invertida.
     return word == reversed_str

def test_is_palindrome():
    input_str = "osso"
    result = is_palindrome(input_str)

    assert result == True
    print("Teste aprovado! '" + input_str + "' é um palíndromo.")