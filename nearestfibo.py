"""Nearest fibonocci number"""
Num1=int(input("Enter a number :"))
def is_fib(n):
   a,b=0,1
   while a<n:
        c=a+b
        a=b
        b=c
   print(a,b-a)
   if(n-(b-a)<a-n):
       print("The nearest fibo number is",(b-a))
   if(n-(b-a)>a-n):
       print("The nearest fibo number is",a)
       
is_fib(Num1)
