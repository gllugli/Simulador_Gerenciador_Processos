from processo import Processo
from escalonador import escalonar

def carregar_processos(caminho):
    processos = []
    with open(caminho, "r") as arquivo:
        for linha in arquivo:
            if linha.strip():
                pid, entrada, io, proc, prioridade = linha.strip().split(";")
                p = Processo(int(pid), int(entrada), int(io), int(proc), int(prioridade))
                processos.append(p)
    return processos

if __name__ == "__main__": 
    processos = carregar_processos("dados.txt")
    print("Processos carregados:")
    for p in processos:
        print(p.pid, p.entrada, p.io, p.proc, p.prioridade)

    finalizados = escalonar(processos)
    print("\nRESULTADO FINAL:", finalizados)
    
    with open("saida.txt", "w") as f:
        for tempo, pid in finalizados:
            f.write(f"{tempo};{pid}\n")

