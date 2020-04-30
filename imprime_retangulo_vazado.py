largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

def Quadrado(altura, largura, simbolo = '#', preenchimento = ' '):
    print(simbolo * largura)
    for _ in range(altura-2):
        print('{}{}{}'.format(simbolo, preenchimento * (largura - 2), simbolo))
    print(simbolo * largura)

Quadrado(altura, largura)
