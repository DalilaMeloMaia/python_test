def reverse_string(word):
    return ''.join(reversed(word))

def test_reverse_string():
    input_str = "TripleTen"

    reversed_str = reverse_string(input_str)

    assert reversed_str == "neTelpirT"

    print("Teste Approval! " + input_str + " inverter é " + reversed_str)

test_reverse_string()
