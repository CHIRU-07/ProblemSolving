"""Right rotation method 1 long method -more compile time"""
# arr=input().split()
# k=int(input("Enter the number to rotate the array: "))

# for i in range(k):
#     x=arr[-1]
#     for j in range(len(arr)-2,-1,-1):
#         arr[j+1]=arr[j]
#     arr[0]=x
# print(arr)

"""Right rotation method 2- short method less compile time"""
# arr=input().split()
# k=int(input("Enter the number to rotate the array: "))
# def rev(x,y):
#     while(x<y):
#         arr[x],arr[y]=arr[y],arr[x]
#         x,y=x+1,y-1
# k=k%len(arr)
# rev(0,len(arr)-1)
# rev(0,k-1)
# rev(k,len(arr)-1)
# print(arr)




"""Left rotation."""
# arr=input().split()
# k=int(input("Enter the number to rotate the array: "))
 
# for i in range(k):
#     x=arr[0]
#     for j in range(0,len(arr)-1):
#         arr[j]=arr[j+1]
#     arr[-1]=x
# print(arr)

arr=input().split()
k=int(input("Enter the number to rotate the array: "))

def rev(x,y):
    while(x<y):
        arr[x],arr[y]=arr[y],arr[x]
        x,y=x+1,y-1
k=k%len(arr)
rev(0,len(arr)-1)
rev(0,k)
rev(k+1,len(arr)-1)
print(arr)