semafaro= lambda cor: "ACELERE" if cor == "verde" else "ATENÇÃO" if cor == "amarelo" else "PARE" if cor == "vermelho" else "COR INVALIDA"

cores= str(input("Digite uma cor: "))

print(semafaro(cores.lower()))