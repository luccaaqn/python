num1= int(input("digite um numero"))
num2= int(input("digite um numero"))

resultado = 0

operacao = int(input("""
           EScolha uma operação
           1 - somar
           2 - subtrair
           3 - multiplicar
           4 - dividir
"""))

match operacao:
    case 1:
        resultado = num1 + num2
    case 2:
        resultado = num1 - num2
    case 3:
        resultado = num1 * num2
    case 4:
        resultado = num1 / num2
    case _ :
        print("operação invalida")     

if resultado % 2 == 0:
    print(f"{resultado} é par")
else:
    print(f"{resultado} é impar")

if resultado > 0:
    print(f"{resultado} é positivo")
elif resultado < 0:
    print(f"{resultado} é negativo")
else:
    print(f"{resultado} é neutro")                            