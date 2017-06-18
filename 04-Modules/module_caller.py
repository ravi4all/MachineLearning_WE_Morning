from modules import main_module


num_1 = int(input("Enter first number : "))
num_2 = int(input("Enter second number : "))

print("Addition is",main_module.add(num_1,num_2))
print("Subtraction is",main_module.sub(num_1,num_2))
print("Division is",main_module.div(num_1,num_2))
print("Multiplication is",main_module.mul(num_1,num_2))