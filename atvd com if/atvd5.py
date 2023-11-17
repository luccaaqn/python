av1= float(input("Digite sua nota da av1 :"))
av2= float(input("Digite sua nota da av2 :"))
av3= float(input("Digite sua nota da av3 :"))
av4= float(input("Digite sua nota da av4 :"))

if (av1+av2+av3+av4) / 4 >= 7 and (av1+av2+av3+av4) /4 < 10:
    print("APROVADO")
elif (av1+av2+av3+av4) / 4 < 7:
    print("REPROVADO")
elif (av1+av2+av3+av4) / 4 == 10:
    print("APROVADO COM DISTINÇÃO")   
else:
    print("ALGUMA NOTA ESTA ERRADA")    
