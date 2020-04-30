list = []

def remove_repetidos (list):
    count = len(list)
    new_list = []
    for i in range(count):
        if list[i] in new_list:
            count -= 1
        else:
            new_list.append(list[i])
    return sorted(new_list)

print(remove_repetidos(list))
