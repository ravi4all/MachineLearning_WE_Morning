def bio(name,age,*address):
    print("Name is {} and Age is {}".format(name,age))
    #print("Address is {}".format(address))

    for a in address:
        print(a,end="")

#bio(name="Ram",age=20)

#bio(name="Ram",age=20)

#bio("Shyam",20)

bio("Ram",20,"Delhi","Rohini","Pocket-7",12,12,1,2)