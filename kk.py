def  calculaComissao(abadas):
    valorAbada = 80             
    if abadas > 0:         
        return abadas*valorAbada*0.07

abadas= int(input("\nDigite quantos abadas o funcionário vendeu: "))
comissao= calculaComissao(abadas)

print("a comissão do funcionário foi de: R${:.02f}" .format(comissao))