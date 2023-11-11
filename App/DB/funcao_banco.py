import sqlite3

_caminho = r'DB\banco_dados.db'

def abrir_BD()-> sqlite3.Connection:
    '''Retorna em uma variavel o banco de dados aberto.'''
    BD = sqlite3.connect(_caminho)
    return BD

def fechar_BD(BD: sqlite3.Connection):
    '''Fecha o baco de dados e salva'''
    BD.commit()
    BD.close()

def carrega_lista(Ferramentas: str) -> list:
    BD = abrir_BD()
    cursor = BD.cursor()
    
    lista = []
    try:
        cursor.execute(f'SELECT * FROM {Ferramentas}')
        rows = cursor.fetchall()
        for row in rows:
            lista.append(row[0]) # supodo que queremos so o primeiro valor da linha
    finally:
        fechar_BD(BD)
    return lista            
    
def carregar_tabela(Tecnicos: str) -> list:
    BD = abrir_BD()
    cursor = BD.cursor()

    tabela = []
    try:
        cursor.execute(f'SELECT * FROM {Tecnicos}')
        rows = cursor.fetchall()
        for row in rows:
            tabela.append(list(row))
    finally:
        fechar_BD(BD)
    return tabela        




