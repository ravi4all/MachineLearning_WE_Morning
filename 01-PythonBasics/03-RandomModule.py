import random

a = ["Hi","Hello","Hey","Hie","Hola","Good Morning","Bye"]
#print(random.choice(a))

#cpu_choice = random.choice(a)

mainLoop = True
while mainLoop:
    user_msg = input("Enter your message : ")
    print(user_msg)
    cpu_choice = random.choice(a)
    print(cpu_choice)

