lista = [
    {'nome': 'Luiz', 'sobrenome':'miranda' },
    {'nome': 'Maria', 'sobrenome':'Oliveira'},
    {'nome': 'Nicholas', 'sobrenome':'Focke'},
    {'nome': 'Frida', 'sobrenome':'Gois'},
    {'nome': 'Filipe', 'sobrenome':'Esteves'},
]
 
def exibir(lista):
    for item in lista:
        print(item)

    print()

l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)
