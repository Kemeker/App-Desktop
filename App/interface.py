import openpyxl
import pandas as pd
from tkinter import ttk
import tkinter as tk
import datetime as dt


'''------------------------criar o acesso ao banco de dados----------------------------------------------------'''
def abrir_BD() -> openpyxl.Workbook:
    BD: openpyxl.Workbook = openpyxl.load_workbook(r'App\banco_dados.xlsx')
    return BD
def fechar_BD(BD: openpyxl.Workbook):
    BD.save(r'App\banco_dados.xlsx')
    BD.close()
'''------------------------------------------------------------------------------------------------------------'''

'''------------------------funcoes com a tabela workbook-------------------------------------------------------'''
def dimencoes_tabela():
    '''o openpyxl não dimenciona onde começa e termina a tabela,
    essa função vai achar a linha e coluna inicial e final.
    para usar faça: colI, colF, linI, linF = dimencoes_tabela()'''

    #setando variaveis:
    colI = 0
    colF = 0
    linI = 0
    linF = 0

    #abrindo BD
    BD = abrir_BD()


    #achando primeira linha e coluna:
    for col in range(1,101,1):
        if linI > 0:
            break
        for lin in range(1,101,1):
            if BD.active.cell(row=lin,column=col).value != None:
                linI = lin
                colI = col
                break

    #encontrar ultima linha:
    for lin in range(linI,1_000_000,1):
        if BD.active.cell(row=lin+1,column=colI).value == None:
            linF = lin
            break
    #encontrar ultima coluna:
    for col in range(colI,1000,1):
        if BD.active.cell(row=linI,column=col+1).value == None:
            colF = col
            break
    fechar_BD(BD)
    return colI,colF,linI,linF
def puxar_cabecalho():
    '''essa puxa somente o cabecalho tabela do BD'''
    BD = abrir_BD()
    colI, colF, linI, linF = dimencoes_tabela()
    cabecalho = []
    for col in range(colI,colF+1,1):
        cabecalho.append(BD.active.cell(row=linI,column=col).value)
def puxar_tabela() -> list:
    '''essa puxa somente o corpo tabela do BD'''
    BD = abrir_BD()
    colI, colF, linI, linF = dimencoes_tabela()

    tabela = []
    for lin in range(linI+1,linF+1,1):
        linha = []
        for col in range(colI,colF+1,1):
            linha.append(BD.active.cell(row=lin,column=col).value)
        tabela.append(linha)
    fechar_BD(BD)
    return tabela
def coluna_em_lista(tabela: list, coluna: int) -> list:
    '''essa funcão é pra gerar uma lista da coluna desejada da tabela
    (como usar: tabela[a tabela puxada da funcao PUXAR TABELA], numero da coluna.)'''
    lista = []
    for item in tabela:
        lista.append(item[coluna])
    return lista
'''------------------------------------------------------------------------------------------------------------'''

'''------------------------------ puxando informacoes da lista-------------------------------------------------'''
tabela = puxar_tabela() #sua tabela não tem mais de uma coluna, mesmo assim, a tabela é gerada como matriz.
lista = coluna_em_lista(tabela,0)
'''------------------------------------------------------------------------------------------------------------'''
'''---------------------------------Janela para cadastro de ferramentas-------------------------------------------'''
""""""
#def abrir_janela_cadastro:
#janela_cadastro = tk.Tk()
#botao = tk.Button(janela_cadastro, text="Cadastrar ferramenta", command=abrir_janela_cadastro)



#janela_cadastro.mainloop()

'''-----------------------------------------------------------------------------------------------------------------'''

# Janela para solicitaçao de ferramenta

'''----------------------------------------------------------------------Listas-------------------------------------''' 
lista_voltagem = ["110v","220v","360v","110v~220v"]
#lista_ferramentas = ["Chave de Fenda", "Chave Philips", "Alicate Universal", "Alicate Diagonal de Corte", "Martelo", "Parafusadeira Dewalt", "Furadeira Bosch", "Grampeadeira Eletrica", "Serrote", "Serra Arco", ]
'''------------------------------------------------------------------------------------------------------------------'''

'''-----------------------------------------------------------Parametros da janela----------------------------------'''
janela = tk.Tk() 
janela.geometry("900x600") 
janela.title("Solicitaçao de Ferramentas") 
janela.resizable(0, 0)
'''-----------------------------------------------------------------------------------------------------------------'''

'''------------------------------------------------Caixa para digitar o nome do Tecnico-----------------------------'''
label_codigo_ferramenta = tk.Label(text="Técnico:")
label_codigo_ferramenta.grid(row=0, column=0, padx=10, pady=10)
entry_ferramenta = tk.Entry()
entry_ferramenta.grid(row=0, column=1, padx=5, pady=5)

'''------------------------------------------------Caixa para digitar a ferramenta----------------------------------'''
label_nome_ferramenta = tk.Label(text="Ferramenta:")
label_nome_ferramenta.grid(row=1, column=0, padx=5, pady=2)
ferramentas = ttk.Combobox(values=tabela)
ferramentas.grid(row=1, column=1, padx=5, pady=5)
'''-----------------------------------------------------------------------------------------------------------------'''

'''----------------------------------Caixa para selecionar a voltagem da ferramenta---------------------------------'''
label_selecionar_voltagem = tk.Label(text="Voltagem:")
label_selecionar_voltagem.grid(row=1, column=2, padx = 5, pady = 5)
selecionar_voltagem = ttk.Combobox(values=lista_voltagem)
selecionar_voltagem.grid(row=1, column=3, padx = 5, pady = 5)
'''-----------------------------------------------------------------------------------------------------------------'''

'''---------------------------------------Caixa para digitar a unidade de ferramentas-------------------------------'''
label_unidade = tk.Label(text="Unidade:")
label_unidade.grid(row=1, column=4, padx=5, pady=5, )
entry_ferramenta = tk.Entry()
entry_ferramenta.grid(row=1, column=5, padx=5, pady=5, )
'''------------------------------------------------------------------------------------------------------------------'''

'''-------------------------------------------Data de entrada e saida das ferramentas--------------------------------'''
label_data_saida = tk.Label(text="Data de saida:")
label_data_saida.grid(row=2, column=0, padx=10, pady=10, columnspan=1)
entry_data_saida = tk.Entry()
entry_data_saida.grid(row=2, column=1, padx=10, pady=10, columnspan=1)
label_data_entrada = tk.Label(text="Data de entrada:")
label_data_entrada.grid(row=2, column=2, padx=10, pady=10, columnspan=1)
entry_data_entrada = tk.Entry()
entry_data_entrada.grid(row=2, column=3, padx=10, pady=10, columnspan=1)
'''------------------------------------------------------------------------------------------------------------------'''

'''----------------------------------------------------Botao para cadastrar a solicitaçao------------------------------'''
botao_cadastrar_solicitacao = ttk.Button(janela, text="Cadastrar Solicitaçao")
botao_cadastrar_solicitacao.grid(row=4, column=2, sticky=tk.E, padx=5, pady=5)
'''---------------------------------------------------------------------------------------------------------------------'''



janela.mainloop()