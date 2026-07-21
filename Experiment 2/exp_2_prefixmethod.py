arr = []
print("Enter the number of elements:")
n = int(input())
answer = [1] * n
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

prefix = [1]
for i in range(1, n):
    prefix.append(prefix[i - 1] * arr[i - 1])

suffix = [1] * n
for i in range(n - 2, -1, -1):
    suffix[i] = suffix[i + 1] * arr[i + 1]

for i in range(n):
    answer[i] = prefix[i] * suffix[i]

print(answer)


