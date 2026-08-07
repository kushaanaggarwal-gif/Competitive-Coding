def search(arr, key):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == key:
            return True

        if arr[left] == arr[mid]:
            left += 1
            continue

        if arr[left] <= arr[mid]:
            if arr[left] <= key <= arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if arr[mid] <= key <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1

    return False


n = int(input("n: "))

arr = list(map(int, input("Elements: ").split()))

key = int(input("Target: "))

if len(arr) != n:
    print("Invalid input")
else:
    if search(arr, key):
        print("Found")
    else:
        print("Not Found")