expression = input("expression: ")
x, y, z = expression.split(" ")

new_x = float(x)
new_z = float(z)

if y == "+":
    result = new_x + new_z
elif y == "-":
    result = new_x - new_z
elif y == "*":
    result = new_x * new_z
elif y == "/":
    result = new_x / new_z

print(round(result, 1))

