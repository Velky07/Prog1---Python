def  calculaComissao(abadas):
    valorAbada = 80             
    if abadas > 0:         
        return abadas*valorAbada*0.07

def calculaBonus(abadas):
    if abadas > 50: 
        return 70
    else:
        return 0

comissaoFunc = []
totalAbadas= 0
op = 1
while op == 1:

    abadas = int(input("\nDigite quantos abadas o funcionário vendeu: "))
    comissao = calculaComissao(abadas)                                                          #Chama a função 'comissão' passando parametro 'abadas' e retorna o valor de 'comissão'
    bonus = calculaBonus(abadas)                                                                #Chama a função 'bonus' passando parametro 'abadas' e retorna o valor de 'bonus'

    comissaoFunc.append(comissao+bonus)                                                         #Adiciona o valor da comissao+bonus na lista 'comissaoFunc'
    totalAbadas += abadas                                                                       #Conta o total de abadas
    op = int(input("\nDigite 1 para continuar ou 0 para sair: "))
    while op != 0 and op !=1:                                                                   #Enquanto a opção for diferente de 0 e diferente de 1:
        op = int(input("\nERRO: Opção inválida!\nDigite 1 para continuar ou 0 para sair: ")) 
    
for x in comissaoFunc:                                                                          #Percorre a lista 'comissaoFunc', x é o valor da posição
    print("A comissão do funcionario {} foi de: R${:.02f}".format(comissaoFunc.index(x)+1,x))   #comissaoFunc.index(x) é a posição do vetor, e x é oque ta nele.

print("\nA quantidade do total de abadas foi de: {}".format(totalAbadas))



