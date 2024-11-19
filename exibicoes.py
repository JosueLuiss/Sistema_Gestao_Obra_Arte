class Exibicao:
    def __init__(self, id, titulo, local, data_inicio, data_termino, curador):
        self.id = id
        self.titulo = titulo
        self.local = local
        self.data_inicio = data_inicio
        self.data_termino = data_termino
        self.curador = curador
    

    def get_id(self):
        return self.id
    

    def get_titulo(self):
        return self.titulo
    

    def get_local(self):
        return self.local
    

    def get_data_inicio(self):
        return self.data_inicio
    

    def get_data_termino(self):
        return self.data_termino
    

    def get_curador(self):
        return self.curador