perguntas = [
    {
        "Pergunta": "Quanto é 100²? ",
        "Opções": ["200", "2000", "100", "1000", "10000"],        
        "Resposta": "10000",
    },
    {
        "Pergunta": "Qual a capital da Ucrânia?  ",
        "Opções": ["Lisboa", "Oslo", "Kiev", "Moscou", "Berlim"],        
        "Resposta": "Kiev",
    },
    {
        "Pergunta": "Qual a derivada de x²?  ",
        "Opções": ["x²/2", "x³/3", "x²", "x³", "x"],        
        "Resposta": "x³/3",
    }
]

qtd_acertos = 0

for pergunta in perguntas:
    print("Pergunta:", pergunta["Pergunta"])
    print()

    opcoes = pergunta["Opções"]
    for i,  opcao in enumerate (opcoes):
        print(f'{i})', opcao) 
    print()
    
    escolha = input("Escolha uma opção: ")

    acertou = False  

    escolha_int = None
    
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta["Resposta"]:
                acertou = True

    print()
    if acertou:
        qtd_acertos +=1
        print("Acertou!")
    else:
        print("Errou!")

    print()
print(f"Você acertou {qtd_acertos} de {len(perguntas)} perguntas!")