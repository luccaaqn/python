def somar(n1,n2):
    return n1 + n2

def subtrair(n1,n2):
    return n1 - n2

def multiplicar(n1,n2):
    return n1 * n2

def dividir(n1,n2):
    if n2 == 0:
        return "Não pode dividir por 0"
    else:
        return n1 / n2


numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

while True:
    menu = int(input("""
    Escolha uma opção:
    1 - Somar
    2 - Subtrair
    3 - Dividir
    4 - Multiplicar
    0 - Sair
    """))

    match menu:
        case 1:
            print(somar(n1=numero1, n2=numero2))
        case 2:
            print(subtrair(n1=numero1, n2=numero2))
        case 3:
            print(multiplicar(n1=numero1, n2=numero2))
        case 4:
            print(dividir(n1=numero1, n2=numero2))
        case 0:
            print("Fim do programa")
            break
        case _:
            print("Opção inválida")




