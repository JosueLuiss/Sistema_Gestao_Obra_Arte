class Obra_arte:
    def __init__(self, id, titulo, autor, foto, ano, descricao, categoria, id_autor, id_exibicao):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.foto = foto
        self.ano = ano
        self.descricao = descricao
        self.categoria = categoria
        self.autor = id_autor
        self.id_exibicao = id_exibicao

    def get_id(self):
        return self.id
    
    def get_titulo(self):
        return self.titulo
    
    def get_autor(self):
        return self.autor
    
    def get_foto(self):
        return self.foto
    
    def get_ano(self):
        return self.ano
    
    def get_descricao(self):
        return self.descricao
    
    def get_categoria(self):
        return self.categoria
    
    def get_id_autor(self):
        return self.id_autor
    
    def get_id_exibicao(self):
        return self.id_exibicao

    