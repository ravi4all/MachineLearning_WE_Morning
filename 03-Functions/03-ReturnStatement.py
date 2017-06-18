num_1 = int(input("Enter first number : "))
num_2 = int(input("Enter second number : "))

result = 0

def add(num_1,num_2):
    return  num_1 + num_2

def sub(num_1,num_2):
    return  num_1 - num_2

def div(num_1,num_2):
    return  num_1 / num_2

def mul(num_1,num_2):
    return  num_1*num_2

print("Addition is",add(num_1,num_2))
print("Subtraction is",sub(num_1,num_2))
print("Division is",div(num_1,num_2))
print("Multiplication is",mul(num_1,num_2))