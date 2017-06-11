##a = 5
##
##for i in range(1,11):
##    print(a*i)

# Pattern Program

a = [i for i in range(0,21) if i%2 == 0]
print(a)

for z in a:
    print(z)

for x in range(0,5):
    for y in range(0,x+1):
        print("*", end="")
    print()

for x in reversed(range(0,5)):
    for y in range(0,x+1):
        print("*", end="")
    print()
