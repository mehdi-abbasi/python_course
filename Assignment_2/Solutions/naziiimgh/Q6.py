from tkinter import N

num = {"a" : "b","b" : "c","c" : "d","d" : "e","e" : "f","f" : "g","g" : "h","h" : "i","i" : "j","j" : "k","k" : "l","l" : "m","m" : "n","n" : "o","o" : "p","p" : "q","q" : "r","r" : "s","s" : "t","t" : "u","u" : "v","v" : "w","w" : "x","x" : "y","y" : "z","z" : "a"}

n = int(input("how many times?"))
word = list(input("Enter a word"))

for j in range(n): 

    nword = word[-1:] + word[:-1] 


    for t in nword:
        for i in range(0,len(word)):

            if str(nword[i])=='z':
                str(nword[i])=='a'

            word = list(str(num[t]))
            
        print(word)