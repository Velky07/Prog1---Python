#Escreva um programa que receba como entrada a quantidade de 
#residentes na casa de cada funcionário de uma empresa, até que seja informado o 
#número zero. Assegure que o usuário não informe uma quantidade inválida de residentes (por exemplo, número negativo). 
#Em seguida, o programa deve exibir a quantidade média de residentes das casas dos 
#funcionários e quantos funcionários moram em uma casa com 5 ou mais residentes. 
func=0
func2=0
res=0
n=1
while n>0:
    n= int(input("Quantas pessoas moram com você?(apenas números naturais): "))
    if n>0:
        res=res+n
        func=func+1
    if n>=5:
        func2=func2+1
    while n<0:
        print("ERRO: O valor informado deve ser maior que zero")
        n= int(input("Quantas pessoas moram com você?(apenas números naturais)"))

media=res/func

print("\nVocê digitou 0, o programa se encerrou\n")
print("A média dos residêntes dos funcionários é {:.02f}, e {} funcionários moram com 5 pessoas ou mais".format(media, func2))