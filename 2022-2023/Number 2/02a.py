# Step 1: Initialize an empty dictionary to store counts
counts = {}

# Step 2: List of numbers (example)
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# Step 3: Count occurrences
for num in numbers:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1

# Step 4: Sort the dictionary by keys
sorted_counts = sorted(counts.items())

# Step 5: Print the results
for num, count in sorted_counts:
    plural = "time" if count == 1 else "times"
    print(f"{num} occurs {count} {plural}")
