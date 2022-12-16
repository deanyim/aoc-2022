import itertools

from functools import reduce

with open('input03.txt', encoding='utf-8') as f:
	data = f.read().splitlines()

def split_rucksack(r):
	midpoint = int(len(r) / 2)
	return (r[:midpoint], r[midpoint:])

def rucksack_intersection(r1, r2):
	return set([*r1]).intersection(set([*r2]))

def group_intersection(group):
	sets = map(lambda r: set(r), group)
	return reduce(rucksack_intersection, sets)


def item_to_pri(i):
	i = list(i)[0]
	if ord(i) >= 97:
		return ord(i) - 96
	if ord(i) < 97:
		return ord(i) - 38

def solve_part_1():
	rucksack_intersections = map(
		lambda r: rucksack_intersection(*split_rucksack(r)), data)
	return sum(map(lambda i: item_to_pri(i), rucksack_intersections))

def grouplen(sequence, chunk_size):
    return list(zip(*[iter(sequence)] * chunk_size))

def solve_part_2():
	groups = grouplen(data, 3)
	group_intersections = map(lambda g: group_intersection(g), groups)
	return sum(map(lambda i: item_to_pri(i), group_intersections))


print(solve_part_2())