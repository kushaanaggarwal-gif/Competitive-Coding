def D(nums, k):
    window = set()

    for i in range(len(nums)):
        if nums[i] in window:
            return True

        window.add(nums[i])

        if len(window) > k:
            window.remove(nums[i - k])

    return False

n = int(input("Enter size of array: "))

nums = []
for i in range(n):
    num = int(input())
    nums.append(num)

k = 3

print(D(nums, k))