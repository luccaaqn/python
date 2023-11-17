frase= str(input("Digite uma frase :"))

contador= 0

vogal= "aeiou"

for letra in frase :
    if letra in vogal:
        contador += 1
print(contador)        
        
   