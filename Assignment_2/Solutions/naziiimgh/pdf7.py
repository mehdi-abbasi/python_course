# pdf 7 phone number


number = list(int(input("Enter 8 numbers ")))
print(number)
res = ''            # why not [] ?

if number[0] == 0:
    print ("invalid number. enter numbers again")

else:

#1  atleast 4 repeated numbers
    for i in number:
        res[i] = number.count(i)
        
    print(res)
    
    if (number.count(i)) >= 4 :
        print("Ronde")
    else : print("Rond nist")


#2    3 consecutive numbers

    # for j in range(0,len(number)-2):
    #     if res[j] == res[j+1] and res[j+1] == res[j+2] :
    #         print("Ronde")
    #     else : print("Rond nist")
     
