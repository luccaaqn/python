class Pessoa:
    def __init__(self,nome:str,idade:int,peso:float,genero:str):
        self.nome= nome
        self.idade= idade
        self.peso= peso
        self.genero= genero
        self.sobrenome= "Silva"

pessoa1= Pessoa(
    nome="cleiton",
    idade= 18,
    peso= 66.5,
    genero= "Masculino",    
)

pessoa2= Pessoa(
    nome="jessica",
    idade= 15,
    peso= 60.5,
    genero= "feminimo",   
)

print(f"A pessoa 1 se chama {pessoa1.nome}, ele tem {pessoa1.idade} anos, esta pesando {pessoa1.peso}kg, se denomina do genero {pessoa1.genero}, seu sobrenome é {pessoa1.sobrenome}")

print(f"A pessoa 2 se chama {pessoa2.nome}, ela tem {pessoa2.idade} anos, esta pesando {pessoa2.peso}kg, se denomina do genero {pessoa2.genero}, seu sobrenome é {pessoa2.sobrenome}")

