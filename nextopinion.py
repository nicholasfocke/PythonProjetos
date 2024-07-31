import os
class Usuario:

    lista = []

    def __init__(self, nome, email, senha, confirmar_senha):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.confirmar_senha = confirmar_senha

    def cadastrar_usuario(self):
        self.lista.append(self)

    def exibir_dados(self):
        for usuario in self.lista:
            print(f"Nome: {usuario.nome}")
            print(f"Email: {usuario.email}")
            print(f"Senha: {usuario.senha}")
            print(f"Confirmar Senha: {usuario.confirmar_senha}")

def validar_email(email):
    return "@" in email

def validar_senha(senha):
    return len(senha) == 8

def cadastrar_novo_usuario():
    nome_teste = input("Digite seu nome: ")
    email_teste = input("Digite seu email: ")

    while not validar_email(email_teste):
        print("Formato de email inválido. Certifique-se de incluir o '@' no email.")
        email_teste = input("Digite seu email: ")

    senha_teste = input("Digite sua senha (8 caracteres): ")
    confirmar_senha_teste = input("Confirme sua senha: ")

    while not (validar_senha(senha_teste) and senha_teste == confirmar_senha_teste):
        if not validar_senha(senha_teste):
            print("A senha deve ter exatamente 8 caracteres.")
        else:
            print("Senha e Confirmar Senha não coincidem.")
        senha_teste = input("Digite sua senha (8 caracteres): ")
        confirmar_senha_teste = input("Confirme sua senha: ")

    novo_usuario = Usuario(nome_teste, email_teste, senha_teste, confirmar_senha_teste)
    return novo_usuario

nome = input("Digite seu nome: ")
email = input("Digite seu email: ")

while not validar_email(email):
    print("Formato de email inválido. Certifique-se de incluir o '@' no email.")
    email = input("Digite seu email: ")

senha = input("Digite sua senha (8 caracteres): ")

while not validar_senha(senha):
    print("A senha deve ter exatamente 8 caracteres.")
    senha = input("Digite sua senha (8 caracteres): ")

confirmar_senha = input("Confirme sua senha: ")

while senha != confirmar_senha:
    print("Senha e Confirmar Senha não coincidem.")
    confirmar_senha = input("Confirme sua senha: ")

usuarioNovo = Usuario(nome, email, senha, confirmar_senha)
usuarioNovo.cadastrar_usuario()
print("Usuário cadastrado!")

usuarios = []
os.system("cls")
while True:
    print("Menu")
    print("1- Cadastrar novo usuário")
    print("2- Exibir dados dos usuários")
    print("3- Sair")
    escolha = input("Digite qual opção deseja: ")

    if escolha == "1":
        novo_usuario = cadastrar_novo_usuario()
        novo_usuario.cadastrar_usuario()
        usuarios.append(novo_usuario)
        print("Usuário cadastrado!")

    elif escolha == "2":
        mostrar_dados = input("Deseja que mostre os usuários cadastrados? [s]im ou [n]ão: ")
        if mostrar_dados.lower() == "s":
            usuarioNovo.exibir_dados()
        else:
            print("Fim do programa")

    elif escolha == "3":
        print("Saindo do programa...")
        break

    else:
        print("Escolha inválida!")
