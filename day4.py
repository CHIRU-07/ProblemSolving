"""WAP to print the count of alphabets, numbers, special characters in the given string without using methods.

input: 10kcoders@gmail.com
output: 
Numbers: 2
Alphabets: 15
Special characters: 2"""
str=input("Enter any string: ")
alpha,num,sp=0,0,0
i=0
while i<len(str):
    if str[i].isalpha():
        alpha+=1
    elif str[i].isdigit():
        num+=1
    else:
        sp+=1
    i=i+1
if(alpha > num and alpha > sp):
    print("Alphabets are more")
elif(num > sp):
    print("Digits are more")
else:
    print("Special characters are more")
print("Alphabets are {} , Numbers are {}, Special characters are {}".format(alpha,num,sp))
