import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkinter import *

# metodo de autenticacao de ususario

def autenticacao_usuario():
    usuario = txt_usuario.get()
    senha = txt_senha.get()

    # testando se a senha informada esta correta

    if usuario == "admin" and senha == "1234":
        messagebox.showinfo("Aviso", "Usuario e senha esta correto")
    else:
        messagebox.showinfo("Aviso", "Usuario e senha não conferem")

# metodo principal da funcao
def janela_login():
    pass

def main(false=None):
    global janela_login
    global txt_usuario
    global txt_senha

    # Criando a tela de login
    janela_login = Tk()

    # Definindo o tamanho da janela
    janela_login.geometry("730x430")

    # Titulo da janela de login
    janela_login.title("Login do Usuario")
    janela_login.resizable(width=false, heigth=false)

    # Configurando o grid
    janela_login.columnconfigure(0, weight=1)
    janela_login.columnconfigure(1, weight=3)

# nome do usuario
def label(janela_login, tect):
    pass

label_usuario = label(janela_login, tect="Usuário:")
label_usuario.grid(column=0, row=0, padx=15, pady=10)
txt_usuario = Entry(janela_login, width=28)
txt_usuario.grid(column=1, row=0, sticky=E, padx=15, pady=10)

# senha
label_senha = Label(janela_login, text="Senha:")
label_senha.grid(column=0, row=1, sticky=W, padx=15, pady=0)
txt_senha = Entry(janela_login, show="*", width=28)
txt_senha.grid(column=1, row=1, sticky=E, padx=15, pady=0)

# botão de login
btn_login = Button(janela_login, text="Entrar", command=autenticacao_usuario())
btn_login.grid(column=1, row=3, sticky=E, padx=15, pady=10)

# entramos no loop de eventos
janela_login.mainloop()

if __name__ == "_main_":
    main()