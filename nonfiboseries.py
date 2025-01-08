# To print nonFibo series to a certain number
'''num=int(input("Enter a number : "))#5
a,b=0,1
count=0
while (count!=num):
    c=a+b
    a=b
    b=c
    for i in range(a+1,b):
        count+=1
        print(i,end=" ")
        if(count==num):
         break'''
    
#      WAP to print the sum of non-fib numbers as per the input
# input: Enter no. of non-fib series: 3
# output: 17
Num=int(input("Enter a Number: "))
count=sum=0
a,b=0,1
while Num!=count:
    c=a+b
    a=b
    b=c
    for i in range(a+1,b):
        print(i)
        sum+=i
        count+=1
        if(count==Num):
            break
        
print("The sum of Non-fibo series is",sum)


# 1) WAP to convert the decimal to binary
# input: Enter a number: 5
# output: 101

'''Num=int(input("Enter a number: "))
temp=Num
Binary=""
while Num!=0:
    digit=Num%2
    Num=Num//2
    Binary=Binary+str(digit)
    
BinaryNum=Binary[::-1]
print("Binary Number of {} is {}".format(temp,BinaryNum))'''
        
       

