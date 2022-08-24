import random
response = "y"
def dfjsldfjs(response) :
    if response == "y":
        no = random.randint(1,6)
        if no == 1:
            print("[   ]")
            print("[ * ]")
            print("[   ]")
        if no == 2:
            print("[ * ]")
            print("[   ]")
            print("[ * ]")
        if no == 3:
            print("[*  ]")
            print("[ * ]")
            print("[  *]")
        if no == 4:
            print("[* *]")
            print("[   ]")
            print("[* *]")
        if no == 5:
            print("[* *]")
            print("[ * ]")
            print("[* *]")
        if no == 6:
            print("[* *]")
            print("[* *]")
            print("[* *]")
        response = str(input("Would you like to roll the dice? y or n?:"))
while response == "y":
    dfjsldfjs(response)