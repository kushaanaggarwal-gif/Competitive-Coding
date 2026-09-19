num = int(input("Enter a number: "))

while num >= 10:
    total = 0
    while num > 0:
        total = total + (num % 10)
        num = num // 10
    num = total

print("Result:", num)