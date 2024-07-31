pessoa = {
    "nome" : "Nicholas", 
    "sobrenome": "Focke",
    "idade" : 18,
    "altura": 1.77,
    "endereços": [

        {"rua": "tal tal", "numero" : 123},
        {"rua": "outra rua", "numero" : 321},
    ]
}

print(pessoa["nome"])
print(pessoa["sobrenome"])
print()

for chave in pessoa:
    print(chave, pessoa[chave])



#print(pessoa, type(pessoa)) 