'''1) Problem Statement: You are given an integer. Your task is to replace all the zeros in the integer with ones and all the ones with zeroes.

Examples:
Example 1:
Input: N = 502113
Output: 512003'''


"""Method 1"""
# num=int(input("Enter a number: "))
# str1=str(num)
# str1=str1.replace("0","1")
# print(str1)

"""Method 2"""
# num=int(input("Enter a number: "))
# str1=str(num)
# str2=""
# for i in str1:
#     if(i=="0"):
#         i="1"
#         str2+=i
#     else:
#         str2+=i

# print(str2)



"""2) Problem Statement: Check if the number is a Harshad(or Niven) number or not.

Examples:

Example 1:
Input: 378
Output: Yes it is a Harshad number.
Explanation: 3+7+8=18. 378 is divisible by 18. Therefore 378 is a harshad number.

Example 2:
Input: 379
Output: No
 it is not a Harshad number.
Explanation: 3+7+9=19. 379 is not divisible by 19. Therefore 379 is a harshad number."""

# Num=int(input("Enter a number: "))
# Num1=Num
# digits,sum=0,0
# for i in range(0,len(str(Num))):
#     digits=Num1%10
#     Num1=Num1//10
#     sum+=digits
# print("sum of the digits:",sum)
# res=True if Num%sum==0 else False
# if res:
#    print("{} is a harshad Number".format(Num))
# else:
#     print("{} Not a Harshad Number".format(Num))