Nome= input("Nome do Aluno: ")

pr1= float(input("Digite a primeira nota do aluno: "))

ps1= float(input("Digite o peso da primeira nota: "))

pr2= float(input("Digite a segunda nota do aluno: "))

ps2= float(input("Digite o peso da segunda nota: "))


MP= ((pr1 * ps1) + (pr2 * ps2)) / (ps1 + ps2)

print("A média Ponderada do aluno", Nome, "é:", MP)
