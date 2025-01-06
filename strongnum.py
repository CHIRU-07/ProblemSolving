"""Strong number"""
'''method 1'''
# num=input("Enter a number : ")
# sum,fact=0,1
# for i in num:
#     x=int(i)
#     j=1
#     while j<=x:
#         fact=fact*j
#         j+=1
#     sum+=fact
#     fact=1
# if (sum==int(num)):
#     print("{} is a strong Number".format(num))
# else:
#     print("{} is not a strong Number".format(num))   

'''method 2'''
# num=input("Enter a number : ")
# sum,fact=0,1
# for i in num:
#     x=int(i)
#     fact=1
#     for j in range(1,x+1):
#         fact*=j
#     sum+=fact

# if (sum==int(num)):
#     print("{} is a strong Number".format(num))
# else:
#     print("{} is not a strong Number".format(num))  



""" factorial of a number"""
# num=int(input("Enter any number: "))
# fact=1
# for i in range(1,num+1):
#      fact=fact*i
# print("The factorial of {} is {}".format(num,fact))


"""Strong Numbers in the range 1 to 500"""
Num=int(input("Enter a number ,till where you need to find strong Numbers : "))

for i in range(1,Num+1):
    x=str(i)
    sum=0
    for j in x:
        fact=1
        for k in range(1,int(j)+1):
            fact=fact*k
        sum+=fact
    if(sum==i):
        print(i)
    else:
        continue