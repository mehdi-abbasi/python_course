# def my_function (next_int):
#     num = 'abcdefghijklmnopqrstuvwxyz'
#     next_int='' 
#     for j in num: 
#         code = ord(j) #give the ascii code of num  
#         if num == 'z':  #ascii of 'z'
#             nxt_letter = 'a' #ascii of 'a'
#         else : 
#             nxt_letter = chr(code+1)  #give character
#             next_int = next_int + nxt_letter 

# my_function("abcd")    

word = list(input("Enter a word"))
n = int(input("how many times?"))
lenWrod = len(word)

num = {"a" : "b",
"b" : "c",
"c" : "d",
"d" : "e",
"e" : "f",
"f" : "g",
"g" : "h",
"h" : "i",
"i" : "j",
"j" : "k",
"k" : "l",
"l" : "m",
"m" : "n",
"n" : "o",
"o" : "p",
"p" : "q",
"q" : "r",
"r" : "s",
"s" : "t",
"t" : "u",
"u" : "v",
"v" : "w",
"w" : "x",
"x" : "y",
"y" : "z",
"z" : "a"}
   

for i in word:
    print(num[i])


    