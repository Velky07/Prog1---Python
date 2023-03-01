import bibCorreios

listaC = []
op=1
while op == 1:
  item=input("Digite o tipo do item: ")
  compara=bibCorreios.validaTipoItem(item)
  while compara == False:
    item=input("Opa!\nParece que você escreveu algo errado \nDigite o tipo do item novamente: ")
    compara=bibCorreios.validaTipoItem(item)


  peso=float(input("Digite o peso (em quilo) do item: "))
  comparaPeso=bibCorreios.validaPeso(peso)
  while comparaPeso == False:
    peso=float(input("Opa!\nParece que você escreveu algo errado \nDigite o peso (em quilo) do item novamente: "))
    comparaPeso=bibCorreios.validaPeso(peso)

  embalagem=input("Digite o tamanho da embalagem: ")
  comparaEmba = bibCorreios.validaEmbalagem(embalagem)
  while comparaEmba == False:
    embalagem=input("Opa!\nParece que você escreveu algo errado \nDigite o tamanho da embalagem novamente: ")
    comparaEmba = bibCorreios.validaEmbalagem(embalagem)

  entrega=input("Digite qual o tipo de entrega: ")
  comparaEntr=bibCorreios.validaEntrega(entrega)
  while comparaEntr == False:
    entrega=input("Opa!\nParece que você escreveu algo errado \nDigite qual o tipo de entrega novamente: ")
    comparaEntr=bibCorreios.validaEntrega(entrega)

  PesoG=bibCorreios.convertePeso(peso)
  itemPeso=bibCorreios.calculaCustoItem(item,PesoG)
  embalagemCusto=bibCorreios.calculaCustoEmbalagem(embalagem)
  entregraFrete=bibCorreios.calculaCustoEntrega(entrega)
  custoParcial=(itemPeso + embalagemCusto + entregraFrete)
  
  listaC.append(custoParcial)
  op=int(input("\nDigite 1 para colocar outro pedido \nse deseja sair, digite 0: "))
  while op !=0 and op !=1:
    op = int(input("\nERRO: Opção inválida!\nDigite 1 para colocar outro pedido \nse deseja sair, digite 0: "))

custoTotal=0
for x in listaC:
  custoTotal +=x


print("O custo total do seu pedido é de \nR${:.02f}".format(custoTotal))