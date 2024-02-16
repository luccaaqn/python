class Animal:
    def __init__(self,nome:str,raca:str,cor:str,peso:float) -> None:
        self.nome= nome
        self.raca= raca
        self.cor= cor
        self.peso= peso

    def comer(self,nome_comida):
        return f"O animal {self.nome} comeu a comida {nome_comida}"      

class Cachorro(Animal):
    def __init__(self, nome: str, raca: str, cor: str, peso: float,pedigre:bool) -> None:
        super().__init__(nome, raca, cor, peso)
        self.pedigre= pedigre
    def pegar_bolinha(self):
        return f"O cachorro {self.nome} pegou a bolinha"

class Papagaio(Animal):
    def __init__(self, nome: str, raca: str, cor: str, peso: float,asa_cortada:bool) -> None:
        super().__init__(nome, raca, cor, peso)
        self.asa_cortada = asa_cortada
    def voar(self):
        return f"O papagaio {self.nome} está voando"

cachorro1 = Cachorro(nome= "Bob",raca="shitzu",cor="preto",peso=24,pedigre=True)     
papagaio1 = Papagaio(nome="Loro",raca="Papagaio do norte",cor="azul",peso=10,asa_cortada=False)
porco1= Animal(nome="Peppa",raca="grande",cor="rosa",peso=50)


print(cachorro1.comer("osso"))
print(cachorro1.pegar_bolinha())
print(papagaio1.comer("biscoito"))
print(papagaio1.voar())
print(porco1.comer("lavagem"))
  
