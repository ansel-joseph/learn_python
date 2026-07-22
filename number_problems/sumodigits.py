a=int(input("Enter a number to find the sum of its digits: "))
sum=0
while a!=0:
    last_digit=a%10
    sum=sum+last_digit
    a=a//10
print(sum)
