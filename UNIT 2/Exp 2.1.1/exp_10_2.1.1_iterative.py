user_input = input("Enter numbers: ")
nums = [int(x) for x in user_input.split()]

result = [[]]

for num in nums:
    new_subsets = []
    for subset in result:
        new_subsets.append(subset + [num])
    result = result + new_subsets

print("Subsets:", result)