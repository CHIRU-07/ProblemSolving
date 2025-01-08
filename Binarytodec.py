# By taking input as a number
'''Num=int(input("Enter a binary number: "))
temp=Num
digits=dec=0
count=0
while Num!=0:
    digits=Num%10
    Num=Num//10
    dec=digits*(2**count)+dec
    count+=1
print(dec)'''

# By taking input as a string
# Method 1
'''Num=input(("Enter a binary number: "))
dec=0
for i in range(0,len(Num)):
    # print(i,Num[(len(Num))-1-i])
    dec=int(Num[i])*(2**(len(Num)-1)-i)+dec
print(dec)'''
# method 2
'''Num=input("Enter a binary Number: ")
count=dec=0
for i in range(len(Num)-1,-1,-1):
    # print(Num[i])
    dec=int(Num[i])*(2**count)+dec
    count+=1
print(dec)'''