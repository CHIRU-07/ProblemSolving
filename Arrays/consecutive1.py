"""Given an array that contains only 1 and return 0 return count of maximum consecutive ones in the array"""
num=input().split(" ")
c=max1=0
for i in num:
    if i=="1":
        c+=1
    else:
        c=0
    max1=max(max1,c)
print(max1)