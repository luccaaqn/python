gato= { 
  "Nome": str(input("Qual nome do gato:")),
    "Cor":str(input("Qual a cor do gato:")),
    "Raça":str(input("Qual a raça do gato:")),
    "Adestrado":bool(input("O gato e adestrado:")),
    "Idade": int(input("Qual idade do gato:"))
}

if gato ["Idade"] > 3:
  print("ta velho em")

else:
  print("ta novo em")
  gato["vacinado"] = True
  print(gato)
