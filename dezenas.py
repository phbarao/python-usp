entrada = input("Digite um número inteiro: ")
numero = int(entrada)

resto = numero % 100
dezena = resto // 10

print("O dígito das dezenas é",dezena)