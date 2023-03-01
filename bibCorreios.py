#No arquivo bibCorreios.py, crie uma função chamada validaTipoItem que recebe como parâmetro um tipo de item e retorne True caso seja válido, ou False caso contrário. Copie e cole o código da função desenvolvida (ou o link para o código) no espaço reservado abaixo:

def validaTipoItem(item):
  ListaTipo = ["pacote","PACOTE", "Pacote", "Documento", "DOCUMENTO", "documento"]
  if str(item) in ListaTipo:
    return(True)
  else:
    return(False)
    
assert validaTipoItem("PACOTE")
assert not validaTipoItem("Doc")
assert not validaTipoItem(5)

#FIM DA FUNÇÃO validaTipoItem.



#No arquivo bibCorreios.py, crie uma função chamada validaPeso que recebe como parâmetro o peso de um item (em quilos) e retorne True caso seja maior ou igual a zero, ou False caso contrário. Copie e cole o código da função desenvolvida (ou o link para o código) no espaço reservado abaixo:

def validaPeso(Peso):
  if float(Peso) >= 0:
    return(True)
  else:
    return(False)  


assert validaPeso(5)
assert validaPeso(0.8)
assert not validaPeso(-2)

#FIM DA FUNÇÃO validaPeso.



#No arquivo bibCorreios.py, crie uma função chamada convertePeso que recebe como parâmetro o peso de um item (em quilos) e retorne o valor equivalente em gramas. Copie e cole o código da função desenvolvida (ou o link para o código) no espaço reservado abaixo:

def convertePeso(Pesodoitem):
  return(Pesodoitem*1000)

assert convertePeso(5) == 5000
assert convertePeso(0.8) == 800

#FIM DA FUNÇÃO convertePeso.



#No arquivo bibCorreios.py, crie uma função chamada calculaCustoItem que recebe como parâmetro o tipo de item e o peso (em gramas) e retorne o custo correspondente. Copie e cole o código da função desenvolvida (ou o link para o código) no espaço reservado abaixo:

def calculaCustoItem(Tipo, PesoemG):
    ListaTipo = ["pacote","PACOTE", "Pacote", "Documento", "DOCUMENTO", "documento"]
    for y in range(6):
        if ListaTipo[y] == Tipo and y <=2: 
            custo = 3 * PesoemG/1000
            return custo
        elif ListaTipo[y] == Tipo  and y > 2: 
            custo = 2 * PesoemG/1000
            return custo


assert calculaCustoItem("Pacote",300) == 0.90
assert calculaCustoItem("Documento",150) == 0.30
assert calculaCustoItem("Documento",0) == 0

#FIM DA FUNÇÃO calculaCustoItem.



#No arquivo bibCorreios.py, crie uma função chamada validaEmbalagem que recebe como parâmetro um tipo de embalagem e retorne True caso seja válido, ou False caso contrário. Copie e cole o código da função desenvolvida (ou o link para o código) no espaço reservado abaixo:

def validaEmbalagem(x):
  listaEmbala = ["Pequena","pequena", "PEQUENA", "MÉDIA", "Média", "média", "Grande", "grande", "GRANDE"]
  if str(x) in listaEmbala:
    return(True)
  else:
    return(False)


assert validaEmbalagem("Pequena")
assert validaEmbalagem("MÉDIA")
assert not validaEmbalagem ("G")


#FIM DA FUNÇÃO validaEmbalagem.  


#No arquivo bibCorreios.py, crie uma função chamada calculaCustoEmbalagem que recebe como parâmetro o tipo de embalagem desejada e retorne o custo correspondente. Copie e cole o código da função desenvolvida (ou o link para o código) no espaço reservado abaixo.

def calculaCustoEmbalagem(x):
  listaEmbala = ["Pequena","pequena", "PEQUENA", "MÉDIA", "Média", "média", "Grande", "grande", "GRANDE"]
  for y in range(9):
    if listaEmbala[y] == x and y<=2:
      custoEmbala = 4
      return custoEmbala
    elif listaEmbala[y] == x and y>2 and y<=5:
      custoEmbala  = 7
      return custoEmbala
    elif listaEmbala[y] == x and y>5:
      custoEmbala = 10
      return custoEmbala


assert calculaCustoEmbalagem("Pequena") == 4
assert calculaCustoEmbalagem("Média") == 7
assert calculaCustoEmbalagem("GRANDE") == 10

#FIM DA FUNÇÃO calculaCustoEmbalagem.



#No arquivo bibCorreios.py, crie uma função chamada validaEntrega que recebe como parâmetro um tipo de entrega e retorne True caso seja válido, ou False caso contrário. Copie e cole o código da função desenvolvida (ou o link para o código) no espaço reservado abaixo

def validaEntrega(x):
    ListaEntrega = ["Normal","normal","NORMAL","Sedex","sedex","SEDEX","Sedex 10","sedex 10","SEDEX 10"]
    if str(x) in ListaEntrega:
      return(True)
    else:
      return(False)

assert validaEntrega("Normal")
assert validaEntrega("SEDEX")    
assert not validaEntrega("SEDEX 20")

#FIM DA FUNÇÃO validaEntrega.


#No arquivo bibCorreios.py, crie uma função chamada calculaCustoEntrega que recebe como parâmetro o tipo de entrega desejada e retorne o custo correspondente. Copie e cole o código da função desenvolvida (ou o link para o código) no espaço reservado abaixo.

def calculaCustoEntrega(x):
    ListaEntrega = ["Normal","normal","NORMAL","Sedex","sedex","SEDEX","Sedex 10","sedex 10","SEDEX 10"]
    for y in range(9):
      if ListaEntrega[y] == x and y<=2:
        custoEntr=0
        return custoEntr
      elif ListaEntrega[y] == x and y>2 and y<=5:
        custoEntr=5
        return custoEntr
      elif ListaEntrega[y] == x and y>5:
        custoEntr=8
        return custoEntr

assert calculaCustoEntrega("Normal") == 0
assert calculaCustoEntrega("Sedex") == 5
assert calculaCustoEntrega("Sedex 10") == 8

#FIM DA FUNÇÃO calculaCustoEntrega.



