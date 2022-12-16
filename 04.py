import re

with open('input04.txt', encoding='utf-8') as f:
	data = f.read().splitlines()

def is_fully_contained(row):
	start_1, end_1, start_2, end_2 = map(lambda s: int(s), re.split(',|-', row))
	return ((start_1 <= start_2) & (end_1 >= end_2)) | \
		((start_1 >= start_2) & (end_1 <= end_2))

def is_partially_contained(row):
	start_1, end_1, start_2, end_2 = map(lambda s: int(s), re.split(',|-', row))
	return (end_1 >= start_2) & (end_2 >= start_1)


def solve_part_1():
	results = list(filter(lambda d: is_fully_contained(d), data))
	print(len(results))

def solve_part_2():
	results = list(filter(lambda d: is_partially_contained(d), data))
	print(len(results))

solve_part_2()
