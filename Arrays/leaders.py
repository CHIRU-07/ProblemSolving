# leader
"""16 17 4 3 5 2"""
num=[int(i) for i in input().split()]

leaders=[]
x=len(num)
max_from_right=0
for i in range(x-1,-1,-1):
    if(num[i]>=max_from_right):
        leaders.append(num[i])
        max_from_right=num[i]
print(leaders[::-1])
