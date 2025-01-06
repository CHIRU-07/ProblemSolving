# sum of non primes in number
numbers=input("Enter a number :")
div=0
sum=0
for i in numbers:
    for j in range(1,10):
        if(int(i)%j==0):
            div+=1
    if(div>2):
        sum=int(i)+sum
    div=0
print(sum)      

    
      
      