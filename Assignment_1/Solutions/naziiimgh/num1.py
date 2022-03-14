#compare numbers

k = list(open('1.txt','r'))
# print(k[1600])
for i in range(0,len(k)):
    if k[i] > k[i+1]:
        print('increased')
    else:
        print('decreased')    

