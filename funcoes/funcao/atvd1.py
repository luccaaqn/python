def cal_retangulo(comp,larg):
    return comp* larg

comprimento= float(input("Digite o comprimento do retangulo:"))
largura= float(input("Digite a largura do retangulo:"))

area= cal_retangulo(comp= comprimento, larg=largura)
print(f" A area do retangulo e {area:2f}")