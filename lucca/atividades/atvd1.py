escola=[]

for i in range(5):
    usuario = {
    "nome": str(input("Qual seu nome:")),
    "endereco": str(input("Qual seu endereço:")),
    "cpf": int(input("Qual seu cpf:")),
    "rg": int(input("Qual seu rg:")),
    "serie": int(input("Qual sua serie:")),
    }
    escola.append(usuario)
print(escola)    


