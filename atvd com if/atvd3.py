sex= str(input("""
Digite o seu sexo :
F-FEMININO
M-MASCULINO 
""")).upper().strip()

if sex == "M" or sex == "MASCULINO" :
    print(f"O seu sexo é  {sex}")

elif sex == "F" or sex == "FEMININO":
    print(f"O seu sexo é  {sex}")  

else:
    print("Sexo indefinido")   
