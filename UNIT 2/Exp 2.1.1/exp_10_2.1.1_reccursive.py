user_input = input("Enter numbers: ")
nums = [int(x) for x in user_input.split()]

result = []

def solve(index, current):
    if index == len(nums):
        result.append(current)
        return
    solve(index + 1, current)
    solve(index + 1, current + [nums[index]])

solve(0, [])

print("Subsets:", result)