supermercado=[]

while True :
    produto= str(input("Nome do produto:"))
    if produto == "sair" :
      break 
    valor= float(input("Valor do produto:"))
    supermercado.append({
    "nome": produto,
    "preço": valor
    })
print(supermercado)    