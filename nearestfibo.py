"""Nearest fibonocci number"""
Num=int(input("Enter a number: "))
def is_fib(n):
    a,b=0,1
    while True:
        if a==n:
            return a
        if a>n:
           if((n-a) < ((b-a)-n)):
               return b-a
           else:
               return a
        c=a+b
        a=b
        b=c
# if (is_fib(Num)):
#     print("The neares fibonocci num is",Num)

print(is_fib(Num))