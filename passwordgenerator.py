import random
howmanyloop = True
print("All passwords created are NOT stored by any third parties")
while howmanyloop == True:
    try:
        howmany = int(input("How many characters would you like to have in your password?: "))
        howmanyloop = False
        if howmany >= 93:
            print("Cannot go higher than 92")
            howmanyloop = True
        if howmany <= 8:
            print("Using an 8 character or less password is NOT reccomended")
    except ValueError as e:
        print(e)

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-_=+\|{<}:;>/?\"\'.,`~*&^%$#@!()"

optrunning = True
while optrunning == True:
    option = input("Press ENTER to generate a randomized encrypted password: ")
    result = "".join(random.sample(chars, howmany))
    print(result)
    opt = input("1. Restart \n2. Quit \n ")
    if opt == "2":
        optrunning = False
        break
    if opt == "1":
        opt2running = True
        optrunning = False
        while opt2running == True:
            try:
                howmany = int(input("How many characters would you like to have in your password?: "))
                optrunning = True
                opt2running = False
                if howmany >= 93:
                    print("Cannot go higher than 92")
                    opt2running = True
                elif howmany <= 0:
                    print("Must be a positve value")
                if howmany <= 8:
                    print("Using an 8 character or less password is NOT recommended")
                
            except ValueError:
                print("Must enter valid method")


    