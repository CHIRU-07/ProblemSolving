"""TO print matrix """
# row,col=[int(i) for i in input().split()]
# res=[]

# for i in range(1,row+1):
#     print("Enter row",i,"elements")
#     ele=[int(i) for i in input().split()]
#     res.append(ele)
# print(res)
# for i in range(0,len(res)):
#     str1=""
#     for j in range(0,row):
#         str1=str1+str(res[i][j])+" "
#     print(str1)


"""To print transpose of a matrix"""
# row,col=[int(i) for i in input().split()]
# res=[]
# for i in range(1,row+1):
#      print("Enter row",i,"elements")
#      ele=[int(i) for i in input().split()]
#      res.append(ele)
# print(res)
# for i in range(0,row):
#      str1=""
#      for j in range(0,col):
#           str1=str1+str(res[j][i])+" "
#      print(str1)

"""To print outer elements"""
# row,col=[int(i) for i in input().split()]
# res=[]
# for i in range(1,row+1):
#      print("Enter row",i,"elements")
#      ele=[int(i) for i in input().split()]
#      res.append(ele)
# print(res)
# for i in range(0,len(res)):
#      str1=""
#      for j in range(0,len(res[i])):
#           if i==0 or j==0 or i==row-1 or j==col-1:
#                str1=str1+str(res[i][j])+" "
#           else:
#                str1=str1+"  "
#      print(str1)

"""To print sum of the diagonal elements in the matrix"""
# row,col=[int(i) for i in input().split()]
# res=[]
# sum=0
# for i in range(1,row+1):
#      print("Enter row",i,"elements")
#      ele=[int(i) for i in input().split()]
#      res.append(ele)
# print(res)
# for i in range(0,row):
#      for j in range(0,col):
#           if(i==j or i+j==row-1 ):
#                sum+=res[i][j]
# print(sum)


"""input: [[1,2,3],[4,3,2],[10,5,4]]
output: 
row1 max: 3
row2 max: 4
row3 max: 10"""
# row,col=[int(i) for i in input().split()]
# res=[]
# max1=0
# for i in range(1,row+1):
#      print("Enter row",i,"elements")
#      ele=[int(i) for i in input().split()]
#      res.append(ele)
# print(res)
# for i in range(0,row):
#      for j in range(0,col):
#         if(res[i][j]>max1):
#             max1=res[i][j]
#      print("Max element in the",i,"row is",max1)
