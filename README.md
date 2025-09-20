# Simulador de Escalonamento de Processos

Este projeto implementa um **simulador de escalonamento de processos** em Python, considerando execução simultânea de **CPU** e **I/O**, com filas específicas para cada recurso e suporte a prioridades e quantums definidos.

---

## Estrutura do Projeto

- **main.py** – ponto de entrada da simulação, responsável por carregar os processos e executar o escalonador
- **escalonador.py** – contém a lógica do escalonamento, controlando CPU e I/O em ciclos de clock
- **fila.py** – classe base de fila (FIFO)
- **fila_cpu.py** – fila da CPU, ordenada por prioridade (menor número = maior prioridade)
- **fila_io.py** – fila de I/O, baseada em FIFO
- **processo.py** – definição da classe `Processo`, com atributos (PID, tempos de entrada/CPU/I/O, prioridade) e métodos de execução
- **dados.txt** – arquivo de entrada com os processos a serem simulados
- **saida.txt** – arquivo gerado com o resultado final da simulação
- **INSTRUCOES.txt** – guia de execução oficial do projeto

---

## Modelo de Entrada

O arquivo `dados.txt` deve conter um processo por linha, no formato:

```
pid;tempo_entrada;tempo_io;tempo_cpu;prioridade
```

### Exemplo:
```
1;0;6;9;2
2;2;4;12;1
```

- **pid** → identificador do processo  
- **tempo_entrada** → ciclo de chegada do processo  
- **tempo_io** → tempo necessário em I/O  
- **tempo_cpu** → tempo necessário em CPU  
- **prioridade** → menor número = maior prioridade  

---

## Modelo de Saída

Ao final da execução, o programa gera o arquivo `saida.txt` com os processos finalizados no formato:

```
tempo_final;pid
```

### Exemplo:
```
16;2
22;1
```

---

## Regras da Simulação

- Quantum da CPU: **3 ciclos**  
- Quantum do I/O: **6 ciclos**  
- CPU e I/O são executados **simultaneamente a cada ciclo**  
- Escalonamento:
  - CPU → fila ordenada por prioridade  
  - I/O → fila FIFO (ordem de chegada)  
- A execução continua até que **todos os processos sejam finalizados**.  

---

## Como Executar

1. Certifique-se de ter o **Python 3.x** instalado:
   ```bash
   python --version
   ```
2. Coloque todos os arquivos na mesma pasta.  
3. Configure o arquivo `dados.txt` com os processos que deseja simular.  
4. Execute no terminal:
   ```bash
   python main.py
   ```
   ou, em alguns ambientes:
   ```bash
   python3 main.py
   ```
5. Ao final, consulte o arquivo `saida.txt` para verificar a ordem e o tempo de finalização dos processos.  

---

## Exemplo de Execução

Entrada (`dados.txt`):
```
1;0;6;9;2
2;2;4;12;1
```

Execução (`python main.py`):  
- Logs exibem a movimentação dos processos entre CPU, I/O e finalização.  

Saída (`saida.txt`):
```
16;2
22;1
```

---

## Observações

- O código imprime no terminal o estado das filas e processos a cada ciclo de clock.  
- É possível ajustar quantums e lógica de escalonamento alterando os métodos da classe `Processo` e do `escalonador`.  
- O simulador é modular e pode ser estendido para implementar novos algoritmos de escalonamento.  
