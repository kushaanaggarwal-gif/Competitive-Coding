num = int(input("Enter a number: "))

if num == 0:
    ans = 0
else:
    ans = 1 + (num - 1) % 9

print("Result:", ans)