matrix = [[0, 5, 7, 2],
          [8, 9, 4, 5],
          [4, 5, 5, 1],
          ["Mario", "Lugio", "Peach", "Zelda"]]
print(matrix[3][2])

nameList = ["Mario", "Lugio", "Peach", "Zelda", "Mario", "Lugio",
            "Peach", "Zelda", "Frida", "Mario", "Lugio", "Peach", "Zelda"]

name_counts = {}
for name in nameList:
    if name in name_counts:
        name_counts[name] += 1
    else:
        name_counts[name] = 1

for name, count in name_counts.items():
    if count > 2:
        print(f"{name} appears {count} times.")

a, b, c, d, *other, e = [1, 2, 3, 4, 5, 5, 5, 7, 7,
                         7, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
other = [x for x in other if x is not None]

print(a)
print(b)
print(c)
print(d)
print(other)
print(e)
print(set(other))
