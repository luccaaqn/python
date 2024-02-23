class Autor:
    def __init__(self, nome:str, idade:int, nacionalidade: str) -> None:
        self.nome = nome
        self.idade = idade
        self.nacionalidade = nacionalidade


class Livro:
    def __init__(self, titulo:str, qtde_paginas:int, ano:int, genero:str, autor:Autor) -> None:
        self.titulo = titulo
        self.qtde_paginas = qtde_paginas
        self.ano = ano
        self.genero = genero
        self.autor = autor

    

autor1 = Autor(nome="João", idade=51, nacionalidade="Brasileiro")
autor2 = Autor(nome="Mary", idade=36, nacionalidade="Inglesa")

livro1 = Livro(titulo="Alguma coisa", qtde_paginas=80, ano=2020, genero="Drama", autor=autor1)


print(livro1.autor.nome)