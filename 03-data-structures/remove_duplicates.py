ages = [10, 5, 4, 5, 2, 1, 5]

unique = sorted(set(ages))
print(unique)

# doing it without set, keeping the original order
seen = []
for age in ages:
    if age not in seen:
        seen.append(age)
print(seen)
