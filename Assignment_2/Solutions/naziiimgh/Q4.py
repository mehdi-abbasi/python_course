# pdf 4  watermelon


list1 = list(map(int, input("Enter 5 numbers between 0,100: ").split()))
print(list1)
k=0

for i in range(0,len(list1)):

    if (list1[i] > 80):

        k=k+1
    
print(k)

if k >= 3:
    print("mamma mia!")    

if k <=2 and k >=1 :
    print("mamma mia!!") 

else : print("mamma mia!!!") 





