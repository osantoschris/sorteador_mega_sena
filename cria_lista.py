from openpyxl import load_workbook

planilha = load_workbook('C:\\Gerador Mega Sena\\bases\\numeros_atributos.xlsx')
aba = planilha.active

impares = []
pares = []

def criar_lista():
    for celula in aba['B']:
        if celula.value != 'Atributo':
            linha = celula.row
            valor = aba[f'A{str(linha)}'].value
            atributo = aba[f'B{str(linha)}'].value
            if atributo == 'Par':
                pares.append(valor)
            if atributo == 'Ímpar':
                impares.append(valor)

def limpar_lista():
    impares.clear()
    pares.clear()