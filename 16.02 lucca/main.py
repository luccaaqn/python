class Veiculo:
    def __init__(self,marca:str,modelo:str,cor:str,ano:int) -> None:
       self.marca = marca
       self.modelo = modelo
       self.cor = cor
       self.ano= ano
    def ligar(self):
        return f"O veículo ligou"   

class Carro(Veiculo):
    def __init__(self, marca: str, modelo: str, cor: str, ano: int,qtde_portas) -> None:
        super().__init__(marca, modelo, cor, ano)
        self.qtde_portas = qtde_portas

        def ligar_o_ar(self):
          return f"O carro {self.modelo} ligou o ar condicionado"

class Moto(Veiculo):
    def __init__(self, marca: str, modelo: str, cor: str, ano: int,cilindradas:float) -> None:
        super().__init__(marca, modelo, cor, ano)
        self.cilindradas = cilindradas  

class Bicicleta(Veiculo):
    def __init__(self, marca: str, modelo: str, cor: str, ano: int,marchas:bool) -> None:
        super().__init__(marca, modelo, cor, ano)
        self.marchas =  marchas       

carro1 = Carro(marca="Fiat", modelo="Palio", cor="Azul", ano=2004, qtde_portas=2)
moto1 = Moto(marca="Honda", modelo="500x", cor="Vermelho", ano=2021, cilindradas=500)
bicicleta1 = Bicicleta(marca="Caloi", cor="Cinza", ano=2019, marchas=True)



print(carro1.ligar())
print(carro1.ligar_o_ar())
print(moto1.ligar())
print(bicicleta1.ligar())