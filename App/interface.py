from turtle import bgcolor
from webbrowser import BackgroundBrowser
from numpy import imag
import pandas as pd
from tkinter import Canvas, PhotoImage, ttk
import tkinter as tk
import datetime as dt
import os
import tkinter.messagebox as msg
from PIL import ImageTk, Image
import sqlite3
from DB.banco_dados import abrir_BD, fechar_BD, carregar_lista
from DB.funcao_banco import carrega_lista 




'''---INTERFACE CADASTRO DO TECNICO--------'''
def janela_cadastro_tecnicos():
    janela_cadastro = tk.Toplevel()
    janela_cadastro.geometry("800x400")
    janela_cadastro.title("Cadastrar Técnico")
    janela_cadastro.configure(background="#00BFB2")
    
    def novo_tecnico():
        '''Funçao para cadastrar Tecnico no banco de dados'''
        global lista_tecnicos
        BD = abrir_BD()
        cursor = BD.cursor()

        '''Codigo para iserir dados no banco'''
        cursor.execute('INSERT INTO Tecnicos (Nome, CPF, Turno, Radio, Equipe) VALUES (?, ?, ?, ?, ?)',
                       (entrar_nome.get(), entrar_cpf.get(), entrar_turno.get(), entrar_radio.get(), entrar_equipe.get()))

        

        fechar_BD(BD)
        lista_tecnicos = carrega_lista('Tecnicos')
        janela_cadastro.destroy()
        msg.showinfo('Cadastro de Tecnicos', 'Tecnico Cadastrado!')
    
       

    '''---------------------Cadastro do Tecnico--------------'''
    label_nome = tk.Label(janela_cadastro, text='Nome do Técnico:', background="#00BFB2")
    label_nome.grid(row=0, column=0, padx=0, pady=0, columnspan=1)
    entrar_nome = tk.Entry(janela_cadastro)
    entrar_nome.grid(row=0, column=1, padx=0, pady=0, columnspan=1)

    '''-------------------cadastro do cpf----------------------'''
    label_cpf = tk.Label(janela_cadastro, text='CPF:', background="#00BFB2")
    label_cpf.grid(row=2, column=0, padx=0, pady=0, columnspan=1)
    entrar_cpf = tk.Entry(janela_cadastro)
    entrar_cpf.grid(row=2, column=1, padx=0, pady=0, columnspan=1)

    '''-----------------Numero do Radio--------------------'''
    label_radio = tk.Label(janela_cadastro, text='Nª RADIO:', background="#00BFB2")
    label_radio.grid(row=3, column=0, padx=0, pady=0, columnspan=1)
    entrar_radio = tk.Entry(janela_cadastro)
    entrar_radio.grid(row=3, column=1, padx=0, pady=0, columnspan=1)

    '''---------------------Turno do Tecnico cadastrado----'''
    label_turno = tk.Label(janela_cadastro, text='Turno', background="#00BFB2")
    label_turno.grid(row=4, column=0, padx=0, pady=0, columnspan=1)
    entrar_turno = ttk.Combobox(janela_cadastro, values=lista_turnos)
    entrar_turno.grid(row=4, column=1, padx=0, pady=0, columnspan=1)

    '''------------------------Equipe de trabalho--------------------'''
    label_nome_equipe = tk.Label(janela_cadastro, text='Nome da Equipe:', background="#00BFB2")
    label_nome_equipe.grid(row=5, column=0, padx=0, pady=0, columnspan=1)
    entrar_equipe = tk.Entry(janela_cadastro)
    entrar_equipe.grid(row=5, column=1, padx=0, pady=0, columnspan=1)

    botao_cadastrar_tecnico = tk.Button(janela_cadastro, text='Cadastrar', command=novo_tecnico)
    botao_cadastrar_tecnico.grid(row=6, column=3, padx=0, pady=0, columnspan=1)

'''---INTERFACE PARA CADASTRO DE FERRAMENTAS--'''
def interface_cadastro_ferramentas():
    janela_cadastro_ferramentas = tk.Toplevel()
    janela_cadastro_ferramentas.geometry("800x400")
    janela_cadastro_ferramentas.title("Cadastrar Ferramenta")
    janela_cadastro_ferramentas.configure(background="#00BFB2")

    def nova_ferramenta():
        '''Funçao que vai adicionar nova ferramenta'''
        global lista_ferramentas
        BD = abrir_BD()
        cursor = BD.cursor()

        '''Codigo para iserir dados nno banco'''
        cursor.execute( 'INSERT INTO Ferramentas (id, DescricaoFerramenta, Fabricante, Voltagem, Tamanho, UnidadeDeMedida, TipoDeFerramenta, MaterialDaFerramenta, TempoMaximoDeReserva)VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)',
                                                 (entrar_id.get(), entrar_descricaoferramenta.get(), entrar_fabricante.get(), entrar_voltagem.get(), entrar_tamanho.get(), entrar_unidadeDeMedida.get(), entrar_tipoDeFerramenta.get(), entrar_materialDaFerramenta.get(), entrar_tempoMaximoDeReserva.get() ))                                                                                                                                             
                                                                                                                                                                                              
       
        fechar_BD(BD)
        lista_ferramentas = carrega_lista('Descriçao Ferramenta')
        janela_cadastro_ferramentas.destroy()
        msg.showinfo('Cadastrar', 'Ferramenta Cadastrada!')

    '''----------------------------------------ID  da ferramenta---------------------------------------'''
    label_id_ferramenta = tk.Label(janela_cadastro_ferramentas, text="ID: ", background="#00BFB2")
    label_id_ferramenta.grid(row=1, column=0, padx=0, pady=0, columnspan=1)
    entry_id_ferramenta = tk.Entry(janela_cadastro_ferramentas)
    entry_id_ferramenta.grid(row=1, column=1, padx=0, pady=0, columnspan=1)
    
    '''----------------------------------------Descriçao  da ferramenta---------------------------------'''
    label_nome_ferramenta = tk.Label(janela_cadastro_ferramentas, text="Descrição da ferramenta: ", background="#00BFB2")
    label_nome_ferramenta.grid(row=2, column=0, padx=0, pady=0, columnspan=1)
    entry_nome_ferramenta = tk.Entry(janela_cadastro_ferramentas)
    entry_nome_ferramenta.grid(row=2, column=1, padx=0, pady=0, columnspan=1)
    
    '''--------------------------------------Fabricante-------------------------------------------------'''
    label_fabricante = tk.Label(janela_cadastro_ferramentas, text="Fabricante: ", background="#00BFB2")
    label_fabricante.grid(row=3, column=0, padx=0, pady=0, columnspan=1)
    entry_fabricante = tk.Entry(janela_cadastro_ferramentas)
    entry_fabricante.grid(row=3, column=1, padx=0, pady=0, columnspan=1)

    '''--------------------------------------Voltagem de Uso---------------------------------------------'''
    label_voltagem_uso = tk.Label(janela_cadastro_ferramentas, text="Voltagem de Uso: ", background="#00BFB2")
    label_voltagem_uso.grid(row=4, column=0, padx=0, pady=0, columnspan=1)
    entry_voltagem_uso = ttk.Combobox(janela_cadastro_ferramentas, values=lista_voltagem)
    entry_voltagem_uso.grid(row=4, column=1, padx=0, pady=0, columnspan=1)
    
    '''--------------------------------------Tamanho-----------------------------------------------------'''
    label_tamanho = tk.Label(janela_cadastro_ferramentas, text="Tamanho: ", background="#00BFB2")
    label_tamanho.grid(row=5, column=0, padx=0, pady=0, columnspan=1)
    entry_tamanho = tk.Entry(janela_cadastro_ferramentas)
    entry_tamanho.grid(row=5, column=1, padx=0, pady=0, columnspan=1)

    '''--------------------------------------Unidade de Medida--------------------------------------------'''
    label_unidade_medida = tk.Label(janela_cadastro_ferramentas, text="Unidade de Medida: ", background="#00BFB2")
    label_unidade_medida.grid(row=6, column=0, padx=0, pady=0, columnspan=1)
    entry_unidade_medida = ttk.Combobox(janela_cadastro_ferramentas, values=lista_unidade_medidas)
    entry_unidade_medida.grid(row=6, column=1, padx=0, pady=0, columnspan=1)

    '''--------------------------------------Tipo de Ferramenta--------------------------------------------'''
    label_tipo_ferramenta = tk.Label(janela_cadastro_ferramentas, text="Tipo de Ferramenta: ", background="#00BFB2")
    label_tipo_ferramenta.grid(row=7, column=0, padx=0, pady=0, columnspan=1)
    entry_tipo_ferramenta = ttk.Combobox(janela_cadastro_ferramentas, values=lista_tipo_ferramenta)
    entry_tipo_ferramenta.grid(row=7, column=1, padx=0, pady=0, columnspan=1)

    '''--------------------------------------Material da Ferramenta-----------------------------------------'''
    label_material_ferramenta = tk.Label(janela_cadastro_ferramentas, text="Material da Ferramenta: ", background="#00BFB2")
    label_material_ferramenta.grid(row=8, column=0, padx=0, pady=0, columnspan=1)
    entry_material_ferramenta = ttk.Combobox(janela_cadastro_ferramentas, values=lista_material_ferramenta)
    entry_material_ferramenta.grid(row=8, column=1, padx=0, pady=0, columnspan=1)

    '''--------------------------------------Tempo de uso-----------------------------------------------------'''
    label_tempo_uso = tk.Label(janela_cadastro_ferramentas, text="Tempo de Uso: ", background="#00BFB2")
    label_tempo_uso.grid(row=9, column=0, padx=0, pady=0, columnspan=1)
    entry_tempo_uso = tk.Entry(janela_cadastro_ferramentas)
    entry_tempo_uso.grid(row=9, column=1, padx=0, pady=0, columnspan=1)

    botao_cadastrar_ferramenta = tk.Button(janela_cadastro_ferramentas, text='Cadastrar', command=nova_ferramenta)
    botao_cadastrar_ferramenta.grid(row=10, column=2, padx=0, pady=0, columnspan=1)

'''--INTERFACE PARA FAZER SOLICITAÇAO DAS FERRAMENTAS--'''
def janela_solicitacoes():
    '''Janela da Interface para Solicitar Ferramenta'''
    
    janela = tk.Toplevel()
    janela.geometry("800x400")
    janela.title("Solicitaçao de Ferramentas")
    janela.configure(background= "#00BFB2")
    
    

    
    def nova_solicitacao():
        '''-Funçao que solicita ao banco de dados , a ferramenta cadastrada-'''
        global lista_ferramentas
        BD = abrir_BD()
        cursor = BD.cursor()

        '''Codigo para iserir dados nno banco'''
        cursor.execute('INSERT INTO SolicitarFerramentas (Nome, Ferramenta, Voltagem, Unidade, DataSaida, DataEntrada) VALUES (?, ?, ?, ?, ?, ?)',
                (entry_tecnico.get(), ferramentas.get(), selecionar_voltagem.get(), entry_unidade.get(), entry_data_saida.get(), entry_data_entrada.get()))


        fechar_BD(BD)
        lista_ferramentas = carrega_lista('Ferramentas')
        janela.destroy()
        msg.showinfo('Solicitar', 'Solicitacao Concluida!')

    
      

    label_nome_tecnico = tk.Label(janela, background="#00BFB2", text="Técnico:")
    label_nome_tecnico.grid(row=0, column=0, padx=10, pady=10)
    entry_tecnico = ttk.Combobox(janela, values=lista_tecnicos)
    entry_tecnico.grid(row=0, column=1, padx=0, pady=0)

    '''-----------Caixa para digitar a ferramenta-------------'''
    label_nome_ferramenta = tk.Label(janela, text="Ferramenta:", background="#00BFB2")
    label_nome_ferramenta.grid(row=1, column=0, padx=5, pady=2)
    ferramentas = ttk.Combobox(janela, values=lista_ferramentas)
    ferramentas.grid(row=1, column=1, padx=5, pady=5)

    '''----------Caixa para selecionar a voltagem da ferramenta-----------'''
    label_selecionar_voltagem = tk.Label(janela, text="Voltagem de Trabalho:", background="#00BFB2")
    label_selecionar_voltagem.grid(row=1, column=2, padx=5, pady=5)
    selecionar_voltagem = ttk.Combobox(janela, values=lista_voltagem)
    selecionar_voltagem.grid(row=1, column=3, padx=5, pady=5)

    '''------Caixa para digitar a unidade de ferramentas--------------'''
    label_unidade = tk.Label(janela, text="Unidade:", background="#00BFB2")
    label_unidade.grid(row=1, column=4, padx=5, pady=5, )
    entry_unidade = tk.Entry(janela)
    entry_unidade.grid(row=1, column=5, padx=5, pady=5, )
   
    '''------------Data de entrada e saida das ferramentas----------------------'''
    label_data_saida = tk.Label(janela, text="Data de saida:", background="#00BFB2")
    label_data_saida.grid(row=2, column=0, padx=10, pady=10, columnspan=1)
    entry_data_saida = tk.Entry(janela)
    entry_data_saida.grid(row=2, column=1, padx=10, pady=10, columnspan=1)
    label_data_entrada = tk.Label(janela, text="Data de entrada:", background="#00BFB2")
    label_data_entrada.grid(row=2, column=2, padx=10, pady=10, columnspan=1)
    entry_data_entrada = tk.Entry(janela)
    entry_data_entrada.grid(row=2, column=3, padx=10, pady=10, columnspan=1)
    
    '''--------------------------------------Botao para cadastrar a solicitaçao---------------------------'''
    botao_cadastrar_solicitacao = ttk.Button(janela, text="Cadastrar Solicitaçao", command=nova_solicitacao)
    botao_cadastrar_solicitacao.grid(row=4, column=1, sticky=tk.E, padx=5, pady=5)


'''---------------------------------------------------------INTERFACE PRINCIPAL DO SISTEMA-----------------------------------------------'''
aplication = tk.Tk()

aplication.title("DBV Softwares & Sistemas")
aplication.configure(background="grey")
aplication.geometry("800x600")
background = PhotoImage(file=r'App\imagens\projeto-desktop.png')
canvas1 = Canvas(aplication)


canvas1.pack(fill="both", expand=True)
canvas1.create_image(0, 0, image=background, anchor="nw")

'''----------------------------Boatao solicitar Ferramentas----------------------'''
imagem_solicitar_ferramenta = tk.PhotoImage(file=r'App\imagens\Solicitar ferramenta.png')
botao1 = ttk.Button( aplication,image=imagem_solicitar_ferramenta, command=janela_solicitacoes) 
botao1_canvas = canvas1.create_window(100, 10, anchor= "nw", window= botao1)

'''----------------------------Botao Cadastro Tecnico----------------'''
imagem_cadastro_tecnico = tk.PhotoImage(file=r'App\imagens\tecnico.png')
botao2 = ttk.Button( aplication, image=imagem_cadastro_tecnico, command= janela_cadastro_tecnicos) 
botaoe_canvas = canvas1.create_window(100, 90, anchor= "nw", window= botao2)

'''---------------------------Botao Cadastro Ferramentas-------------------------------'''
imagem_cadastro_ferramenta = tk.PhotoImage(file=r'App\imagens\cadastrar ferramenta.png')
botao3 = ttk.Button( aplication, image=imagem_cadastro_ferramenta, command=interface_cadastro_ferramentas) 
botaoe_canvas = canvas1.create_window(100, 170, anchor= "nw", window= botao3)



aplication.mainloop()













