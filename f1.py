s2 = "sister"

dup = []

for value in s2:
    if s2.count(value) > 1:
        if value not in dup:
            dup.append(value)

print(dup)
