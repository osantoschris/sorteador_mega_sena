import cria_lista, main
from random import choices
import os, locale
from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox

# Definindo a localização para pt-Br
locale.setlocale(locale.LC_ALL, 'pt-Br.utf-8')

# Definindo a data atual
data_atual = datetime.today().strftime('%d.%m.%y %H%M%S')

# Definindo o nome do arquivo
nome_arquivo = f'jogos_mega_sena{data_atual}.txt'

jogo = []
num_pares = main.num_par
num_impares = main.num_impar

def criar_jogo_pares():
    cria_lista.criar_lista()
    for x in range(num_pares):
        sorteado = choices(cria_lista.pares)[0] 
        jogo.append(sorteado)
        indice = cria_lista.pares.index(sorteado)
        del cria_lista.pares[indice]
    cria_lista.limpar_lista()

def criar_jogo_impares():
    cria_lista.criar_lista()
    for x in range(num_impares):
        sorteado = choices(cria_lista.impares)[0]
        jogo.append(sorteado)
        indice = cria_lista.impares.index(sorteado)
        del cria_lista.impares[indice]
    cria_lista.limpar_lista()

def criar_arquivo():
    jogo_ordenado = sorted(jogo)
    try:
        arquivo = open(f'C:\\Gerador Mega Sena\\sorteios\\{nome_arquivo}', 'a')
        arquivo.write(f'{jogo_ordenado}\n')
        jogo.clear()
        jogo_ordenado.clear()
    except:
        print('Erro ao gerar arquivo')

def gerar_jogos():
    criar_jogo_pares()
    criar_jogo_impares()
    criar_arquivo()

def abrir_arquivo_jogos():
    try:
        os.startfile('C:\\Gerador Mega Sena\\sorteios\\')
    except:
        messagebox.showerror('Atenção!', 'Nenhum arquivo foi gerado até o momento!')

def gerar_jogos_repeticoes():
    if qtde_jogos.get() != "":
        try:
            total_jogos = int(qtde_jogos.get())
            for i in range(total_jogos):
                gerar_jogos()
            qtde_jogos.delete(0, 'end')
            messagebox.showinfo('Jogos gerados!', f'Os {total_jogos} foram gerados com sucesso. Para abrir clique em "Abrir Jogos"')
        except:
            messagebox.showerror('Atenção!', 'Formato de número inválido!')
            qtde_jogos.delete(0, 'end')
            qtde_jogos.focus_set()
    else:
        messagebox.showerror('Atenção!', 'Inserir uma quantidade válida para a geração dos jogos!')
        qtde_jogos.focus_set()

janela = tk.Tk()
janela.title('Gerador de jogos Mega Sena')
janela.iconbitmap('C:\\Gerador Mega Sena\\icons\\loteria.ico')
janela.geometry("330x200")
janela.resizable(0,0)

texto = tk.Label(janela, text='Bem vindo ao gerador de jogos da Mega Sena')
texto.pack()

texto2 = tk.Label(janela, text='Digite a quantidade de jogos que deseja gerar: ')
texto2.pack(padx=10, pady=10)

qtde_jogos = tk.Entry(janela, width=18)
qtde_jogos.pack(padx=10, pady=10)

btn_gerar_jogo = ttk.Button(janela, text='Gerar Jogo', command=gerar_jogos_repeticoes, width=15)
btn_gerar_jogo.pack(padx=10, pady=10)

btn_abrir_arquivo = ttk.Button(janela, text='Abrir Jogos', command=abrir_arquivo_jogos, width=15)
btn_abrir_arquivo.pack(padx=10, pady=10)

qtde_jogos.focus_set()
janela.mainloop()