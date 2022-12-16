import ast

IS_TEST = False

TEST_DICT = {
	True: {
		'filename': 'input16-test.txt'
	},
	False: {
		'filename': 'input16.txt'
	}
}

with open(TEST_DICT[IS_TEST]['filename'], encoding='utf-8') as f:
	data = f.read().splitlines()
	parsed_data = {}
	valves = {}

	for row in data:
		row_split = row.split(';')
		valve = row_split[0]
		pressure = int(row_split[1])
		connections = set(row_split[2].split(", "))
		parsed_data[valve] = (pressure, connections)
		if pressure != 0:
			valves[valve] = pressure

MEMOIZED_DISTANCES = {}

def get_distance(start, end):
	if (start, end) in MEMOIZED_DISTANCES.keys():
		return MEMOIZED_DISTANCES[(start, end)]

	traversal = {start}
	distance = 0
	while end not in traversal:
		distance += 1
		trav_list = list(traversal)
		for t in trav_list:
			traversal.update(parsed_data[t][1])

	MEMOIZED_DISTANCES[(start, end)] = distance
	return distance

def get_pressure(remaining_valves, all_valves):
	activated_valves = all_valves - remaining_valves
	return sum([valves[v] for v in activated_valves])

MEMOIZED_ANSWERS = {}

def get_max_pressure(time, loc, remaining_valves, all_valves):
	choices = []

	if remaining_valves == frozenset():
		return time * get_pressure(remaining_valves, all_valves)

	for v in remaining_valves:
		args = (
			time - 1 - get_distance(loc, v),
			v,
			remaining_valves - {v},
			all_valves,
		)

		if args[0] <= 0:
			choices.append(time * get_pressure(remaining_valves, all_valves))
			continue

		if args in MEMOIZED_ANSWERS.keys():
			pressure = MEMOIZED_ANSWERS[args]
		else:
			pressure = get_max_pressure(*args)
			MEMOIZED_ANSWERS[args] = pressure

		current_pressure = get_pressure(remaining_valves, all_valves) * (1 + get_distance(loc, v))
		choices.append(pressure + current_pressure)
	
	return max(choices)
	

def solve_part_1():
	print(get_max_pressure(
		30,
		'AA',
		frozenset(valves.keys()),
		frozenset(valves.keys())
	))
	
def make_partial_paths():
	paths = {(0, ('AA',), 0)}
	paths_to_add = set()
	while True:
		num_paths_start = len(list(paths))
		for path in paths:
			for valve in valves.keys():
				if valve not in set(path[1]):
					d = get_distance(path[1][-1], valve)
					time_after_opening = path[0] + d + 1
					if time_after_opening < 26:
						paths_to_add.add((
							time_after_opening,
							path[1] + (valve,),
							path[2] + (26 - time_after_opening) * valves[valve]
						))

		paths.update(paths_to_add)
		num_paths_end = len(list(paths))
		if num_paths_start == num_paths_end:
			break

	return paths

def solve_part_2():
	# Try every 26-minute path -- including partials
	# Then, subtract the used valves from `valves`, and find the maximum for the elephant.
	
	paths = make_partial_paths()
	print("paths:", len(list(paths)))
	total_pressures = []
	count = 0
	for path in paths:
		count += 1
		if count % 100 == 0:
			print(count)

		remaining_valves = valves.keys() - set(path[1])
		total_pressure = path[2] + get_max_pressure(
			26,
			'AA',
			frozenset(remaining_valves),
			frozenset(remaining_valves))
		total_pressures.append(total_pressure)

	print(max(total_pressures))


solve_part_2()
