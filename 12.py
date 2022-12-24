IS_TEST = False

TEST_DICT = {
	True: {
		'filename': 'input12-test.txt'
	},
	False: {
		'filename': 'input12.txt'
	}
}

def find_start_and_end():
	for i in range(len(data)):
		start_index = data[i].find('S')
		if start_index != -1:
			start = (i, start_index)

		end_index = data[i].find('E')
		if end_index != -1:
			end = (i, end_index)

	return (start, end)

with open(TEST_DICT[IS_TEST]['filename'], encoding='utf-8') as f:
	data = f.read().splitlines()
	start, end = find_start_and_end()
	cache = {
		start: 0
	}

def get_altitude(point):
	alt_letter = data[point[0]][point[1]]
	if alt_letter == 'S':
		return 1
	elif alt_letter == 'E':
		return 26
	return ord(alt_letter) - 96

def get_min_steps(point):
	if point in cache.keys():
		return cache[point]

	adjacencies = [(1, 0), (-1, 0), (0, 1), (0, -1)]
	adjacent_points = [(point[0] + a[0], point[1] + a[1]) for a in adjacencies]
	current_altitude = get_altitude(point)
	points_to_test = []

	for p in adjacent_points:
		if (p[0] < 0) or (p[0] >= len(data[0])):
			continue
		if (p[1] < 0) or (p[1] >= len(data[1])):
			continue

		if (current_altitude - get_altitude(p) > 1):
			continue

		points_to_test.append(p)

	print(points_to_test)

	# min_steps = 1 + min([get_min_steps(p) for p in points_to_test])
	# cache[point] = min_steps
	# return min_steps

def expand_cache():
	curr_cache_size = len(cache)
	current_level = max(cache.values())
	current_level_cache = list(filter(lambda k: cache[k] == current_level, cache.keys()))

	for point in current_level_cache:
		adjacencies = [(1, 0), (-1, 0), (0, 1), (0, -1)]
		adjacent_points = [(point[0] + a[0], point[1] + a[1]) for a in adjacencies]
		current_altitude = get_altitude(point)
		for p in adjacent_points:
			if (p[0] < 0) or (p[0] >= len(data)):
				continue
			if (p[1] < 0) or (p[1] >= len(data[0])):
				continue
			if (get_altitude(p) - current_altitude > 1):
				continue
			if p in cache.keys():
				continue

			cache[p] = 1 + current_level

	return len(cache) - curr_cache_size

def solve_part_1():
	# I think this is a DP problem.
	# Find the fastest route to each square.
	# You find the fastest route, by looking at each VALID neighbor

	# Use that to find the fastest route to E

	# Oh, that's an infinite recursion. We gotta try something else.
	# Start by looking at all the 0's in the cache. Build a list of 1's
	# Then, look at all the 1's. Build a list of 2's. Etc.

	while end not in cache.keys():
		expand_cache()
	print(cache[end])

def solve_part_2():
	candidate_starts = []
	min_paths = {}

	for i in range(len(data)):
		for j in range(len(data[i])):
			if get_altitude((i, j)) == 1:
				candidate_starts.append((i, j))

	print(len(candidate_starts))
	count = 0

	for start in candidate_starts:
		count += 1
		print(count, start)

		cache.clear()
		cache[start] = 0
		while end not in cache.keys():
			cache_expansion = expand_cache()
			if cache_expansion == 0:
				cache[end] = 1000000
				break

		min_paths[start] = cache[end]

	print(min(min_paths.values()))

solve_part_2()
