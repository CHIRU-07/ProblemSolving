# 1) In this challenge, the user enters a string and a substring. 
# You have to print the number of times that the substring occurs in the given string.
# String traversal will take place from left to right, not from right to left.
# input: 
# ABCDCDC
# CDC
# Output:
# 2

'''str=input("Enter a string: ")
substr=input("Enter a substring: ")
count,i,j=0,0,0
while i<=(len(str)-1):
    if(str[i]==substr[j]):
        i+=1
        if(i==len(str)):
            break
        j+=1
        if(j==len(substr)-1 and str[i]==substr[j]):
           count+=1
           print(str[i],substr[j])
           j=0

    else:
        i+=1
        j=0
print(f"\"{substr}\" occurs {count} times in \"{str}\"")'''


# Method 2 
str1=input("Enter the string: ")
substr1=input("Enter the substring: ")
count=0
for i in range(0,len(str1)):
    if(str1[i]==substr1[0]):
        if(str1[i:i+len(str1)]==substr1):
            count+=1
print(count)
        
