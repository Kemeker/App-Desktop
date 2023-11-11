import sqlite3

_caminho = r'App\DB\banco_dados.db'

def abrir_BD() -> sqlite3.Connection:
    '''Retorna em uma variável o banco de dados aberto.'''
    BD = sqlite3.connect(_caminho)
    return BD

def fechar_BD(BD: sqlite3.Connection):
    '''Fecha o banco de dados e salva'''
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
            lista.append(row[0])  # Supondo que queremos apenas o primeiro valor da linha
    finally:
        fechar_BD(BD)
    return lista

# ... (outras funções necessárias)

def criar_tabelas():
    BD = abrir_BD()
    cursor = BD.cursor()

    cursor.execute( 
        '''
        CREATE TABLE IF NOT EXISTS Ferramentas (
            idFerramenta INTEGER PRIMARY KEY,
            id INTEGER,
            DescricaoFerramenta TEXT,
            Fabricante TEXT,
            Voltagem TEXT,
            Tamanho TEXT,
            UnidadeDeMedida TEXT,
            TipoDeFerramenta TEXT,
            MaterialDaFerramenta TEXT,
            TempoMaximoDeReserva INTEGER 
        )
        '''
    )

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS Tecnicos (
            idTecnicos INTEGER PRIMARY KEY,
            Tecnico TEXT,
            CPF INTEGER,
            Turno TEXT,
            Radio INTEGER, 
            Equipe TEXT
        )
        '''
    )

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS SolicitarFerramentas (
            idSolicitacoes INTEGER PRIMARY KEY AUTOINCREMENT,
            Nome TEXT,
            Ferramenta TEXT,
            Voltagem TEXT,
            Unidade TEXT,
            DataSaida TEXT,
            DataEntrada TEXT
        )
        '''
    )

    fechar_BD(BD)

# Chamada para criar tabelas 
criar_tabelas()
