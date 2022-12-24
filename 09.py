IS_TEST = False

TEST_DICT = {
	True: {
		'filename': 'input09-test.txt'
	},
	False: {
		'filename': 'input09.txt'
	}
}

with open(TEST_DICT[IS_TEST]['filename'], encoding='utf-8') as f:
	data = f.read().splitlines()
	direction_map = {
		'R': (1, 0),
		'L': (-1, 0),
		'U': (0, 1),
		'D': (0, -1)
	}

def get_tail_pos(new_head_pos, tail_pos):
	x_distance = new_head_pos[0] - tail_pos[0]
	y_distance = new_head_pos[1] - tail_pos[1]

	if (abs(x_distance) <= 1) and (abs(y_distance) <= 1):
		pass

	elif (abs(x_distance) == 2) and (abs(y_distance) == 0):
		x_sign = int(abs(x_distance) / x_distance)
		tail_pos = (
			tail_pos[0] + x_sign,
			tail_pos[1]
		)

	elif (abs(x_distance) == 0) and (abs(y_distance) == 2):
		y_sign = int(abs(y_distance) / y_distance)
		tail_pos = (
			tail_pos[0],
			tail_pos[1] + y_sign
		)

	else:
		x_sign = int(abs(x_distance) / x_distance)
		y_sign = int(abs(y_distance) / y_distance)
		tail_pos = (
			tail_pos[0] + x_sign,
			tail_pos[1] + y_sign
		)

	return tail_pos

def solve_part_1():
	head_pos = (0, 0)
	tail_pos = (0, 0)
	tail_positions = {tail_pos}

	for d in data:
		direction, count = d.split(' ')
		for i in range(int(count)):
			# move head
			head_pos = (
				head_pos[0] + direction_map[direction][0],
				head_pos[1] + direction_map[direction][1]
			)
			# move tail
			tail_pos = get_tail_pos(head_pos, tail_pos)
			tail_positions.add(tail_pos)

	print(len(tail_positions))

def solve_part_2():
	head_pos = (0, 0)
	all_positions = []
	for i in range(10):
		all_positions.append([head_pos])

	for d in data:
		direction, count = d.split(' ')
		for i in range(int(count)):
			head_pos = (
				head_pos[0] + direction_map[direction][0],
				head_pos[1] + direction_map[direction][1]
			)
			all_positions[0].append(head_pos)

	for tail_number in range(1, 10):
		for prev_tail_pos in all_positions[tail_number - 1][1:]:
			tail_pos = all_positions[tail_number][-1]
			all_positions[tail_number].append(
				get_tail_pos(
					prev_tail_pos,
					tail_pos
				))

	print(len(list(set(all_positions[9]))))

solve_part_2()
