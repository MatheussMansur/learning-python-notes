width = 10
height = 5
area = width * height
print("area:", area)

# type conversion
print(type(width), type(float(width)), type(str(width)))
print(int(10.9))  # 10, it just cuts the decimal part

# division
print(10 / 3)
print(10 // 3)
print(10 % 3)

# trying the if order thing from the module
x = 7
y = 49
if 2 * x == y:
    print("y is double of x")
elif x ** 2 == y:
    print("y is x squared")
else:
    print("no relation")
