def x (i):
   cont_vogais= 0

   for letra in i:
        if letra in "aeiou":
          cont_vogais +=1

   return cont_vogais 

texto= str(input("digite uma palavra:"))

print(x(i=texto))