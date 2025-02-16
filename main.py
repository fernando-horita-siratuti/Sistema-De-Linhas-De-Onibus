from os import name 
from sys import exit 
from LinhaDeOnibus import LinhaDeOnibus 
from Onibus import Onibus 
import Funcoes 

listaDeLinhas = [] # lista de linhas de ônibus
listaDeOnibus = [] # lista de ônibus
total = [0] # variável para armazenar o total arrecadado

# Inicializa a variável de controle do menu
opc = 0

# linha1 = LinhaDeOnibus(1, "São Paulo", "Rio de Janeiro", "12:00", "100.00", 
# Onibus(1, "16/02/2025", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),
# Onibus(2, "17/02/2025", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),
# Onibus(3, "18/02/2025", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),
# Onibus(4, "19/02/2025", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),
# Onibus(5, "20/02/2025", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),
# Onibus(6, "21/02/2025", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),
# Onibus(7, "22/02/2025", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
# linha2 = LinhaDeOnibus(2, "São Jose dos Campos", "Sorocaba", "17:00", "70.00", Onibus(2, "24/02/2025", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
# listaDeLinhas.append(linha1)
# listaDeLinhas.append(linha2)

# Enquanto a opção for diferente de 9, o programa permanece em loop
while(opc != 9):
    # Mostra o menu
    print('''
    Menu:

    (1) -> Cadastro de linhas
    (2) -> Remover linhas
    (3) -> Editar Linhas
    (4) -> Consultar todos horários para determinada cidade
    (5) -> Consultar os assentos disponíveis em determinado ônibus
    (6) -> Consultar total arrecadado no mês atual
    (7) -> Ler reservas de um arquivo
    (8) -> Mostrar ocupação diária
    (9) -> Sair   
    ''')

    # Verifica se a opção escolhida é válida
    while True:
        try:
            opc = int(input('    Digite a opção desejada: '))
            break
        except ValueError:
            print('\nOpção inválida. Por favor, tente novamente.\n')

    # Verifica qual a opção escolhida e chama a função correspondente
    match opc:
        case 1: 
            Funcoes.cadastrar_linhas(listaDeLinhas, listaDeOnibus)
        case 2:
            if(len(listaDeLinhas) > 0):
                Funcoes.remover_linhas(listaDeLinhas)
            else:
                print('\nNenhuma linha cadastrada. Por favor, tente novamente.')
        case 3:
            if(len(listaDeLinhas) > 0):
                Funcoes.editar_linhas(listaDeLinhas, listaDeOnibus)
            else:
                print('\nNenhuma linha cadastrada. Por favor, tente novamente.')
        case 4:
            if(len(listaDeLinhas) > 0):
                Funcoes.horarios_cidade(listaDeLinhas)
            else:
                print('\nNenhuma linha cadastrada. Por favor, tente novamente.')
        case 5:
            if(len(listaDeLinhas) > 0):
                Funcoes.ver_assentos(listaDeLinhas, total)
            else:
                print('\nNenhuma linha cadastrada. Por favor, tente novamente.')
        case 6:
            if(total[0] > 0):
                Funcoes.total_arrecadado_mensal(total)
            else:
                print('\nNada arrecadado no mês ainda.')
        case 7:
            if(len(listaDeLinhas) > 0):
                Funcoes.processar_reservas(listaDeLinhas, total)
            else:
                print('\nNenhuma linha cadastrada. Por favor, tente novamente.')
        case 8:
            if(len(listaDeLinhas) > 0):
                Funcoes.calcular_ocupacao_total(listaDeLinhas)
            else:
                print('\nNenhuma linha cadastrada. Por favor, tente novamente.')
        case 9:
            exit()
        case _:
            print('\nOpção inválida. Por favor, tente novamente.')                  