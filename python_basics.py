


# Comentario en linea
''' Comentario 1 '''
""" Comentario 2 """

print("Hello World!")

print(type(print))
print(type(1))
print(type(1.0))
print(type("Hello World!"))
print(type("None"[1]))
print(type(True))


# Variables
print("---------- Variables ----------")
a = "hola"
print(type(a))
a : int = 10
print(type(a))
b = 1.0
c = 1
d = "None"[1]
e = True

# String
print("---------- String ----------")
# Concatenar
print("---------- Concatenar ----------")
product_name = "manzanas"
quantity = 10

print ('ha comprado ' + str(quantity) + ' ' + product_name)
print("ha comprado {} {}".format(quantity, product_name))
print("ha comprado %d %s" % (quantity, product_name))
print(f"ha comprado {quantity} {product_name}")



# id = input("Introduce a number: ")
# print(id)

address = "calle de la fantasia n13 4D"
print(address[0])
print(address[0:5])
print(address[2:])
print(address[:6])
print(address[-2])
print(address[::-1])
print(address[::-2])

# Functions
print("---------- Functions ----------")
print(address.capitalize())
print(address.lower())
print(address.upper())
print
