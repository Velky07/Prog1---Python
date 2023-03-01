H= float(input("Qual sua altura?"))

man=(72.7*H) - 58
woman=(62.1*H) - 44.7

S= int(input("Você é Homem - 1 ou Mulher - 2?"))

if S==2:
    print("Seu peso ideal é", woman, "kg")
else: 
    print("Seu peso ideal é", man, "kg")
    