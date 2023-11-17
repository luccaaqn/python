letra= str(input("Digite uma letra:")).upper()

if letra in "AEIOU" :
    print(f"a letra {letra} é uma vogal")
elif letra.isalpha() :
    print(f"a letra {letra} é uma consoante")
else:
    print("Você nao digitou uma letra")    
