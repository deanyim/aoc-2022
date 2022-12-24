IS_TEST = False

TEST_DICT = {
	True: {
		'filename': 'input07-test.txt'
	},
	False: {
		'filename': 'input07.txt'
	}
}

with open(TEST_DICT[IS_TEST]['filename'], encoding='utf-8') as f:
	data = f.read().splitlines()
	grouped_commands = []
	for r in data:
		if r[0] == "$":
			grouped_commands.append([r])
		else:
			grouped_commands[-1].append(r)

def build_filesystem(fs):
	# I FIGURED OUT THE MISTAKE!!!!
	# I NEED TO STORE THE FULL PATH... NOT JUST THE PARTIAL PATH!
	# YOU CAN HAVE MULTIPLE DIRS/FILES WITH THE SAME NAME! THIS FUCKS YOU UP!
	cursor = "/"
	for command in grouped_commands:
		print(cursor, command)
		c, args = command[0], command[1:]
		if c.startswith('$ cd'):
			cursor = move_cursor(c, cursor, fs)
			print ("moved cursor to", cursor)
		elif c.startswith('$ ls'):
			fs = parse_ls(args, cursor, fs)
	return fs

def move_cursor(command, old_cursor, fs):
	target = command[5:]
	if target != "..":
		if (target != "/") and (target not in fs[old_cursor][2]):
			raise NotImplementedError("target not in current directory", command, old_cursor, fs)

		return target
	for path, v in fs.items():
		if (old_cursor in v[2]) and (v[0] == 'dir'):
			return path

	raise NotImplementedError("couldn't find parent", command, old_cursor, fs)

def parse_ls(args, cursor, fs):
	for f in args:
		if f in fs.keys():
			continue

		first, filename = f.split(" ")
		fs[cursor][2].add(filename)

		if first == "dir":
			fs[filename] = ["dir", "?", set()]
		else:
			size = int(first)
			fs[filename] = ["file", size, set()]
	return fs

def get_directory_size(fn, fs):
	children = fs[fn][2]
	size = 0
	for child in children:
		if fs[child][0] == "file":
			size += fs[child][1]
		elif fs[child][0] == "dir":
			if fs[child][1] == "?":
				size += get_directory_size(child, fs)
			else:
				size += fs[child][1]

	fs[fn][1] = size
	return size


def solve_part_1():
	# path: (type, size, children)
	fs = {
		"/": ["dir", '?', set()]
	}
	fs = build_filesystem(fs)
	get_directory_size("/", fs)
	directories = [fn for fn in fs.keys() if fs[fn][0] == 'dir']
	sizes = [fs[d][1] for d in directories]
	print(sizes)
	print(sum([s for s in sizes if s <= 100000]))

solve_part_1()
