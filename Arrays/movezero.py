"""You are given an array of integers, your task is to move all the zeroes
 in the array to the end of the array and move non-negative integers to the front by maintaining order """

num=input().split(",")
print(num)
res=[]
for i in num:
    if i!="0":
        res.append(i)
a=len(num)-len(res)
for i in range(0,a):
    res.append("0")
print(res)


