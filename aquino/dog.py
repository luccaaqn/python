class Dog:
    def __init__(self, nome:str, raça:str, idade:int):
        self.nome = nome
        self.raça = raça
        self.idade = idade

dog1= Dog (
    nome= "bob",
    raça="shitzu",
    idade= 2
) 

dog2= Dog (
    nome= "bolinha",
    raça="pastor alemão",
    idade= 3
)        

print(f"O nome do primeiro dog e:{dog1.nome}")
print(f"A raça do primeiro dog e:{dog1.raça}")
print(f"A idade do segundo dog e:{dog2.idade}")