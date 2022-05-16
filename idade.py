# calculadora de média escolar

nota1 = float(input("Nota da p1: "))
nota2 = float(input("Nota da p2: "))

media = (nota1 + nota2) / 2

print("Sua media: ")
print(media)

if media >=5:
	print("Voce foi aprovado!")
else:
	print("Voce nao foi aprovado!")