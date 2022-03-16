from ast import Num
import math

ques = int(input("how many questions do you have?"))

for z in range(ques):

    k=0
    numser = list(input("Enter  Numbers").split())

    num_range = range(int(numser[0]),int(numser[1] )+ 1)

    num_list = list(num_range)

    for i in num_list:

        root = math.sqrt(i)
        if int(root + 0.5) ** 2 == i:
            k=k+1
    print(int(k))

    
