total_count = int(input("How many numbers? "))

nums = []
for i in range(total_count):
    val = int(input("Enter number: "))
    nums.append(val)

slow = nums[0]
fast = nums[0]

while True:
    slow = nums[slow]
    fast = nums[nums[fast]]
    if slow == fast:
        break

slow = nums[0]
while slow != fast:
    slow = nums[slow]
    fast = nums[fast]

print("Duplicate number:", slow)