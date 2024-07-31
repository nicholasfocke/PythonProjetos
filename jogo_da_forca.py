import random

palavras_dicas = {
    "python": "é uma linguagem de programação de alto nível, interpretada de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte. Foi lançada por Guido van Rossum em 1991",
    "java": "é uma linguagem de programação orientada a objetos desenvolvida na década de 90 por uma equipe de programadores chefiada por James Gosling, na empresa Sun Microsystems, que em 2008 foi adquirido pela empresa Oracle Corporation",
    "javascript": "é uma linguagem de programação interpretada estruturada, de script em alto nível com tipagem dinâmica fraca e multiparadigma. Juntamente com HTML e CSS, o JavaScript é uma das três principais tecnologias da World Wide Web",
    "php": "é uma linguagem interpretada livre, usada originalmente apenas para o desenvolvimento de aplicações presentes e atuantes no lado do servidor, capazes de gerar conteúdo dinâmico na World Wide Web",
    "brasil": "é um país grande e seu idioma é o português"

}

def escolher_palavra():
    return random.choice(list(palavras_dicas.keys()))

def mostrar_palavra(palavra_secreta, letra_certa):
    palavra = ""
    for letra in palavra_secreta:
        if letra in letra_certa:
            palavra += letra
        else:
            palavra += "_"
    return palavra

def jogar_forca():
    palavra_secreta = escolher_palavra()
    maximo_tentativa = 7
    letra_certa = []
    tentativas_erradas = 0
    print("Jogo da Forca!")
    print("Dica:", palavras_dicas[palavra_secreta])
    print("Palavra:", mostrar_palavra(palavra_secreta, letra_certa))
    
    while tentativas_erradas < maximo_tentativa:
        letra = input("Digite uma letra ou 'dica' para receber uma dica: ").lower()
        
        if letra == "dica":
            print("Dica:", palavras_dicas[palavra_secreta])
            continue
        
        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, digite apenas uma letra válida.")
            continue
        
        if letra in letra_certa:
            print("Você já tentou esta letra. Tente outra.")
            continue

        if letra in palavra_secreta:
            letra_certa.append(letra)
        else:
            tentativas_erradas += 1
            print("Letra errada! Você tem mais", maximo_tentativa - tentativas_erradas, "tentativas.")

        palavra_atual = mostrar_palavra(palavra_secreta, letra_certa)
        print("Palavra:", palavra_atual)
        
        if palavra_atual == palavra_secreta:
            print("Parabéns, você acertou!")
            break
        
        if tentativas_erradas == maximo_tentativa:
            print("Você perdeu! A palavra correta era:", palavra_secreta)

jogar_forca()
