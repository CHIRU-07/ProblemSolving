"""Method 1"""
list=input().split()
uni,dup="",""
l1=[]
for i in list:
    if i not in l1:
        l1.append(i)

for i in l1:
    x=list.count(i)
    if x==1:
        uni+=i+" "
    else:
        dup+=i+" "
print("Duplicates are : ",dup)
print("Uniques are : ",uni)


