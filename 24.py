IS_TEST = False

TEST_DICT = {
	True: {
		'filename': 'input24-test.txt'
	},
	False: {
		'filename': 'input24.txt'
	}
}

with open(TEST_DICT[IS_TEST]['filename'], encoding='utf-8') as f:
	data = f.read().splitlines()
	rows = len(data) - 2
	cols = len(data[0]) - 2
	mazes = [{}]
	blizzard_to_dir = {
		'>': (0, 1),
		'<': (0, -1),
		'^': (-1, 0),
		'v': (1, 0)
	}

	for i in range(1, len(data) - 1):
		for j in range(1, len(data[1]) - 1):
			row = i - 1
			col = j - 1
			if data[i][j] != ".":
				mazes[0][(row, col)] = [data[i][j]]
		

def step_maze(current_maze):
	next_maze = {}
	for point in current_maze.keys():
		for blizzard in current_maze[point]:
			next_row = point[0] + blizzard_to_dir[blizzard][0]
			next_col = point[1] + blizzard_to_dir[blizzard][1]
			if (next_row < 0) or (next_row >= rows):
				next_row = next_row % rows
			if (next_col < 0) or (next_col >= cols):
				next_col = next_col % cols

			if (next_row, next_col) in next_maze.keys():
				next_maze[(next_row, next_col)].append(blizzard)
			else:
				next_maze[(next_row, next_col)] = [blizzard]

	return next_maze

def expand_possibilities(current_possibilities, next_maze):
	next_possibilities = set()
	movements = {
		(0, 0),
		(0, 1),
		(0, -1),
		(1, 0),
		(-1, 0)
	}

	for p in current_possibilities:
		for m in movements:
			next_row = p[0] + m[0]
			next_col = p[1] + m[1]
			
			# you can always hide at the beginning of the maze
			if (next_row == -1) and (next_col == 0):
				next_possibilities.add((next_row, next_col))
				continue

			# you can always hide at the end of the maze
			if (next_row == rows) and (next_col == cols - 1):
				next_possibilities.add((next_row, next_col))
				continue

			# can't add if there's a blizzard
			if (next_row, next_col) in next_maze:
				continue

			if (next_row < 0) or (next_row >= rows):
				continue

			if (next_col < 0) or (next_col >= cols):
				continue

			next_possibilities.add((next_row, next_col))

	return next_possibilities

def solve_part_1():
	possibilities = [{(-1, 0)}]

	while True:
		mazes.append(step_maze(mazes[-1]))
		possibilities.append(expand_possibilities(
			possibilities[-1], mazes[-1]))

		if (rows, cols - 1) in possibilities[-1]:
			break

	print(len(possibilities) - 1)

def solve_part_2():
	possibilities = [{(rows, cols - 1)}]

	# takes 295 steps
	for i in range(295):
		mazes.append(step_maze(mazes[-1]))

	while True:
		mazes.append(step_maze(mazes[-1]))
		possibilities.append(expand_possibilities(
			possibilities[-1], mazes[-1]))

		if (-1, 0) in possibilities[-1]:
			break

	print(len(mazes) - 1)

def solve_part_2b():
	possibilities = [{(-1, 0)}]

	# takes 556 steps
	for i in range(556):
		mazes.append(step_maze(mazes[-1]))

	while True:
		mazes.append(step_maze(mazes[-1]))
		possibilities.append(expand_possibilities(
			possibilities[-1], mazes[-1]))

		if (rows, cols - 1) in possibilities[-1]:
			break

	print(len(mazes) - 1)


solve_part_2b()
