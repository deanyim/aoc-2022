IS_TEST = True

TEST_DICT = {
	True: {
		'filename': 'input17-test.txt'
	},
	False: {
		'filename': 'input17.txt'
	}
}


with open(TEST_DICT[IS_TEST]['filename'], encoding='utf-8') as f:
	data = f.read().splitlines()
	conversion_table = {'>': 1, '<': -1}
	data = [conversion_table[d] for d in list(data[0])]


def is_collision(rocks, stopped_rocks):
	for rock in rocks:
		if rock[0] < 0:
			return True
		if rock[0] >= 7:
			return True
		if rock[1] < 0:
			return True
		if rock[1] < len(stopped_rocks):
			if (rock[1] == 0) and stopped_rocks == []:
				pass
			elif stopped_rocks[rock[1]][rock[0]] == 1:
				return True

	return False

def add_rock(rock, stopped_rocks):
	for r in rock:
		while r[1] >= len(stopped_rocks):
			stopped_rocks.append([0, 0, 0, 0, 0, 0, 0])
		if stopped_rocks[r[1]][r[0]] == 1:
			print ("Something's fucked")
		stopped_rocks[r[1]][r[0]] = 1
	return stopped_rocks

def feed_rock(stopped_rocks, shape, push_index):
	# for each rock, figure out the start position and the shape
	# start at the imaginary location of 2,len(stopped_rocks)+3

	start_x = 2
	start_y = len(stopped_rocks) + 3

	shapes = {
		0: [(0, 0), (1, 0), (2, 0), (3, 0)],
		1: [(1, 0), (0, 1), (1, 1), (1, 2), (2, 1)],
		2: [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
		3: [(0, 0), (0, 1), (0, 2), (0, 3)],
		4: [(0, 0), (0, 1), (1, 0), (1, 1)]
	}

	rock_points = [(start_x + p[0], start_y + p[1]) for p in shapes[shape]]

	while True:
		push_dir = data[push_index % len(data)]
		push_index += 1
		potential_rock_push = [(p[0] + push_dir, p[1]) for p in rock_points]
		if not is_collision(potential_rock_push, stopped_rocks):
			rock_points = potential_rock_push[:]

		potential_rock_fall = [(p[0], p[1] - 1) for p in rock_points]
		if is_collision(potential_rock_fall, stopped_rocks):
			break

		rock_points = potential_rock_fall[:]

	return (add_rock(rock_points, stopped_rocks), push_index)

def pretty_print(stopped_rocks):
	mapping = {0: " ", 1: "#"}
	for row in reversed(stopped_rocks):
		print("".join([mapping[v] for v in row]))
	print("-" * 7)
	print("")

def get_stopped_rocks(rocks, verbose_mode=False):
	push_index = 0
	stopped_rocks = []
	min_ratio = 1
	for i in range(rocks):
		(stopped_rocks, push_index) = feed_rock(stopped_rocks[:], i % 5, push_index)

		if (i > 1) & (verbose_mode):
			ratio = len(stopped_rocks) / i - 1.514285714288
			if abs(ratio) < min_ratio:
				print(i, ratio)
				min_ratio = abs(ratio)

	return stopped_rocks

def solve_part_1():
	print(len(get_stopped_rocks(2022)))

def solve_part_2():
	# test data repeats every 35 (after the first 35)
	# 60 high, then 53 each afterwards
	# real data repeats every 1710 (after the first 1710)

	# generate snapshots
	rocks = 30000
	snapshots = {}

	push_index = 0
	stopped_rocks = []
	min_ratio = 1
	for i in range(rocks):
		(stopped_rocks, push_index) = feed_rock(stopped_rocks[:], i % 5, push_index)
		snapshots[i + 1] = stopped_rocks

	for i in range(1, int(rocks / 15)):
		first_block = snapshots[i * 5]
		second_block = snapshots[2 * i * 5][len(first_block):]
		final_block = snapshots[3 * i * 5][len(first_block) + len(second_block):]
		if(second_block == final_block):
			print(i * 5)


def solve_part_2_b():
	count = 1000000000000
	period = 35
	first_height = len(get_stopped_rocks(period))
	next_height = len(get_stopped_rocks(2 * period)) - len(get_stopped_rocks(period))

	remainder = count % period
	first_batch_rocks = period + remainder
	next_batch_rocks = count - first_batch_rocks

	return len(get_stopped_rocks(first_batch_rocks)) + next_batch_rocks * next_height / period

print(solve_part_2_b())
