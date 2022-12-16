with open('input06.txt', encoding='utf-8') as f:
	data = f.read().splitlines()

def get_marker_location(buffer, num_distinct):
	n_tuples = [(i + num_distinct, set(buffer[i:i+num_distinct]))
		for i in range(len(buffer) - num_distinct + 1)]
	return list(filter(lambda t: len(t[1]) == num_distinct, n_tuples))[0][0]

def solve_part_1():
	return get_marker_location(data[0], 4)

def solve_part_2():
	return get_marker_location(data[0], 14)

print(solve_part_2())
