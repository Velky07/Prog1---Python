def calculaBonus(abadas):
    if abadas > 50: 
        return 70
    else:
        return 0

abadas= int(input("\nDigite quantos abadas o funcionário vendeu: "))
bonus= calculaBonus(abadas)

print("O bônus do funcionário foi de: {}" .format(bonus))