sem= int(input("quantas semanas foram gastas? "))
day= int(input("quantos dias foram gastos? "))
hr= int(input("quantas horas foram gastas? "))
min= int(input("Quantos minutos foram gastos? "))


result=(sem * 7 * 24 * 60 * 60) + (day * 24 * 60 * 60) + (hr * 60 * 60) + (min * 60)

print("A quantidade de minutos total é:",result, "segundos")


