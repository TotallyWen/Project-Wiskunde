print("Lijn 1: y = ax + b")
a = float(input("a?"))
b = float(input("b?"))
print("Lijn 2: y = cx + d")
c = float(input("c?"))
d = float(input("d?"))

if a == c:
    print("De twee lijnen zijn parallel")
else:
    x = (d-b)/(a-c)
    y = a*x + b
    print('Kruispunt: {} ,"{}!"'.format(x, y))