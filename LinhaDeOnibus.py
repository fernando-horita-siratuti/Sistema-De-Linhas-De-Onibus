from datetime import datetime

class LinhaDeOnibus:
    def __init__(self, id, cidadeOrigem, cidadeDestino, horarioPartida, valorPassagem, *onibus):
        # Cria uma linha de ônibus com os dados fornecidos
        # e uma lista de ônibus que a compõem
        self.id = id
        self.cidadeOrigem = cidadeOrigem
        self.cidadeDestino = cidadeDestino
        self.horarioPartida = horarioPartida
        self.valorPassagem = float(valorPassagem)
        self.onibus = list(onibus)
    
    def calcular_ocupacao_media(self):
        # Calcula a ocupação média diária de uma linha de ônibus
        ocupacao_diaria = {i: [] for i in range(7)}  
        
        # Itera sobre os ônibus da linha e separa a ocupação em dias da semana (0 = segunda, 1 = ter ça, ..., 6 = domingo)
        for onibus in self.onibus:
            dia_da_semana = datetime.strptime(onibus.dataPartida, '%d/%m/%Y').weekday()
            ocupacao_diaria[dia_da_semana].append(onibus.calcular_ocupacao())
        
        # Calcula a ocupação média para cada dia da semana (None se n o houver dados para aquele dia)
        ocupacao_media = []
        for dia in range(7):
            if ocupacao_diaria[dia]:
                ocupacao_media.append(sum(ocupacao_diaria[dia]) / len(ocupacao_diaria[dia]))
            else:
                ocupacao_media.append(None) 
        
        return ocupacao_media