result = 0

def add():
    num_1 = int(input("Enter first number : "))
    num_2 = int(input("Enter second number : "))
    result = num_1 + num_2
    print(result)

def sub():
    num_1 = int(input("Enter first number : "))
    num_2 = int(input("Enter second number : "))
    result = num_1 - num_2
    print(result)

def div():
    num_1 = int(input("Enter first number : "))
    num_2 = int(input("Enter second number : "))
    result = num_1 / num_2
    print(result)

def mul():
    num_1 = int(input("Enter first number : "))
    num_2 = int(input("Enter second number : "))
    result = num_1 * num_2
    print(result)


print("""
Enter your choice :
1. Add
2. Sub
3. Div
4. Mul
""")

options = {"1":add,"2":sub,"3":div,"4":mul}
choice = input("Enter your choice : ")
options.get(choice)()