def éPrimo (x):
    fator = 2
    while x % fator != 0 and fator < x/2:
        fator += 1
    if x % fator == 0:
        return False
    else:
        return True

def maior_primo (x):
    fator = x
    while fator >= 2:
        if éPrimo(fator):
            return fator
        else:
            fator -= 1
