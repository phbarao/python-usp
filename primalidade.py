n = int(input('Digite um número inteiro: '))

def éPrimo (x):
    fator = 2
    while x % fator != 0 and fator < x/2:
        fator += 1
    if x % fator == 0:
        return False
    else:
        return True

while n > 0:
    if éPrimo(n):
        print (n, 'é primo')
    else:
        print (n, 'não primo')
    n = int(input('Digite um número inteiro: '))
