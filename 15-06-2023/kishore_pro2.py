d = {"don": 100, "sunny": 200, "sai": 1, "shannu": 20}
total = 0

for value in d.values():
    total += value

print(total)

#or

d = {"don": 100, "sunny": 200, "sai": 1, "shannu": 20}
total = sum(d.values())
print(total)
