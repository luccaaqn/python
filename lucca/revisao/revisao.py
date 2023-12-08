usuario= {
    "Nome": str(input("Qual seu nome?:")),
    "Idade": int(input("Qual sua idade?:")),
    "Altura": float(input("Qual sua altura?:")),
    "Salario": int(input("Quanto voce ganha?:"))
}

if usuario["Idade"]>=18:
    print("pode tirar a habilitação")
else:
    print("nao pode tirar a habilitação")


if usuario["Salario"] >= 5000:
    print("e um programador e?")

elif usuario["Salario"] <5000 and usuario ["Salario"] >3000 :
    print("ta bem em")   

else:
    print("vamo trabalhar mais ne")
        