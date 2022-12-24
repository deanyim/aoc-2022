IS_TEST = False

TEST_DICT = {
	True: {
		'filename': 'input10-test.txt'
	},
	False: {
		'filename': 'input10.txt'
	}
}

with open(TEST_DICT[IS_TEST]['filename'], encoding='utf-8') as f:
	data = f.read().splitlines()

def get_cycle_values():
	cycle_values = [1]
	for instruction in data:
		cycle_values.append(cycle_values[-1])
		if instruction == 'noop':
			pass
		else:
			summand = int(instruction.split(' ')[1])
			cycle_values.append(cycle_values[-1] + summand)
	return cycle_values

def solve_part_1():
	cycle_values = get_cycle_values()
	cycle_indices = [20, 60, 100, 140, 180, 220]
	print(sum([i * cycle_values[i-1] for i in cycle_indices]))
	print(len(cycle_values))

def solve_part_2():
	cycle_values = get_cycle_values()
	for i in range(6):
		output = ""
		for j in range(1, 41):
			pixel_index = i * 40 + j - 1
			if abs(cycle_values[pixel_index] - j + 1) <= 1:
				output += "#"
			else:
				output += "."
		print(output)

solve_part_2()
