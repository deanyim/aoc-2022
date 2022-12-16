IS_TEST = True

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

class Directory:
	def __init__(self, name):
		self.name = name
		self.children = {}

class File:
	def __init__(self, name, parent, size):
		self.name = name
		self.children = {}
		self.size = size

def get_size(directories, files, directory):
	pass

def build_filesystem(commands):
	directories = []
	files = []
	cursor = "/"
	
	for command in commands:
		

def get_grouped_commands():
	grouped_commands = []
	for r in data:
		if r[0] == "$":
			grouped_commands.append([r])
		else:
			grouped_commands[-1].append(r)
	return grouped_commands


def solve_part_1():
	# whoa... 
	# what if I want to create a Directory class and a File class?
	# Directory and File both have Name and Parent attributes
	# File has Size

	# is that overkill? lol

	# then i can just write Directory.get_size() and enumerate thru
	# all the Directories
	commands = get_grouped_commands()
	[print(c) for c in commands]
	pass

solve_part_1()
