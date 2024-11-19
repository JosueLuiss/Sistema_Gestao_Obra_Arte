class Artistas:
    def __init__(self, id, nome, foto, descricao):
        self.id = id
        self.nome = nome
        self.foto = foto
        self.descricao = descricao

    def get_id(self):
        return self.id
    
    def get_nome(self):
        return self.nome
    
    def get_foto(self):
        return self.foto
    
    def get_descricao(self):
        return self.descricao
    
