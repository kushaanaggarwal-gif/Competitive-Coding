total_count = int(input("How many candidates? "))

candidates = []
for i in range(total_count):
    val = int(input("Enter candidate: "))
    candidates.append(val)

target = int(input("Enter target: "))

result = []

def solve(start, remaining, current):
    if remaining == 0:
        result.append(list(current))
        return
    for i in range(start, len(candidates)):
        if candidates[i] <= remaining:
            solve(i, remaining - candidates[i], current + [candidates[i]])

solve(0, target, [])

print("Combinations:", result)