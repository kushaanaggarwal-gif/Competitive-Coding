def D(nums, k):
    last_index = {}

    for i in range(n):
        if nums[i] in last_index:
            if i - last_index[nums[i]] <= k:
                return True

        last_index[nums[i]] = i

    return False

nums = []
print("Enter the number of elements:")
n = int(input())

print("Enter the elements:")
for i in range(n):
    nums.append(int(input()))

k = int(input("enter k:"))

print(D(nums, k))