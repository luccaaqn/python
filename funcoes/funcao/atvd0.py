def media(n1,n2,n3):
    return (n1+n2+n3) / 3

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))


resultado_media = media(n1=numero1, n2=numero2, n3=numero3)


if resultado_media >= 7:
    print(f"Aprovado com a média {resultado_media:.2f}")
else:
    print("Reprovado")