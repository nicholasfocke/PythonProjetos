import tkinter as tk
from tkinter import messagebox

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
        dados = f"Nome: {self.nome}\nEmail: {self.email}\nSenha: {self.senha}\nConfirmar Senha: {self.confirmar_senha}"
        messagebox.showinfo("Dados do Usuário", dados)

def validar_email(email):
    return "@" in email

def validar_senha(senha):
    return len(senha) == 8

def cadastrar_novo_usuario(nome, email, senha, confirmar_senha):
    if not validar_email(email):
        messagebox.showerror("Erro", "Formato de email inválido. Certifique-se de incluir o '@' no email.")
        return False

    if not (validar_senha(senha) and senha == confirmar_senha):
        if not validar_senha(senha):
            messagebox.showerror("Erro", "A senha deve ter exatamente 8 caracteres.")
        else:
            messagebox.showerror("Erro", "Senha e Confirmar Senha não coincidem.")
        return False

    novo_usuario = Usuario(nome, email, senha, confirmar_senha)
    novo_usuario.cadastrar_usuario()
    return True

def cadastrar_novo_usuario_window():
    def cadastrar():
        nome = nome_entry.get()
        email = email_entry.get()
        senha = senha_entry.get()
        confirmar_senha = confirmar_senha_entry.get()
        
        if cadastrar_novo_usuario(nome, email, senha, confirmar_senha):
            messagebox.showinfo("Sucesso", "Usuário cadastrado!")
            novo_window.destroy()

    novo_window = tk.Toplevel(root)
    novo_window.title("Cadastrar Novo Usuário")

    tk.Label(novo_window, text="Nome:").grid(row=0, column=0, sticky='w')
    nome_entry = tk.Entry(novo_window)
    nome_entry.grid(row=0, column=1, padx=5, pady=5, sticky='w')

    tk.Label(novo_window, text="Email:").grid(row=1, column=0, sticky='w')
    email_entry = tk.Entry(novo_window)
    email_entry.grid(row=1, column=1, padx=5, pady=5, sticky='w')

    tk.Label(novo_window, text="Senha (8 caracteres):").grid(row=2, column=0, sticky='w')
    senha_entry = tk.Entry(novo_window, show="*")
    senha_entry.grid(row=2, column=1, padx=5, pady=5, sticky='w')

    tk.Label(novo_window, text="Confirmar Senha:").grid(row=3, column=0, sticky='w')
    confirmar_senha_entry = tk.Entry(novo_window, show="*")
    confirmar_senha_entry.grid(row=3, column=1, padx=5, pady=5, sticky='w')

    tk.Button(novo_window, text="Cadastrar", command=cadastrar).grid(row=4, columnspan=2, padx=5, pady=10)

def exibir_dados_usuarios():
    if Usuario.lista:
        for usuario in Usuario.lista:
            usuario.exibir_dados()
    else:
        messagebox.showinfo("Info", "Nenhum usuário cadastrado.")

def sair():
    if messagebox.askokcancel("Sair", "Deseja sair do programa?"):
        root.destroy()

root = tk.Tk()
root.title("Cadastro de Usuários")

tk.Button(root, text="Cadastrar Novo Usuário", command=cadastrar_novo_usuario_window).grid(row=0, column=0, padx=10, pady=10)
tk.Button(root, text="Exibir Dados dos Usuários", command=exibir_dados_usuarios).grid(row=1, column=0, padx=10, pady=10)
tk.Button(root, text="Sair", command=sair).grid(row=2, column=0, padx=10, pady=10)

root.mainloop()
