# Perfect Number
'''num=int(input("Enter a num :"))
sum=0
for i in range(1,(num//2)+1):
    if(num%i==0):
        sum=sum+i
if sum==num:
    print("f({num} is a perfect Number))
else:
    print("f({num} is not a perfect Number))'''
    


# 1 to 100 perfect Numbers
def perfectnum(num1):
    sum=0
    for i in range(1,(num1//2)+1):
        if(num1%i==0):
            sum+=i
    if(sum==num1):
        return True
    else:
        return False

num=int(input("Enter a Number : "))
count=0
for i in range(1,(num)+1):
    if(perfectnum(i)):
        print(i)
        count+=1
print(f"There are only {count} perfect numbers from 1 to {num}")

    
   