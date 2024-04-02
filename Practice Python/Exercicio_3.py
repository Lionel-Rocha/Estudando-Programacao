a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
for element in a:
  if element < 5:
    b.append(element)

print(b)

#Extras

i = [element for element in a if element < 5]
print(i)

numero = int(input("Digite um número: "))
j = [element for element in a if element < numero]
print(j)
