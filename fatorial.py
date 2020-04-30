valor = int(input('Digite o valor de n: '))

fatorial = 1

while (valor > 1):
    fatorial = fatorial * valor
    valor -= 1

print(fatorial)
