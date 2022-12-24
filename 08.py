IS_TEST = False

TEST_DICT = {
	True: {
		'filename': 'input08-test.txt'
	},
	False: {
		'filename': 'input08.txt'
	}
}

with open(TEST_DICT[IS_TEST]['filename'], encoding='utf-8') as f:
	data = f.read().splitlines()
	data = [[int(s) for s in list(row)] for row in data]

def get_lines_of_sight(i, j):
	# return [trees to the left, to the right, above, below]
	dir_vectors = [
		(1, 0),
		(-1, 0),
		(0, 1),
		(0, -1)
	]
	lines_of_sight = []
	for v in dir_vectors:
		intervening_trees = []
		pos_i, pos_j = i, j
		while True:
			pos_i += v[0]
			pos_j += v[1]
			if (pos_i < 0) or (pos_j < 0) or (pos_i >= len(data)) or (pos_j >= len(data[i])):
				break
			intervening_trees.append(data[pos_i][pos_j])
		lines_of_sight.append(intervening_trees)
	return lines_of_sight

def is_tree_visible(tree_height, lines_of_sight):
	visible_lines = []
	for l in lines_of_sight:
		blocked = False
		for t in l:
			if t >= tree_height:
				blocked = True
		visible_lines.append(blocked)

	return not min(visible_lines)

def get_scenic_score(i, j):
	scenic_score = 1
	tree_height = data[i][j]
	lines_of_sight = get_lines_of_sight(i, j)
	for l in lines_of_sight:
		visible_trees = 0

		for t in l:
			visible_trees += 1
			if t >= tree_height:
				break

		scenic_score *= visible_trees
	return scenic_score

def solve_part_1():
	visible_trees = 0
	for i in range(len(data)):
		for j in range(len(data[i])):
			if is_tree_visible(data[i][j], get_lines_of_sight(i, j)):
				visible_trees += 1
	print(visible_trees)

def solve_part_2():
	scenic_scores = []
	for i in range(1, len(data) - 1):
		for j in range(1, len(data[i]) - 1):
			scenic_scores.append(get_scenic_score(i, j))
	print(max(scenic_scores))

solve_part_2()
# print(is_tree_visible(6, get_lines_of_sight(2, 0)))