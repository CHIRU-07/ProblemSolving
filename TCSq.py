"""1  Problem Statement – Given a string S(input consisting) of '*' and '#'. 
The length of the string is variable. The task is to find the minimum number of '*' or '#' to make it a valid string. 
The string is considered valid if the number of '*' and '#' are equal. The '*' and '#' can be at any position in the string.
Note : The output will be a positive or negative integer based on number of '*' and '#' in the input string.

(*>#): positive integer
(#>*): negative integer
(#=*): 0
Example 1:
Input 1:

###***   -> Value of S
Output :

0   → number of * and # are equal"""

# str=input("Enter a string: ")
# sum1,sum2=0,0
# for i in str:
#     if (i=="#"):
#         sum1+=1
#     elif (i=="*"):
#         sum2+=1
# if(sum1==sum2):
#     print("0 --> Number of * and # are equal")
# elif sum1>sum2:
#     print("-1 --> Number of * are less than number of # ")
# elif sum1<sum2:
#     print("1 --> Number of * are greater than number of # ")


""" 2  Given an integer array Arr of size N the task is to find the count of elements whose value is greater than all of its prior elements.
Note : 1st element of the array should be considered in the count of the result.

For example,
Arr[]={7,4,8,2,9}
As 7 is the first element, it will consider in the result.
8 and 9 are also the elements that are greater than all of its previous elements.
Since total of  3 elements is present in the array that meets the condition.
Hence the output = 3.
Example 1:

Input 
5 -> Value of N, represents size of Arr
7-> Value of Arr[0]
4 -> Value of Arr[1]
8-> Value of Arr[2]
2-> Value of Arr[3]
9-> Value of Arr[4]

Output :
3

Example 2:
5   -> Value of N, represents size of Arr
3  -> Value of Arr[0]
4 -> Value of Arr[1]
5 -> Value of Arr[2]
8 -> Value of Arr[3]
9 -> Value of Arr[4]

Output : 
5"""

# arr=[int(i) for i in input("Enter a number: ").split()]
# print(arr)
# sum1=1
# for i in range(0,len(arr)-1):
#     if(arr[i+1]>arr[i]):
#         sum1+=1
# print("The total number of elements that are greater than its before element is :",sum1)


'''3)  A parking lot in a mall has RxC number of parking spaces. Each parking space will either be  empty(0) or full(1). 
The status (0/1) of a parking space is represented as the element of the matrix. The task is to find index of the prpeinzta row(R) 
in the parking lot that has the most of the parking spaces full(1).

Note :
RxC- Size of the matrix
Elements of the matrix M should be only 0 or 1.

Example 1:
Input :
3   -> Value of R(row)
3    -> value of C(column)
[0 1 0 1 1 0 1 1 1] -> Elements of the array M[R][C] where each element is separated by new line.
Output :
3  -> Row 3 has maximum number of 1's

Example 2:
input :
4 -> Value of R(row)
3 -> Value of C(column)
[0 1 0 1 1 0 1 0 1 1 1 1] -> Elements of the array M[R][C]
Output :
4  -> Row 4 has maximum number of 1's'''