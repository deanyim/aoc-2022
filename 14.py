IS_TEST = False

TEST_DICT = {
	True: {
		'filename': 'input14-test.txt'
	},
	False: {
		'filename': 'input14.txt'
	}
}

with open(TEST_DICT[IS_TEST]['filename'], encoding='utf-8') as f:
	data = f.read().splitlines()

def turn_line_to_rock_points(line):
	rock_points = set()
	points = [p.split(",") for p in line.split(" -> ")]
	for i in range(len(points) - 1):
		start_x = int(points[i][0])
		start_y = int(points[i][1])
		end_x = int(points[i+1][0])
		end_y = int(points[i+1][1])

		if start_x == end_x:
			lo = min(start_y, end_y)
			hi = max(start_y, end_y)
			for y in range(hi - lo + 1):
				rock_points.add((start_x, lo + y))
		elif start_y == end_y:
			lo = min(start_x, end_x)
			hi = max(start_x,end_x)
			for x in range(hi - lo + 1):
				rock_points.add((lo + x, start_y))

	return rock_points

def place_sand(rock_points, void_threshold):
	# returns (x, y) for the next sand piece
	# or False if it falls below the void
	location_x, location_y = 500, 0
	is_falling = True
	is_in_void = False
	## void_threshold = max([x[1] for x in rock_points])

	while (is_falling) & (not is_in_void):
		if location_y > void_threshold:
			return False

		if (location_x, location_y + 1) not in rock_points:
			location_y += 1
		elif (location_x - 1, location_y + 1) not in rock_points:
			location_x -= 1
			location_y += 1
		elif (location_x + 1, location_y + 1) not in rock_points:
			location_x += 1
			location_y += 1
		else:
			return (location_x, location_y)

def solve_part_1():
	all_rock_points = set()
	[all_rock_points.update(turn_line_to_rock_points(l)) for l in data]
	starting_rock_points = len(all_rock_points)

	has_void_started = False
	while not has_void_started:
		sand_loc = place_sand(all_rock_points)
		if sand_loc == False:
			has_void_started = True
		else:
			all_rock_points.add(sand_loc)

	return len(all_rock_points) - starting_rock_points

def solve_part_2():
	all_rock_points = set()
	[all_rock_points.update(turn_line_to_rock_points(l)) for l in data]

	void_threshold = max([x[1] for x in all_rock_points])
	[all_rock_points.add((i, void_threshold + 2)) for i in range(-1000, 2000)]
	starting_rock_points = len(all_rock_points)

	sand_counter = 0
	is_starting_point_blocked = False
	while not is_starting_point_blocked:
		sand_loc = place_sand(all_rock_points, void_threshold + 2)
		all_rock_points.add(sand_loc)

		sand_counter += 1
		print(sand_counter)

		if sand_loc == (500, 0):
			is_starting_point_blocked = True

	return len(all_rock_points) - starting_rock_points

print(solve_part_2())