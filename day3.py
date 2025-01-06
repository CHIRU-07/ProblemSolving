'''WAP to print max and min digits in the number'''
# # user=input("Enter a number :")
# maxi=user[0]
# mini=user[0]
# for i in range(0,len(user)):
#     if maxi<user[i]:
#              maxi=user[i]
#     if user[i] <mini:
#         mini=user[i]
# print("The max digit and min digit in {} is {} ,{}".format(user,maxi,mini))
# print("The max even digit in the {} is {}".format(user,maxi))


""" WAP to print max even digit in a number"""
# user=input("Enter a number :")
# maxi=user[1]
# mini=user[1]
# for i in range(1,len(user),2):
#     if maxi<user[i]:
#         maxi=user[i]
# print("The max digit in even digits in the {} is {}".format(user,maxi))


"""WAP to print sum of max and min digit in a number by using while loop"""
user=input("Enter a number :")
maxi=user[0]
mini=user[0]
i=0
while(i<len(user)):
    if user[i]>maxi:
        maxi=user[i]
    i=i+1
print("The max digit in the {} by using while loop is {}".format(user,maxi))