#searching similar elements in a list by brute force method

arr = []
print("Enter the number of elements:")
n = int(input())
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

for i in range(n):
    for j in range(i + 1, n):
        if arr[i] == arr[j]:
            print("TRUE")
