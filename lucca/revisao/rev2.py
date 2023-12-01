boletim=[]

for i in range(1,5):
    nome= str(input(f"Digite seu nome:"))
    nota= float(input(f"Digite sua nota:"))

    boletim.append([nome,nota])

maior=0
nome_aluno= " "
for it in boletim:
    if it[1] > maior:
        maior = it[1]
        nome_aluno= it[0]

print(f"O melhor aluno foi {nome_aluno} e sua nota foi {maior}")