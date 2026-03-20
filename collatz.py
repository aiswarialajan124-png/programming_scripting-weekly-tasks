# Ask user for positie integer
num = int(input("Enter a positive integer: "))

# Keep going until number becomes 1
while num != 1:
    print(num, end=" ")

    if num % 2 == 0:
        num = num // 2
    else:
        num = num * 3 + 1

# Print final 1
print(1)