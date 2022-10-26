import openpyxl

_caminho = r'App\banco_dados.xlsx'
def abrir_BD()-> openpyxl.Workbook:
    '''Retorna em uma variavel o banco de dados aberto.'''
    BD = openpyxl.load_workbook(_caminho)
    return BD
def fechar_BD(BD: openpyxl.Workbook):
    BD.save(_caminho)
    BD.close()
def carrega_lista(Ferramentas: str) -> list:
    BD = abrir_BD()
    pergunta = False
    lista = []
    for col in range(1,1000,1):
        if pergunta == True:
            break
        if BD.active.cell(row=1,column=col).value == Ferramentas:
            for lin in range(2,1_000_000,1):
                if BD.active.cell(row=lin,column=col).value != None:
                    lista.append(BD.active.cell(row=lin,column=col).value)
                else:
                    pergunta = True
                    break
    fechar_BD(BD)
    return lista
def carregar_tabela(Tecnicos: str) -> list:
    '''encontra a primeira coluna e extrai a tabela inteira'''
    BD = abrir_BD()
    pergunta = False
    tabela = []
    for colI in range(1, 1000, 1):
        if pergunta == True:
            break
        if BD.active.cell(row=1, column=colI).value == Tecnicos:
            for lin in range(2,1000,1):
                if BD.active.cell(row=lin, column=colI).value == None:
                    pergunta = True
                    break
                lista= []
                for col in range(colI,1000,1):
                    if BD.active.cell(row=lin, column=col).value != None:
                        lista.append(BD.active.cell(row=lin, column=col).value)
                    else:
                        break
                tabela.append(lista)
    fechar_BD(BD)
    return tabela





'''-----------------------Funçao Chekar CPF----------------------------------'''
"""
while True:
    cpf = input('Digite um CPF: ')
    novo_cpf = cpf[:-2]                 # Elimina os dois últimos digitos do CPF
    reverso = 10                        # Contador reverso
    total = 0

    # Loop do CPF
    for index in range(19):
        if index > 8:                   # Primeiro índice vai de 0 a 9,
            index -= 9                  # São os 9 primeiros digitos do CPF

        total += int(novo_cpf[index]) * reverso  # Valor total da multiplicação

        reverso -= 1                    # Decrementa o contador reverso
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:                   # Se o digito for > que 9 o valor é 0
                d = 0
            total = 0                   # Zera o total
            novo_cpf += str(d)          # Concatena o digito gerado no novo cpf

    # Evita sequencias. Ex.: 11111111111, 00000000000...
    sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)

    # Checagem de cpf válido ou não
    if cpf == novo_cpf and not sequencia:
        print('Válido')
    else:
        print('Inválido')
"""