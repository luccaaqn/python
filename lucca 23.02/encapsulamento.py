class Pessoa:
    def __init__(self, nome:str, idade:int, altura:float) -> None:
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura
    
    def pegar_o_nome(self):
        return self.__nome
    
    def mudar_o_nome(self, novo_nome):
        self.__nome = novo_nome
        return "Nome alterado com sucesso"




pessoa1 = Pessoa(nome="Sidlixo", idade=22, altura=1.79)
pessoa2 = Pessoa(nome="Maria", idade=30, altura=1.80)

print(pessoa1.pegar_o_nome())
pessoa1.mudar_o_nome("Sidney")
print(pessoa1.pegar_o_nome())









class Pessoa:
    def __init__(self, nome:str, idade:int, altura:float) -> None:
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura
    
    def getNome(self):
        return self.__nome
    
    def setNome(self, newValue:str):
        self.__nome = newValue
        return "Valor alterado com sucesso"
    

    def getIdade(self):
        return self.__idade
    
    def setIdade(self, newValue:str):
        self.__idade = newValue
        return "Valor alterado com sucesso"
    
    
    def getAltura(self):
        return self.__altura
    
    def setAltura(self, newValue:str):
        self.__altura = newValue
        return "Valor alterado com sucesso"



pessoa1 = Pessoa(nome="Sidlixo", idade=22, altura=1.79)
pessoa2 = Pessoa(nome="Maria", idade=30, altura=1.80)

print(pessoa1.getNome())
pessoa1.setNome("Sidney")
print(pessoa1.getNome())