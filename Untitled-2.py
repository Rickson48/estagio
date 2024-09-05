def count_a_in_string(text):
    count = text.lower().count('a')
    return f"A letra 'a' aparece {count} vezes na string."

# String de entrada
string = input("Informe uma string: ")
print(count_a_in_string(string))
