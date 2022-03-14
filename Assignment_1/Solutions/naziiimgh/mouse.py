
p = int(input("Enter a number between 0 ,2"))
h = int(input("Enter a number between 0 ,2"))

if p == h:

    print("happy new year!")
else :

    if p-h == 1:
        print("L")

    if p-h == 2:
        print("LL")

    if h-p == 1:
        print("R")

    if h-p == 2:
        print("RR")
