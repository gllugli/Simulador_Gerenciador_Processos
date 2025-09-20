from fila_cpu import FilaCPU
from fila_io import Fila_IO

def escalonar(processos):
    tempo_atual = 0
    fila_cpu = FilaCPU()
    fila_io = Fila_IO()
    finalizados = []

    print("===== INÍCIO DA SIMULAÇÃO =====")

    # Enquanto houver processos não finalizados ou filas ocupadas
    while processos or not fila_cpu.vazia() or not fila_io.vazia():

        # 1. Chegada de novos processos no clock atual
        for p in list(processos):
            if p.entrada == tempo_atual:
                fila_cpu.inserir(p)
                processos.remove(p)
                print(f"[t={tempo_atual}] Processo {p.pid} chegou -> FilaCPU")

        # 2. Executar um ciclo de CPU
        if not fila_cpu.vazia():
            p = fila_cpu.items[0]
            p.executar_cpu()
            print(f"[t={tempo_atual}] CPU rodando {p.pid} | proc={p.proc} | qCPU={p.quantum_cpu_restante}")

            if p.proc == 0 and p.io == 0:
                finalizados.append((tempo_atual, p.pid))
                fila_cpu.remover()
                print(f"[t={tempo_atual}] Processo {p.pid} FINALIZADO")

            elif p.proc == 0 and p.io > 0:
                fila_cpu.remover()
                p.resetar_quantum_cpu()
                p.resetar_quantum_io()
                fila_io.inserir(p)
                print(f"[t={tempo_atual}] {p.pid} terminou CPU, foi para IO")

            elif p.quantum_cpu_acabou():
                fila_cpu.remover()
                if p.io > 0:
                    p.resetar_quantum_cpu()
                    p.resetar_quantum_io()
                    fila_io.inserir(p)
                    print(f"[t={tempo_atual}] {p.pid} estourou quantum CPU, foi para IO")
                else:
                    p.resetar_quantum_cpu()
                    fila_cpu.inserir(p)
                    print(f"[t={tempo_atual}] {p.pid} estourou quantum CPU, voltou para CPU")

        # 3. Executar um ciclo de IO
        if not fila_io.vazia():
            p = fila_io.items[0]
            p.executar_io()
            print(f"[t={tempo_atual}] IO rodando {p.pid} | io={p.io} | qIO={p.quantum_io}")

            if p.io == 0 and p.proc == 0:
                finalizados.append((tempo_atual, p.pid))
                fila_io.remover()
                print(f"[t={tempo_atual}] Processo {p.pid} FINALIZADO")

            elif p.io == 0 and p.proc > 0:
                fila_io.remover()
                p.resetar_quantum_io()
                p.resetar_quantum_cpu()
                fila_cpu.inserir(p)
                print(f"[t={tempo_atual}] {p.pid} terminou IO, voltou para CPU")

            elif p.quantum_io_acabou():
                fila_io.remover()
                p.resetar_quantum_io()
                fila_io.inserir(p)
                print(f"[t={tempo_atual}] {p.pid} estourou quantum IO, voltou para IO")

        # 4. Estado geral
        print(
            f"[t={tempo_atual}] Estado: "
            f"CPU={[p.pid for p in fila_cpu.items]} "
            f"IO={[p.pid for p in fila_io.items]} "
            f"Finalizados={finalizados}"
        )

        # 5. Avança o clock
        tempo_atual += 1

    print("===== FIM DA SIMULAÇÃO =====")
    return finalizados
