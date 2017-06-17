a = ["This","is","Python","Programming...","Python","is","Awseome"]

x = "Python"

##if x in a:
##    print("Exist")
    

for i in a:
    #print(a.index(i))
    if x == i:
        ind = a.index(i)
        #print(ind)
        del(a[ind])

#print(a)

for j in a:
    print(j)
