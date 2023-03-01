contador= 0
totalLavand= 0
for i in range(5):
    tipo=input("Informe o tipo da lavagem, entre peça ou peso: ")
    if tipo == "peça":
        qnt_p=int(input("informe a quantidade de peças a serem lavadas: "))
        total= qnt_p * 7
    elif tipo == "peso":
        qnt_pe=float(input("Informe quantos quilos de roupa a serem lavadas: "))
        total= qnt_pe * 5.00
    else:
        print("informação colocada errada, finalizando programa")
        break
    seco=input("A lavagem é a seco? sim ou não: ")
    if seco == "sim":
        ttotal= total + 3.50
        contador += 1
    elif seco == "não":
        ttotal= total
    totalLavand = totalLavand + ttotal
    print("O valor pago foi de {:.02f} reais" .format(ttotal))
  
print("O total arrecadado pela lavanderia foi de", totalLavand, "reais e a quantidade de lavagens a seco foi de", contador)
