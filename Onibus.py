class Onibus:
    def __init__(self, idOnibus, dataPartida, assentosDisponiveis):
        # Inicializa o objeto ônibus com ID, data de partida e assentos disponíveis
        self.idOnibus = idOnibus
        # Formata a data de partida
        self.dataPartida = self._convert_data_format(dataPartida)
        # Lista de assentos disponíveis
        self.assentosDisponiveis = list(assentosDisponiveis)

    def _convert_data_format(self, data):
        # Converte a data para o formato 'dd/mm/aaaa' se for um objeto de data
        return data.strftime('%d/%m/%Y') if hasattr(data, 'strftime') else data
    
    def calcular_ocupacao(self):
        # Calcula a ocupação em percentual dos assentos
        if self.assentosDisponiveis == 0:
            return 0  # Retorna 0 se não houver assentos disponíveis
        else:
            # Calcula o número de assentos ocupados
            assentosOcupados = 20 - len(self.assentosDisponiveis)

        # Retorna o percentual de ocupação dos assentos
        return assentosOcupados * 5