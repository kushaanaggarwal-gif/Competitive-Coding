answer = []
arr = []
print("enter array size:")
n = int(input())
print("enter array elements:")
for i in range(n):
    arr.append(int(input()))

for i in range(n):
    product = 1
    for j in range(n):
        if i != j:
            product = product*arr[j]
    answer.append(product)

print(answer)
