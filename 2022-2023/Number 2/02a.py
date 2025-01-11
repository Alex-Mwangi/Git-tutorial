

numbers = [1, 2, 3, 4, 5, 5, 6]

counts = {}

for num in numbers:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1

sorted_counts = sorted(counts.items())

for num, counts in sorted_counts:
    plural = 'times' if counts > 1 else 'time'
    print(f'{num} occurs {counts} {plural}')