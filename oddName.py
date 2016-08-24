userName = input("Please enter your name " )
while userName == "":
    print ("You did not enter anything!")
    userName = input("Please enter your name ")
print (userName[1::2])