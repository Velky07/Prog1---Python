import math
F= int(input("Quantos F° está medindo?"))

C= 5 * ((F-32)/9)
print("Então está medindo", C, "C°")
print(math.floor(C),"C°", math.ceil(C), "C°")
