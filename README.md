# Sistema-De-Linhas-De-Onibus

## Sobre o Projeto

Este projeto simula o controle de assentos disponíveis em ônibus de uma empresa de transporte rodoviário de passageiros. O sistema permite gerenciar linhas de ônibus, verificar disponibilidade de assentos, realizar reservas e gerar relatórios financeiros e de ocupação.

As principais funcionalidades incluem:
- Cadastro e gerenciamento de linhas de ônibus.
- Consulta de horários e assentos disponíveis.
- Reserva de passagens com controle de assentos.
- Geração de relatórios de arrecadação e ocupação média.

---

## Funcionalidades

### Cadastro de Linhas
- Inserir novas linhas informando cidade de origem, cidade de destino, horário de partida e valor da passagem.
- Remover linhas cadastradas.
- Alterar informações de linhas existentes.

### Consultar Horários
- Exibir todos os horários de partida disponíveis para uma determinada cidade de destino.

### Consultar Assentos
- Listar os assentos disponíveis em um ônibus específico informando:
  - Cidade de destino
  - Horário de partida
  - Data da viagem (inferior a 30 dias contados a partir da data atual)

### Reservar Assentos
- Após consultar a disponibilidade, é possível reservar assentos específicos.
- As reservas só podem ser realizadas para ônibus que ainda não partiram.
- Assentos disponíveis variam de 1 a 20, sendo os ímpares nas janelas.

### Geração de Relatórios
- Total arrecadado com venda de passagens no mês corrente para cada linha.
- Ocupação percentual média de cada linha em cada dia da semana (representado por uma matriz).

### Manipulação de Arquivos
- Permite ler reservas de um arquivo texto no seguinte formato:
    ```
    CIDADE, HORÁRIO(hh:mm), DATA(dd/mm/aaaa), ASSENTO
    ```
  - Cada linha do arquivo representa uma reserva.
- Grava em um arquivo texto todas as reservas que não puderam ser realizadas, junto com o motivo (ex.: ônibus cheio, ônibus já partiu, assento ocupado).

---

## Estrutura do Código

O projeto é composto pelas seguintes classes principais:

- **MainTransporte**: Responsável pela execução do programa e apresentação do menu de opções.
- **LinhaTransporte**: Gerencia os dados das linhas, incluindo cidades, horários e valor da passagem.
- **OnibusTransporte**: Representa os ônibus, com controle de datas de partida e assentos disponíveis.
- **ReservaTransporte**: Gerencia as reservas realizadas, incluindo a verificação de disponibilidade.
- **RelatorioTransporte**: Gera os relatórios de arrecadação e ocupação média.
- **ArquivoTransporte**: Manipula leitura e gravação de reservas em arquivos texto.

---

## Regras e Restrições

- Cada linha deve ter um conjunto de horários diários de partida.
- Assentos disponíveis variam de 1 a 20, sendo os ímpares nas janelas.
- A data da viagem deve ser inferior a 30 dias, contados a partir da data atual.
- Nenhuma passagem pode ser comercializada para ônibus que já partiram (consultando o relógio do sistema).
- Reservas lidas de arquivo são processadas sequencialmente, e as não realizadas são registradas com o motivo.
