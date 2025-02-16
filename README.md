# Sistema-De-Linhas-De-Onibus

## Sobre o Projeto

Este projeto simula o controle de linhas de ônibus de uma empresa de transporte rodoviário de passageiros. O sistema permite gerenciar linhas de ônibus, verificar disponibilidade de assentos, realizar reservas e gerar relatórios financeiros e de ocupação.

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
- Assentos disponíveis variam de 1 a 20, sendo os ímpares nas janelas e os pares no corredor.

### Geração de Relatórios
- Total arrecadado com venda de passagens no mês corrente para cada linha.
- Ocupação percentual média de cada linha em cada dia da semana (representada por uma matriz).

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

- **Main**: Responsável pela execução do programa e apresentação do menu de opções.
- **Funcoes**: Compõe todas as funções necessários para a execução do código.
- **LinhaDeOnibus**: Gerencia os dados das linhas, incluindo cidades, horários e valor da passagem.
- **Onibus**: Representa os ônibus, com controle de datas de partida e assentos disponíveis.

## Diagrama de Classes

![image](https://github.com/user-attachments/assets/e1a00d55-8a8f-42be-abd0-5f0172429637)
