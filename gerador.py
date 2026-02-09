import random
from faker import Faker
import tkinter as tk
import ttkbootstrap as ttk

#código
fake = Faker("pt_BR")

def gera_nome():
    nome_masc = ["João", "Pedro", "Lucas", "Mateus", "Matheus", "Gabriel",
    "Rafael", "Daniel", "Bruno", "Felipe", "Diego", "Thiago",
    "André", "Leonardo", "Guilherme", "Vitor", "Victor", "Eduardo",
    "Henrique", "Rodrigo", "Caio", "Igor", "Samuel", "Renato",
    "Fernando", "Ricardo", "Alexandre", "Marcos", "Fábio", "Paulo",
    "Vinícius", "Arthur", "Heitor", "Enzo", "Davi", "Luan",
    "Murilo", "Nathan", "Yuri", "Otávio", "Cauã", "Bryan",
    "Pablo", "Wesley", "Douglas", "Jonathan", "Patrick", "Jeferson"]

    sobrenomes = ["Silva", "Santos", "Oliveira", "Pereira", "Costa", "Rodrigues",
    "Alves", "Lima", "Gomes", "Ribeiro", "Martins", "Araujo",
    "Carvalho", "Souza", "Teixeira", "Fernandes", "Azevedo",
    "Rocha", "Barbosa", "Melo", "Nogueira", "Batista",
    "Freitas", "Farias", "Moreira", "Moura", "Cavalcante",
    "Campos", "Pinto", "Macedo", "Ramos", "Lopes",
    "Fonseca", "Guimarães", "Monteiro", "Tavares",
    "Correia", "Duarte", "Mendes", "Torres", "Amaral",
    "Pacheco", "Assis", "Borges", "Figueiredo",
    "Vieira", "Rezende", "Barros", "Peixoto"]

    res.set(f"{random.choice(nome_masc)} {random.choice(sobrenomes)}")

def gera_cartao():
    res.set(f"{fake.credit_card_number()}\n{fake.credit_card_expire()}\n{fake.credit_card_security_code()}")

def gera_cpf():
    res.set(f"{fake.cpf()}")

def copiar():
    texto = res.get()
    if texto:
        janela.clipboard_clear()
        janela.clipboard_append(texto)
        janela.update()


#interface gráfica
janela = tk.Tk()
estilo = ttk.Style("vapor")
janela.title("Gerador de dados")
janela.geometry("300x250")
titulo = tk.Label(janela, text="Gerador de dados")
titulo.grid(row=0, column=0, columnspan=3, pady=35)
titulo.config(font=("Arial", 20, "bold"))
janela.columnconfigure((0, 1, 2), weight=1)
botao_nome = ttk.Button(janela, text="Nome", command=gera_nome)
botao_nome.grid(row=1, column=0, padx=5, pady=5)
botao_cpf = ttk.Button(janela, text="CPF", command=gera_cpf)
botao_cpf.grid(row=1, column=1, padx=5, pady=5)
botao_cartao = ttk.Button(janela, text="Cartão", command=gera_cartao)
botao_cartao.grid(row=1, column=2, padx=5, pady=5)
botao_copiar = ttk.Button(janela, text="Copiar", command=copiar)
botao_copiar.grid(row=3, column=1, padx=5, pady=5)
res = tk.StringVar()
res.label = tk.Label(janela, textvariable=res)
res.label.grid(row=2, column=0, columnspan=3, pady=10)
janela.mainloop()
