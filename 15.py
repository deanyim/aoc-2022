import re

IS_TEST = False

TEST_DICT = {
	True: {
		'filename': 'input15-test.txt',
		'row': 10,
		'max_val': 20
	},
	False: {
		'filename': 'input15.txt',
		'row': 2000000,
		'max_val': 4000000
	}
}

with open(TEST_DICT[IS_TEST]['filename'], encoding='utf-8') as f:
	data = f.read().splitlines()

def get_elimination_points(sensor, beacon):
	# don't forget to exclude the beacon
	elimination_points = set()
	distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
	for x in range(sensor[0] - distance, sensor[0] + distance + 1):
		y = TEST_DICT[IS_TEST]['row']
		if (x, y) == beacon:
			continue
		if abs(sensor[0] - x) + abs(sensor[1] - y) > distance:
			continue
		elimination_points.add((x, y))
	return elimination_points



def solve_part_1():
	# approach: create a set of pts where the beacon can't be
	# figure out how many of those pts are in row y

	all_elimination_points = set()
	for row in data:
		print(row)
		values = re.findall(r'\d+|-\d+', row)
		sensor = (int(values[0]), int(values[1]))
		beacon = (int(values[2]), int(values[3]))
		all_elimination_points.update(
			get_elimination_points(sensor, beacon))
	return len(list(filter(lambda p: p[1] == TEST_DICT[IS_TEST]['row'], all_elimination_points)))

def solve_part_2():
	max_val = TEST_DICT[IS_TEST]['max_val']
	x_plus_y = set(range(2 * max_val + 1))
	x_minus_y = set(range(-max_val, max_val + 1))

	x_plus_y_ranges = set()
	x_minus_y_ranges = set()

	ranges = set()

	for row in data:
		values = re.findall(r'\d+|-\d+', row)
		sensor = (int(values[0]), int(values[1]))
		beacon = (int(values[2]), int(values[3]))
		distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])

		x_plus_y_start = sensor[0] + sensor[1] - distance
		x_plus_y_end = sensor[0] + sensor[1] + distance
		x_minus_y_start = sensor[0] - sensor[1] - distance
		x_minus_y_end = sensor[0] - sensor[1] + distance

		# x+y, then x-y
		ranges.add(((x_plus_y_start, x_plus_y_end), (x_minus_y_start, x_minus_y_end)))
	
	for x_plus_y in range(2 * max_val + 1):
		if (x_plus_y % 1000000) == 0:
			print(x_plus_y)

		span = 20 - abs(20 - x_plus_y)
		x_minus_y_values = set(range(-1 * span, span + 1))
		x_minus_y_start = -1 * span
		x_minus_y_end = span

		if IS_TEST:
			print(x_plus_y)
			print(x_minus_y_start, x_minus_y_end)

		x_minus_y_ranges = []
		for r in ranges:
			x_plus_y_start = r[0][0]
			x_plus_y_end = r[0][1]
			x_minus_y_start = r[1][0]
			x_minus_y_end = r[1][1]

			if (x_plus_y_start <= x_plus_y) and (x_plus_y <= x_plus_y_end):
				# I have to find a better way of combining the sets.
				x_minus_y_ranges.append((x_minus_y_start, x_minus_y_end))
			
		x_minus_y_ranges = sorted(x_minus_y_ranges)
		max_x_minus_y = x_minus_y_ranges[0][1]
		for i in range(len(x_minus_y_ranges) - 1):
			max_x_minus_y = max(max_x_minus_y, x_minus_y_ranges[i][1])
			if ((x_minus_y_ranges[i+1][0] - max_x_minus_y) > 1):
				print(x_plus_y, max_x_minus_y + 1)

		'''
		if x_minus_y_values != set():
			print(x_plus_y, x_minus_y_values)
		'''


	'''
	for row in data:
		print(row)

		for i in range(x_plus_y_start, x_plus_y_end + 1):
			if i in x_plus_y:
				x_plus_y.remove(i)
		for i in range(x_minus_y_start, x_minus_y_end + 1):
			if i in x_minus_y:
				x_minus_y.remove(i)

		print("x+y", x_plus_y)
		print("x-y", x_minus_y)
	'''
	pass

# solve_part_2()

x = (6652075 + 159049) / 2
y = 6652075 - x
print(x * 4000000 + y)