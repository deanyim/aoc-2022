IS_TEST = True

TEST_DICT = {
	True: {
		'filename': 'inputXX-test.txt'
	},
	False: {
		'filename': 'inputXX.txt'
	}
}

with open(TEST_DICT[IS_TEST]['filename'], encoding='utf-8') as f:
	data = f.read().splitlines()

def solve_part_1():
	pass

def solve_part_2():
	pass
