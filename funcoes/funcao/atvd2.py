def encontrar_maior_nota(lista_de_notas):
    maior_nota = lista_de_notas[0]
    for nota_atual in lista_de_notas:
        if nota_atual > maior_nota:
            maior_nota = nota_atual

    return maior_nota


lista_notas = []

while True:
    nota = float(input("Digite uma nota: "))
    lista_notas.append(nota)

    decisao = int(input("""
    1 - Continuar
    2 - Sair
"""))
    match decisao:
        case 1:
            continue
        case 2:
            break
        case _:
            print("Opção inválida")

maior_nota = encontrar_maior_nota(lista_de_notas=lista_notas)

print(f"A maior nota digitada foi: {maior_nota:.2f}")