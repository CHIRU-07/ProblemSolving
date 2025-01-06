"""num=int(input("Enter a number to print fibonocci numbers : "))"""
# a,b=0,1
# i=1
# print(a)
# print(b)
# while i<=(num-2):
#      c=a+b
#      print(c)
#      a=b
#      b=c
#      i=i+1


""" method 2"""
# num=int(input("Enter a number to print fibonocci numbers : "))
# a,b=0,1
# i=1
# while i<=num:
#       print(a,end=" ")
#       c=a+b
#       a,b = b,c
#       i+=1




"""Print fibonocci series until it reaches a certain number"""
'''method1'''
# num=int(input("Enter a number to print fibonocci numbers : "))
# a,b=0,1
# while True:
#      if a<=num:
#           print(a,end=" ")
#           c=a+b
#           a,b=b,c
#      else:
#           break
'''method2''' 
num=int(input("Enter a number to print fibonocci numbers : "))
a,b=0,1
while a<=num:
     print(a,end=" ")
     c=a+b
     a,b=b,c
       

