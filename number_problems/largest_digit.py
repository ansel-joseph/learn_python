a = int(input("Enter numbers to find the largest: "))
largest = 0
while a != 0:
    last_digit = a % 10
    if(last_digit>largest):
        largest=last_digit
    a=a//10
print(largest)
