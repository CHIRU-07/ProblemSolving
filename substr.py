# 1) In this challenge, the user enters a string and a substring. 
# You have to print the number of times that the substring occurs in the given string.
# String traversal will take place from left to right, not from right to left.
# input: 
# ABCDCDC
# CDC
# Output:
# 2

str=input("Enter a string: ")
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
print(f" \"{substr}\" occurs {count} times in \"{str}\"")
        
