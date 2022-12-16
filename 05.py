import re

TEST_STACK_DATA = [
	['Z', 'N'],
	['M', 'C', 'D'],
	['P']
]

STACK_DATA = [
	['F', 'D', 'B', 'Z', 'T', 'J', 'R', 'N'],
	['R', 'S', 'N', 'J', 'H'],
	['C', 'R', 'N', 'J', 'G', 'Z', 'F', 'Q'],
	['F', 'V', 'N', 'G', 'R', 'T', 'Q'],
	['L', 'T', 'Q', 'F'],
	['Q', 'C', 'W', 'Z', 'B', 'R', 'G', 'N'],
	['F', 'C', 'L', 'S', 'N', 'H', 'M'],
	['D', 'N', 'Q', 'M', 'T', 'J'],
	['P', 'G', 'S']
]

TEST_DICT = {
	True: {
		'filename': 'input05-test.txt',
		'stacks': TEST_STACK_DATA
	},
	False: {
		'filename': 'input05.txt',
		'stacks': STACK_DATA
	}
}
IS_TEST = False

def move_crate(start, dest):
	start_index, dest_index = start - 1, dest - 1
	stacks[dest_index].append(stacks[start_index].pop())

def operate_crane(row):
	num_crates, start, dest = map(lambda s: int(s), re.split('move | from | to ', row)[1:])
	[move_crate(start, dest) for i in range(num_crates)]

def operate_crane_9001(row):
	num_crates, start, dest = map(lambda s: int(s), re.split('move | from | to ', row)[1:])
	start_index, dest_index = start - 1, dest - 1

	pop_index = len(stacks[start_index]) - num_crates
	for i in range(num_crates):
		stacks[dest_index].append(stacks[start_index].pop(pop_index))


with open(TEST_DICT[IS_TEST]['filename'], encoding='utf-8') as f:
	data = f.read().splitlines()
	stacks = TEST_DICT[IS_TEST]['stacks']

def solve_part_1():
	[operate_crane(r) for r in data]
	return ''.join([s[-1] for s in stacks])

def solve_part_2():
	[operate_crane_9001(r) for r in data]
	return ''.join([s[-1] for s in stacks])

print(solve_part_2())
