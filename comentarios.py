class Comentario:
    def __init__(self, id, nome_usuario, comentario, data):
        self.id = id
        self.nome_usuario = nome_usuario
        self.comentario = comentario
        self.data = data
    

    def get_id(self):
        return self.id
    
    
    def get_nome_usuario(self):
        return self.nome_usuario
    
    
    def get_comentario(self):
        return self.comentario
    

    def get_data(self):
        return self.data