class Veiculo:
    def __init__(self,marca :str,modelo:str,ano:int,preco:float)-> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.preco = preco
        self.velocidade_atual = 0
    
    def acelerar(self,velocidade):
        self.velocidade_atual += velocidade
        return f"o veiculo {self.modelo} acelerou e esta a {self.velocidade_atual} por hora"
    
    def freiar(self):
        if self.velocidade_atual > 10:
            self.velocidade_atual -= 10
            return f"O veículo {self.modelo} freiou e está a {self.velocidade_atual} por hora"
        else:
            self.velocidade_atual = 0
            return f"O veículo {self.modelo} parou"
    
    def buzinar(self):
        return "som indefinido"
    
class Carro(Veiculo):
        def __init__(self, marca: str, modelo: str, ano: int, preco: float,qtde_portas:int) -> None:
             super().__init__(marca, modelo, ano, preco)
             self.qtde_portas = qtde_portas
             self.ar_condicionado = False
            

        def ligar_ar(self):
            if self.ar_condicionado == False:
                self.ar_condicionado = True
                return f"o carro {self.marca}{self.modelo} ligou o ar"
            else:
                return f"o ar ja esta ligado" 

        def buzinar(self):
            return f"bi bi" 
class Navio(Veiculo):

        def buzinar(self):
            return f" fom fom"
        
carro1= Carro(marca="fiat",modelo= "palio", ano=2016,preco=45000, qtde_portas= 4)
navio1= Navio(marca='Aqua Expeditions', modelo= "luxury small", ano=2022,preco=300000,)

print(carro1.acelerar(8))
print(carro1.acelerar(10))
print(carro1.freiar())
print(carro1.freiar())
print(carro1.freiar())
print(carro1.buzinar())
print(carro1.ligar_ar())
print(carro1.ligar_ar())


print(navio1.acelerar(120))
print(navio1.acelerar(10))
print(navio1.freiar())
print(navio1.freiar())
print(navio1.freiar())
print(navio1.buzinar())


            

        
  
        
