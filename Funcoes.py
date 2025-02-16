from LinhaDeOnibus import LinhaDeOnibus
from datetime import datetime
from Onibus import Onibus
import pandas as pd

# Função que cadastra uma linha de ônibus
def cadastrar_linhas(listaDeLinhas, listaDeOnibus):
    # Loop até que um ID único seja informado
    while(True):
        cont = 0
        
        id = int(input('\nInforme o ID da linha: '))
        for linha in listaDeLinhas:
            if(linha.id == id):
                print('\nID já cadastrado previamente. Por favor, tente novamente.')
                cont += 1
        if(cont == 0):
            break

    # Captura cidade de origem e destino
    cidadeOrigem = str(input('Informe a cidade de origem: '))
    cidadeDestino = str(input('Agora, digite a cidade de destino: '))

    # Loop para validar o formato do horário
    while(True):
        # Solicita o horário de partida e garante que possua 5 caracteres
        horarioPartida = str(input('Informe o horário de partida [hh:mm]: '))[:5]
        
        # Divide o horário em horas e minutos
        horarioPartidaSplit = horarioPartida.split(':')
        horas = int(horarioPartidaSplit[0])
        minutos = int(horarioPartidaSplit[1])

        # Verifica se o horário é válido
        if(horas < 0 or horas > 23 or minutos < 0 or minutos > 59):
            print('\nHorário inválido. Por favor, tente novamente.\n')
        else:
            # Formata o horário para garantir que sempre tenha dois dígitos
            horario_formatado = f'{horas:02}:{minutos:02}'
            break

    # Loop para validar o valor da passagem
    while(True):
        # Solicita o valor da passagem ao usuário
        valorPassagem = input('Digite o valor da passagem(ex: 2,00): ')
        
        # Substitui a vírgula por ponto para conversão correta
        if ',' in valorPassagem:
            valorPassagem = valorPassagem.replace(',', '.')
        
        try:
            # Tenta converter o valor informado para float
            valorPassagem = float(valorPassagem)
            
            # Verifica se o valor é positivo
            if(valorPassagem <= 0):
                print('\nValor inválido. Por favor, tente novamente.\n')
            else:
                break
        except ValueError:
            # Trata o erro caso o valor informado não seja numérico
            print('\nValor inválido. Por favor, tente novamente.\n')

    # Verifica se a linha já existe
    for linha in listaDeLinhas:
        if(linha.cidadeOrigem == cidadeOrigem and linha.cidadeDestino == cidadeDestino and linha.horarioPartida == horario_formatado and linha.valorPassagem == valorPassagem):
            print('\nEssa linha já está cadastrada no sistema.')
            return   

    listaDeOnibusLinha = []       
    idOnibus = 1
    cont = 0
    # Loop para cadastrar ônibus
    while(idOnibus != 0 or cont == 0):
        # Loop para cadastrar os ônibus da linha
        # O loop continua até que o usuário digite 0
        idOnibus = int(input('Informe o ID do ônibus(digite 0 para parar): '))
        if(cont == 0 and idOnibus == 0):
            print('\nCadastre pelo menos 1 ônibus na linha. Por favor, tente novamente.\n')
            continue
        cont += 1
        # Verifica se o ID do ônibus já existe na lista de ônibus
        id_duplicado = any(onibus.idOnibus == idOnibus for onibus in listaDeOnibus)
        if(id_duplicado):
            print('\nID já cadastrado previamente. Por favor, tente novamente.\n')
            continue
        if(idOnibus == 0):
            break
        # Solicita a data de partida do ônibus
        data = str(input('Informe a data de partida [dd/mm/aaaa]: '))
        # Divide a data em dia, mês e ano
        dataSplit = data.split('/')
        dia = int(dataSplit[0])
        mes = int(dataSplit[1])
        ano = int(dataSplit[2])
        # Verifica se a data é válida
        agora = datetime.now()
        data = datetime(ano, mes, dia)
        if(data <= agora or mes < 1 or mes > 12 or dia < 1 or dia > 31 or (dia == 29 and mes == 2 and ano % 4 != 0)):
            print('\nData inválida. Por favor, tente novamente.\n')
            continue
        # Formata a data para o padrão dd/mm/aaaa
        data_formatada = f'{dia:02}/{mes:02}/{ano:04}'
        # Cria uma lista de assentos disponíveis
        listaDeAssentos = list(range(1, 21))
        # Tenta criar um objeto do tipo Onibus
        try:
            onibus = Onibus(idOnibus, data_formatada, listaDeAssentos)        
            # Adiciona o ônibus na lista de ônibus e na lista de ônibus da linha
            listaDeOnibus.append(onibus)
            listaDeOnibusLinha.append(onibus)

        except ValueError as e:
            print(f'\nErro: {e}\n')
                            
    try:
        # Tenta criar um objeto do tipo LinhaDeOnibus
        linha = LinhaDeOnibus(id, cidadeOrigem, cidadeDestino, horario_formatado, valorPassagem, *listaDeOnibusLinha)
        listaDeLinhas.append(linha) 
        print("\nLinha cadastrada com sucesso!")
        # time.sleep(1)
        # system('cls' if name == 'nt' else 'clear')
    except ValueError as e:
        print(f'\nErro: {e}\n')

# Função que remove uma linha da lista de linhas
def remover_linhas(listaDeLinhas):
    # Enquanto o usuário não digitar o id correto, o loop continua
    while(True):
        # Solicita o id da linha que o usuário deseja remover
        id = int(input('\nInforme o id da linha que deseja remover: '))
        # Variável que verifica se o id foi encontrado
        achou = False

        # Loop que percorre a lista de linhas
        for linha in listaDeLinhas:
            # Verifica se o id da linha é igual ao digitado pelo usuário
            if(linha.id == id):
                # Se for igual, marca a variável "achou" como True
                achou = True
                # Remove a linha da lista
                listaDeLinhas.remove(linha)
                # Informa que a linha foi removida com sucesso
                print(f'Linha {id} removida com sucesso!')
                # Sai do loop
                return

        # Se o id não foi encontrado, informa que a linha não existe
        if(achou == False):
            print('\nLinha inexistente. Por favor, tente novamente.')

# Função que edita uma linha da lista de linhas
def editar_linhas(listaDeLinhas, listaDeOnibus):
    cont = 0

    # Enquanto o usuário não digitar o id correto, o loop continua
    while(cont == 0):
        id = int(input('\nInforme o ID da linha que deseja editar: '))
        for linha in listaDeLinhas:
            if(linha.id == id):
                cont += 1
                # Mostra as opções de edição para o usuário
                for linha in listaDeLinhas:
                    if(linha.id == id):
                        print('''
                        (1) -> Editar cidade de origem
                        (2) -> Editar cidade de destino
                        (3) -> Editar horário de partida
                        (4) -> Editar valor da passagem
                        (5) -> Editar ônibus
                        ''')
                        # Solicita a opção do usuário
                        opc = int(input('    Digite a opção desejada: '))

                        # Verifica qual a opção escolhida e chama a lógica correspondente
                        match opc:
                            case 1:
                                # Enquanto o usuário não digitar a cidade de origem correta, o loop continua
                                while(True):
                                    cidadeOrigem = str(input('Informe a nova cidade de origem: '))
                                    # Verifica se a cidade de origem e destino são iguais
                                    if(cidadeOrigem == linha.cidadeDestino):
                                        print('\nCidade de origem e destino iguais. Por favor, tente novamente.\n')
                                    else:
                                        # Altera a cidade de origem da linha
                                        linha.cidadeOrigem = cidadeOrigem
                                        print('\nCidade de origem alterada com sucesso!')
                                        # Sai do loop
                                        break
                            case 2:
                                # Enquanto o usuário não digitar a cidade de destino correta, o loop continua
                                while(True):
                                    cidadeDestino = str(input('Informe a nova cidade de destino: '))
                                    # Verifica se a cidade de origem e destino são iguais
                                    if(cidadeDestino == linha.cidadeOrigem):
                                        print('\nCidade de origem e destino iguais. Por favor, tente novamente.\n')
                                    else:
                                        # Altera a cidade de destino da linha
                                        linha.cidadeDestino = cidadeDestino
                                        print('\nCidade de destino alterada com sucesso!')
                                        # Sai do loop
                                        break
                            case 3:
                                # Enquanto o usuário não digitar o horário de partida correto, o loop continua
                                while(True):
                                    horarioPartida = str(input('Informe o horário de partida [hh:mm]: '))[:5]
                                    # Divide o horário em horas e minutos
                                    horarioPartidaSplit = horarioPartida.split(':')
                                    horas = int(horarioPartidaSplit[0])
                                    minutos = int(horarioPartidaSplit[1])
                                    # Verifica se o horário é válido
                                    if(horas < 0 or horas > 23 or minutos < 0 or minutos > 59):
                                        print('\n Horário inválido. Por favor, tente novamente.\n')
                                    else:
                                        # Formata o horário para o padrão hh:mm
                                        horario_formatado = f'{horas:02}:{minutos:02}'
                                        # Altera o horário de partida da linha
                                        linha.horarioPartida = horario_formatado
                                        print('\nHorário alterado com sucesso!')
                                        # Sai do loop
                                        break
                            # Caso o usuário escolha alterar o valor da passagem
                            case 4:
                                # Enquanto o usuário não digitar um valor de passagem válido, o loop continua
                                while(True):
                                    # Solicita o valor da passagem ao usuário
                                    valorPassagem = float(input('Digite o novo valor da passagem(ex: 2.32): '))
                                    # Verifica se o valor é positivo
                                    if(valorPassagem > 0):
                                        # Altera o valor da passagem da linha
                                        linha.valorPassagem = valorPassagem
                                        print('\nValor da passagem alterado com sucesso!')
                                        # Sai do loop
                                        break
                                    else:
                                        print('\nValor inválido. Por favor, tente novamente.\n')
                            case 5:
                                # Variável para controlar o loop
                                para = 1
                                while(para != 0):
                                    # Solicita ao usuário o que deseja alterar
                                    opc = int(input('O que deseja alterar?(1 - Adicionar Ônibus, 2 - Remover ônibus, 3 - Editar ônibus) '))
                                    # Caso o usuário escolha adicionar um ônibus
                                    if(opc == 1):
                                        # Solicita o ID do ônibus a ser adicionado
                                        idOnibus = int(input('Digite o ID do ônibus a ser adicionado: '))
                                        # Verifica se o ID do ônibus já existe na lista de ônibus
                                        id_duplicado = any(onibus.idOnibus == idOnibus for onibus in listaDeOnibus)
                                        if(id_duplicado):
                                            # Se o ID for duplicado, informa ao usuário e sai do loop
                                            print('\nID já cadastrado previamente. Por favor, tente novamente.\n')
                                            continue
                                        # Solicita a data de partida do ônibus
                                        data = str(input('Informe a data de partida [dd/mm/aaaa]: '))
                                        # Divide a data em dia, mês e ano
                                        dataSplit = data.split('/')
                                        dia = int(dataSplit[0])
                                        mes = int(dataSplit[1])
                                        ano = int(dataSplit[2])
                                        # Verifica se a data é válida
                                        agora = datetime.now()
                                        data = datetime(ano, mes, dia)
                                        if(data <= agora or mes < 1 or mes > 12 or dia < 1 or dia > 31 or (dia == 29 and mes == 2 and ano % 4 != 0)):
                                            # Se a data for inválida, informa ao usuário e sai do loop
                                            print('\nData inválida. Por favor, tente novamente.\n')
                                            continue
                                        # Formata a data para o padrão dd/mm/aaaa
                                        data_formatada = f'{dia:02}/{mes:02}/{ano:04}'
                                        # Verifica se a data de partida do ônibus já existe na lista de ônibus da linha
                                        data_duplicada = any(onibus.dataPartida == data_formatada for onibus in linha.onibus)
                                        if(data_duplicada):
                                            # Se a data for duplicada, informa ao usuário e sai do loop
                                            print('\nJá existe um ônibus com a data informada nessa linha. Por favor, tente novamente.\n')
                                            continue
                                        try:
                                            # Cria um novo objeto Onibus com os dados informados e o adiciona na lista de ônibus da linha e na lista de ônibus global
                                            listaDeAssentos = list(range(1, 21))
                                            onibus = Onibus(idOnibus, data_formatada, listaDeAssentos)        
                                            listaDeOnibus.append(onibus)
                                            linha.onibus.append(onibus)
                                            print('\nÔnibus cadastrado com sucesso!')
                                            # Sai do loop
                                            para = 0
                                        except ValueError as e:
                                            # Se houver um erro ao criar o objeto Onibus, informa ao usuário
                                            print(f'\nErro: {e}\n')
                                    # Caso o usuário escolha remover um ônibus
                                    elif(opc == 2):
                                        # Solicita o ID do ônibus a ser removido
                                        idOnibus = int(input('Informe o ID do ônibus que deseja remover: '))
                                        # Verifica se o ônibus existe na lista de ônibus da linha
                                        for onibus in linha.onibus:
                                            if(onibus.idOnibus == idOnibus):
                                                # Remove o ônibus da lista de ônibus da linha e da lista de ônibus global
                                                linha.onibus.remove(onibus)
                                                listaDeOnibus.remove(onibus)
                                                print('\nÔnibus removido com sucesso!')
                                                # Sai do loop
                                                para = 0
                                                break
                                        else:
                                            # Se o ônibus não existir, informa ao usuário
                                            print('\nÔnibus inexistente. Por favor, tente novamente.\n')
                                    elif(opc == 3):
                                        cont = 0

                                        # Solicita o ID do ônibus a ser editado
                                        idOnibus = int(input('Informe o ID do ônibus que deseja editar: '))
                                        for onibus in linha.onibus:
                                            if(onibus.idOnibus == idOnibus):
                                                cont += 1
                                                while(True):
                                                    # Solicita a nova data de partida do ônibus
                                                    data = str(input('Informe a nova data de partida [dd/mm/aaaa]: '))
                                                    dataSplit = data.split('/')
                                                    dia = int(dataSplit[0])
                                                    mes = int(dataSplit[1])
                                                    ano = int(dataSplit[2])
                                                    
                                                    # Verifica se a data informada é válida
                                                    agora = datetime.now()
                                                    data = datetime(ano, mes, dia)
                                                    if(data <= agora or mes < 1 or mes > 12 or dia < 1 or dia > 31):
                                                        print('\nData inválida. Por favor, tente novamente.\n')
                                                        continue
                                                    
                                                    # Formata a data para o padrão dd/mm/aaaa
                                                    data_formatada = f'{dia:02}/{mes:02}/{ano:04}'
                                                    
                                                    # Verifica se a data de partida do ônibus já existe na lista de ônibus da linha
                                                    data_duplicada = any(onibus.dataPartida == data_formatada for onibus in linha.onibus)
                                                    if(data_duplicada):
                                                        print('\nJá existe um ônibus com a data informada nessa linha. Por favor, tente novamente.\n')
                                                        continue
                                                    
                                                    # Edita a data de partida do ônibus
                                                    onibus.dataPartida = data_formatada
                                                    print('\nData editado com sucesso!')
                                                    para = 0
                                                    break
                                        # Caso o ônibus não exista, imprime mensagem de erro
                                        if(cont == 0):
                                            print('\nÔnibus inexistente. Por favor, tente novamente.\n')
                                    else:
                                        # Caso o ônibus exista, mas a opção digitada seja inválida, imprime mensagem de erro
                                        print('\nOpção inválida. Por favor, tente novamente.\n')
                                        continue
                            case _:
                                # Caso a opção digitada seja inválida, imprime mensagem de erro
                                print('\nOpção inválida. Por favor, tente novamente.\n')
        # Caso a linha não exista, imprime mensagem de erro
        if(cont == 0):
            print('\nLinha inexistente. Por favor, tente novamente.')

def horarios_cidade(listaDeLinhas):
    # Essa função imprime todos os horários de partida de ônibus para uma cidade de destino
    cidadeDestino = str(input('\nInforme a cidade de destino: '))

    # Contador de linhas com destino à cidade informada
    cont = 0
    # Posição da viagem que será impressa
    posicao = 1
    print(f'\nViagens para {cidadeDestino}:\n')
    
    # Percorre todas as linhas de ônibus
    for linha in listaDeLinhas:
        # Verifica se a linha tem como destino a cidade informada
        if(linha.cidadeDestino == cidadeDestino):
            cont += 1
            print(f'Horário de partida: {linha.horarioPartida} | Cidade de origem: {linha.cidadeOrigem} | Valor da passagem: R$ {linha.valorPassagem:.2f}\n') 
            # Percorre todos os ônibus da linha
            for onibus in linha.onibus:
                print(f'- - - - - {posicao}° viagem - - - - -\n')
                posicao += 1
                # Imprime informações do ônibus
                print(f'ID do ônibus: {onibus.idOnibus} | Assentos disponíveis: {len(onibus.assentosDisponiveis)} | Data de partida: {onibus.dataPartida}\n')
    # Caso não existam linhas com destino à cidade informada, imprime mensagem de erro
    if(cont == 0):
        print(f'\nNão existem linhas com destino para {cidadeDestino} cadastradas no sistema.\n')
    
def ver_assentos(listaDeLinhas, total):
    idOnibus = int(input('\nDigite o ID do ônibus que deseja consultar: '))  # Solicita o ID do ônibus ao usuário

    cont = 0  # Inicializa o contador de ônibus encontrados

    for linha in listaDeLinhas:
        for onibus in linha.onibus:
            if(idOnibus == onibus.idOnibus):  # Verifica se o ID do ônibus corresponde
                cont += 1
                agora = datetime.now()  # Obtém a data e hora atuais
                dataPartida = datetime.strptime(onibus.dataPartida, '%d/%m/%Y')  # Converte a data de partida do ônibus para objeto datetime
                diferenca = dataPartida - agora  # Calcula a diferença de dias entre a data atual e a data de partida
                if(diferenca.days < 30):  # Verifica se a diferença é inferior a 30 dias
                    cont += 1
                    print(f'\nLinha: {linha.cidadeOrigem} -> {linha.cidadeDestino} | Horário de partida: {linha.horarioPartida} | Valor da passagem: R$ {linha.valorPassagem:.2f}\n')
                    print(f'ID do ônibus: {onibus.idOnibus} | Assentos disponíveis: {len(onibus.assentosDisponiveis)} | Data de partida: {onibus.dataPartida}\n')
                    if(len(onibus.assentosDisponiveis) > 0):  # Verifica se há assentos disponíveis
                        while(True):
                            opc = int(input('Deseja comprar algum assento?(1 - Sim e 2 - Não): '))  # Pergunta se o usuário deseja comprar um assento
                            if(opc == 1):
                                while(True):
                                    print(f'\nEsses são os assentos disponíveis: {onibus.assentosDisponiveis} (ímpares: assentos na janela e pares: assentos no corredor)')
                                    assento = int(input('Informe o assento que deseja comprar: '))  # Solicita o assento desejado
                                    if(assento in onibus.assentosDisponiveis):  # Verifica se o assento está disponível
                                        onibus.assentosDisponiveis.remove(assento)  # Remove o assento da lista de disponíveis
                                        total[0] += linha.valorPassagem  # Atualiza o total arrecadado
                                        print('\nAssento comprado com sucesso!')
                                        return
                                    else:
                                        print('\nAssento indisponível. Por favor, tente novamente.\n')
                            elif(opc == 2):
                                return  # Sai da função se não quiser comprar
                            else:
                                print('\nOpção inválida. Por favor, tente novamente.')
                                continue
    if(cont == 0):
        print('\nÔnibus inexistente.\n')  # Informa se o ônibus não foi encontrado
    elif(cont == 1):
        print('\nEsse ônibus não está disponível no intervalo de menos de 1 mês.\n')  # Informa se o ônibus não está disponível

def total_arrecadado_mensal(total):
    # Essa função imprime o total arrecadado no mês
    print(f'\nO total arrecadado no mês {datetime.now().month} foi de R$ {total[0]:.2f}')
    
def processar_reservas(listaDeLinhas, total):
    # Essa função processa as reservas de um arquivo e adiciona as válidas na lista de linhas de ônibus
    
    nome_arquivo = input("\nInforme o nome do arquivo: ")

    # Listas para armazenar as reservas válidas e inválidas
    reservasValidas = []
    reservasInvalidas = []

    try:
        # Abre o arquivo em modo de leitura
        with open(nome_arquivo + ".txt", "r", encoding="utf-8") as f:
            # Lê todas as linhas do arquivo
            linhas = f.readlines()
    except FileNotFoundError:
        # Imprime mensagem de erro se o arquivo não for encontrado
        print(f"Erro: Arquivo {nome_arquivo} não encontrado.")
        return

    # Percorre todas as linhas do arquivo
    for linha in linhas:
        # Separa as informações da reserva em variáveis
        cidade, horario_reserva, data_reserva, assento = linha.strip().split(", ")
        assento = int(assento)

        # Encontra a linha de ônibus correspondente
        linha_onibus = next((l for l in listaDeLinhas if l.cidadeDestino == cidade), None)

        # Verifica se a linha de ônibus existe
        if not linha_onibus:
            # Se a linha não existir, adiciona a reserva como inválida
            reservasInvalidas.append((cidade, horario_reserva, data_reserva, assento, "Linha não encontrada"))
            continue

        # Converte a reserva para datetime
        try:
            data_hora_reserva = datetime.strptime(f"{data_reserva} {horario_reserva}", "%d/%m/%Y %H:%M")
        except ValueError:
            reservasInvalidas.append((cidade, horario_reserva, data_reserva, assento, "Formato de data/horário inválido"))
            continue

        # Busca um ônibus disponível na linha que tenha uma data e horário válidos
        onibus_valido = None
        for onibus in linha_onibus.onibus:
            try:
                data_hora_partida = datetime.strptime(f"{onibus.dataPartida} {linha_onibus.horarioPartida}", "%d/%m/%Y %H:%M")
            except ValueError:
                continue  # Pula ônibus com data inválida

            if data_hora_reserva == data_hora_partida:
                onibus_valido = onibus
                break  # Pega o primeiro ônibus válido

        # Se não encontrar um ônibus com data e horário válidos, significa que o ônibus já partiu, então adiciona a reserva como inválida com a razão "Ônibus já partiu"
        if not onibus_valido:
            reservasInvalidas.append((cidade, horario_reserva, data_reserva, assento, "Ônibus já partiu"))
            continue

        # Verifica se o ônibus tem assentos disponíveis
        if onibus_valido.assentosDisponiveis == 0:
            reservasInvalidas.append((cidade, horario_reserva, data_reserva, assento, "Ônibus cheio"))
            continue

        # Verifica se o assento já está ocupado
        if assento not in onibus_valido.assentosDisponiveis:
            reservasInvalidas.append((cidade, horario_reserva, data_reserva, assento, "Assento ocupado"))
            continue

        reservasValidas.append((cidade, onibus_valido.idOnibus, data_reserva, assento))
        onibus_valido.assentosDisponiveis.remove(assento)
        total[0] += linha_onibus.valorPassagem

    # Salvar reservas inválidas em um arquivo
    with open("reservas_invalidas.txt", "w", encoding="utf-8") as f:
        for reserva in reservasInvalidas:
            f.write(", ".join(map(str, reserva)) + "\n")

def calcular_ocupacao_total(listaDeLinhas):
    matriz_ocupacao = []
    ids_linhas = []
    
    # Percorre cada linha de ônibus
    for linha in listaDeLinhas:
        ocupacao_media = linha.calcular_ocupacao_media()  # Lista com ocupações por dia da semana
        matriz_ocupacao.append(ocupacao_media)
        ids_linhas.append(linha.id)  # Supondo que cada linha tem um atributo "id"
    
    # Cria o DataFrame com colunas nomeadas
    dias_da_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
    df_ocupacao = pd.DataFrame(matriz_ocupacao, columns=dias_da_semana)
    
    # Adiciona o ID da linha como uma coluna
    df_ocupacao.insert(0, "ID Linha", ids_linhas)
    
    print("DataFrame de Ocupação Total:")
    print(df_ocupacao.to_string(index=False))
