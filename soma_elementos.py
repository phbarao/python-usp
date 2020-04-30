list = []

def soma_elementos(list):
    count = len(list)
    sum = 0
    for i in range(count):
        sum += list[i]
    return sum

print(soma_elementos(list))
