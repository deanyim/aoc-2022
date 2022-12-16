import ast

from functools import cmp_to_key

IS_TEST = False

TEST_DICT = {
	True: {
		'filename': 'input13-test.txt'
	},
	False: {
		'filename': 'input13.txt'
	}
}

with open(TEST_DICT[IS_TEST]['filename'], encoding='utf-8') as f:
	data = f.read().splitlines()

def grouplen(sequence, chunk_size):
    return list(zip(*[iter(sequence)] * chunk_size))

def compare_packets(packet1, packet2):
	if (packet1 == []) & (packet2 != []):
		return -1
	if (packet2 == []) & (packet1 != []):
		return 1
	if (packet1 == []) & (packet2 == []):
		return 0

	element1 = packet1[0]
	element2 = packet2[0]

	if isinstance(element1, int) & isinstance(element2, int):
		if element1 < element2:
			return -1
		elif element1 > element2:
			return 1
		return compare_packets(packet1[1:], packet2[1:])

	elif isinstance(element1, list) & isinstance(element2, list):
		comparison = compare_packets(element1, element2)

	elif isinstance(element1, int) & isinstance(element2, list):
		comparison = compare_packets([element1], element2)

	elif isinstance(element1, list) & isinstance(element2, int):
		comparison = compare_packets(element1, [element2])

	if comparison == 0:
		return compare_packets(packet1[1:], packet2[1:])
	else:
		return comparison

def solve_part_1():
	groups = grouplen(data, 3)
	results = []
	index = 1
	for g in groups:
		packet1, packet2, _ = g
		results.append((index, compare_packets(
			ast.literal_eval(packet1),
			ast.literal_eval(packet2))))
		index += 1

	results = map(lambda x: x[0], filter(lambda x: x[1] == -1, results))
	print(sum(results))

def solve_part_2():
	groups = grouplen(data, 3)
	packets = [[[2]], [[6]]]
	for g in groups:
		packet1, packet2, _ = g
		packets.append(ast.literal_eval(packet1))
		packets.append(ast.literal_eval(packet2))
	ordered_packets = list(sorted(packets, key=cmp_to_key(compare_packets)))
	print([1 + ordered_packets.index(p) for p in packets[:2]])

solve_part_2()
