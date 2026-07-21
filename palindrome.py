a = int(input("Enter a number to check if it is a palindrome: "))
temp = a
rev = 0
while a!=0:
    last_digit = a%10
    rev= (rev*10)+last_digit
    a=a//10

if(rev==temp):
    print("Palindrome")
else:
    print("Not Palindrome")
