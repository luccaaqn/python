def i (horario):
    
  
    if horario >= 13 and horario <=18:
     return "boa tarde "

    elif horario >= 5 and horario <= 12:
     return "bom dia "


    elif horario >= 19 and horario <= 23:
     return "boa noite "     

    else:
     return "vai dormir , ta de madrugada ja"   
   

hr = int(input("Que horas são?:"))
print(i(hr))