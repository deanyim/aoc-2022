from functools import reduce

with open('input01.txt', encoding='utf-8') as f:
	data = f.readlines()

elves = [[]]

for d in data:
	if d == '\n':
		elves.append([])
	else:
		elves[-1].append(int(d))

calorie_counts = sorted(map(lambda backpack: sum(backpack), elves))

print(calorie_counts[-1])
print(sum(calorie_counts[-3:]))