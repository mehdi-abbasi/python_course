
p = int(input("Enter a number between 0 ,10"))
h = int(input("Enter a number between 0 ,10"))

if p == h:

    print("happy new year!")
else :

    if p>h:
        print(str("L")*int(p-h))

    if h>p:
        print(str("R")*int(h-p))