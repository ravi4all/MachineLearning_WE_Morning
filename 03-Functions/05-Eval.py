def calc(choice):
    num_1 = input("Enter first number : ")
    num_2 = input("Enter second number : ")
    result = 0
    opr = '+'
    if choice == "1":
        opr = '+'
        # result = num_1 + num_2
        # print(result)
    if choice == "2":
        opr = '-'
        # result = num_1 - num_2
        # print(result)
    result = num_1 + opr + num_2
    expression = eval(result)
    print(expression)


print("""
Enter your choice :
1. Add
2. Sub
3. Div
4. Mul
""")

options = {"1":calc,"2":calc,"3":calc,"4":calc}
choice = input("Enter your choice : ")
options.get(choice)(choice)