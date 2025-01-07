# Nearest prime number for a given number
"""num=int(input("Enter a number : "))
leftPrime,RightPrime=num-1,num+1
def is_prime(n):
    if n>1:
       for i in range(2,(n//2)+1):
           if (n%i==0):
               return False
       return True
    return False
i=0
while(i==0):
    if(is_prime(leftPrime)):
        print("Just before prime of a num :",leftPrime)
        break
    leftPrime-=1
while(i==0):
    if(is_prime(RightPrime)):
        print("Just after prime of a num :",RightPrime)
        break
    RightPrime+=1

a=num-leftPrime
b=RightPrime-num
if(is_prime(num)):
    print(num,"is nearest Prime")
else:
    if(a<b):
        print(leftPrime,"is nearest prime Number")
    print(RightPrime,":is nearest prime Number")"""

# sum of prime digits in the number
num=input("Enter a number: ")
sum=0
def primenum(n):
    if n>1:
       for i in range(2,10):
        if (n%i==0):
            return False
        return True
    return False

for i in num:
    if(primenum(int(i))):
        sum+=int(i)
print(sum)