def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total
soma_1_2_3 = soma (1,2,3)
soma_4_5_6 = soma (4,5,6)
print(soma_1_2_3)
print(soma_4_5_6)