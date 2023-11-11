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
            TempoMaximoDeReserva TIME 
        )
        '''
    )

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS Tecnicos (
            idTecnicos INTEGER PRIMARY KEY,
            Tecnicos TEXT,
            CPF INTEGER,
            Turno TEXT,
            Radio INTEGER, 
            Equipe TEXT
        )
        '''
    )

    fechar_BD(BD)

# Chamada para criar tabelas 
criar_tabelas()