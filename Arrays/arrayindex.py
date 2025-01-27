arr=[int(i) for i in input("Enter a number: ").split() ]
rank=[]
s_arr=arr.copy()
s_arr.sort()
for i in range(0,len(arr)):
    a=(s_arr.index(arr[i]))+1
    rank.append(a)
print(rank)
    


