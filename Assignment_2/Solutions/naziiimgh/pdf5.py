from ast import Num
import math

k=0
number1 = int(input("Enter first Number"))
number2 = int(input("Enter second Number"))


num_range = range(number1,number2 + 1)

num_list = list(num_range)

print(num_list)

for i in range(1,len(num_list)):

    root = math.sqrt(i)
    if int(root + 0.5) ** 2 == i:
        a = print(i, "is a perfect square")
        k=k+1
    else:
        print(i, "is not a perfect square")

print(a)
print("number of perfect square numbers betwen number1 & number2 :" ,k)
