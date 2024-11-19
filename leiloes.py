class Leilao:
    def __init__(self, id_obra, lance_inicial, data_encerramento):
        self.id_obra = id_obra
        self.lance_inicial = lance_inicial
        self.data_encerramento = data_encerramento
    

    def get_id_obra(self):
        return self.id_obra
    

    def get_lance_inicial(self):
        return self.lance_inicial
    

    def get_data_encerramento(self):
        return self.data_encerramento