class Processo:
    def __init__(self, pid, entrada, io, proc, prioridade):
        self.pid = pid
        self.entrada = entrada
        self.io = io
        self.proc = proc
        self.prioridade = prioridade
        self.quantum_cpu_restante = 3   # sempre 3 quando entra na CPU
        self.quantum_io = 6         # sempre 6 quando entra no I/O

    def __str__(self):
        return f"Processo(id={self.pid}, entrada={self.entrada}, io={self.io}, proc={self.proc}, prioridade={self.prioridade})"
    
    def executar_cpu(self):
        if self.proc > 0:
            self.proc -= 1
            self.quantum_cpu_restante -= 1

    def cpu_terminou(self):
        return self.proc == 0

    def quantum_cpu_acabou(self):
        return self.quantum_cpu_restante == 0

    def resetar_quantum_cpu(self):
        self.quantum_cpu_restante = 3

    def executar_io(self):
        if self.io > 0:
            self.io -= 1
            self.quantum_io -= 1

    def io_terminou(self):
        return self.io == 0

    def quantum_io_acabou(self):
        return self.quantum_io == 0

    def resetar_quantum_io(self):
        self.quantum_io = 6
