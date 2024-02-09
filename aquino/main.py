class Moto:
    def __init__(self, marca: str, modelo: str, ano: int, cor: str, cilindradas: float, multa: list, velocidade_atual:int ):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.cilindradas = cilindradas 
        self.multa = multa
        self.velocidade_atual= 0
    def buzinar(self):
        return f"A moto {self.modelo} está buzinando, sai da frente"    
    
    def acelerar(self):
        self.velocidade_atual += 20
        return "A moto esta acelerando"
    
    def freiar(self):
        self.velocidade_atual -= 10
        return "A moto esta freiando"

moto1 = Moto(
            marca = "Honda",
            modelo = "Bros",
            ano = 2016,
            cor= "Preto",
            cilindradas= 162.7,
              multa=[{
                    "infração": "Andar sem chinelo",
                    "valor": 120,
                    "gravidade": "Leve"
            }]
            ) 
print(moto1.buzinar())

moto2 = Moto(
            marca = "Yamaha",
            modelo = "Factor",
            ano = 2019,
            cor= "Vermelha",
            cilindradas= 149.7,
            multa=[{
                    "infração": "Andar sem capacete",
                    "valor": 100,
                    "gravidade": "Leve"
            }]
            )
moto3 = Moto(
            marca = "Yamaha",
            modelo = "Factor",
            ano = 2012,
            cor= "preta",
            cilindradas= 149.7,
            multa=[{
                    "infração": "Andar sem blusa",
                    "valor": 130,
                    "gravidade": "Leve"
            }]
            )         
         




