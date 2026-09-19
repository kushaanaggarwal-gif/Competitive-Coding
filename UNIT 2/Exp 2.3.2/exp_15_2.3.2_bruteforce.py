total_count = int(input("How many numbers? "))

nums = []
for i in range(total_count):
    val = int(input("Enter number: "))
    nums.append(val)

seen = []
duplicate = -1

for x in nums:
    if x in seen:
        duplicate = x
        break
    seen.append(x)

print("Duplicate number:", duplicate)