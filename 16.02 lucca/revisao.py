from datetime import datetime

class Funcionario:
    def __init__(self, nome:str,cpf:str,telefone: str,idade:int,altura: float ) -> None:
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.altura= altura
        self.telefone= telefone
        
def bater_ponto(self):
    hora_atual:datetime.now().hour
    minuto_atual:datetime.now().minute
    return f"O funcionario(a) bateu o ponto as {hora_atual}:{minuto_atual}"

func1 = Funcionario(nome="João", cpf="000.555.666-88", telefone="(85) 98456-2145", idade=29, altura=1.82)
func2 = Funcionario(nome="Maria", cpf="000.555.666-81", telefone="(85) 98456-2142", idade=21, altura=1.67)
func3 = Funcionario(nome="Pedro", cpf="000.555.666-82", telefone="(85) 98456-2143", idade=25, altura=1.89)


print(func1.bater_ponto())
print(func2.bater_ponto())
print(func3.bater_ponto())
