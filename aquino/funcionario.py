class Funcionario:
    def __init__(self, nome:str,idade:int, funcao:str) -> None:
        self.nome = nome
        self.idade = idade
        self.funcao = funcao
        self.empresa = "Infinity"


func1 = Funcionario(nome="Abel", idade=28, funcao="Professor")
func2 = Funcionario(nome="Will", idade=31, funcao="Coordenador")


print(func1.empresa)
print(func2.empresa)