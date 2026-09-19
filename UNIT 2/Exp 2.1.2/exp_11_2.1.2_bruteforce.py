total_count = int(input("How many candidates? "))

candidates = []
for i in range(total_count):
    val = int(input("Enter candidate: "))
    candidates.append(val)

target = int(input("Enter target: "))

result = []

def solve(remaining, current):
    if remaining == 0:
        sorted_combo = sorted(current)
        if sorted_combo not in result:
            result.append(sorted_combo)
        return
    if remaining < 0:
        return
    for c in candidates:
        solve(remaining - c, current + [c])

solve(target, [])

print("Combinations:", result)