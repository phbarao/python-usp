n = input("Digite uma letra de A a Z: ")

def vogal(n):
    vogais = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    if n in vogais:
        return True
    else:
        return False

print(vogal(n))
