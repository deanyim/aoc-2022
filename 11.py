import re

IS_TEST = False

TEST_DICT = {
	True: {
		'filename': 'input11-test.txt'
	},
	False: {
		'filename': 'input11.txt'
	}
}

with open(TEST_DICT[IS_TEST]['filename'], encoding='utf-8') as f:
	data = f.read().splitlines()
	monkeys = []
	num_monkeys = len(data) // 7
	worry_modulus = 1
	for i in range(num_monkeys):
		monkey_data = data[7*i+1:7*i+6]

		starting_items = [int(i) for i in re.findall(r'\d+', monkey_data[0])]
		operator = re.findall(r'\*|\+', monkey_data[1])[0]
		op_arg = re.findall(r'\d+$|old$', monkey_data[1])[0]
		if op_arg != 'old':
			op_arg = int(op_arg)

		test_divisor = int(re.findall(r'\d+', monkey_data[2])[0])
		if_true = int(re.findall(r'\d+', monkey_data[3])[0])
		if_false = int(re.findall(r'\d+', monkey_data[4])[0])
		worry_modulus *= test_divisor

		monkeys.append((
			starting_items,
			operator,
			op_arg,
			test_divisor,
			if_true,
			if_false
		))
		monkey_inspection_counts = [0] * len(monkeys)

def run_one_round(monkey_items):
	for i in range(len(monkey_items)):
		# increment monkey inspection counts
		monkey_inspection_counts[i] += len(monkey_items[i])

		operator = monkeys[i][1]
		op_arg = monkeys[i][2]

		test_divisor = monkeys[i][3]
		if_true = monkeys[i][4]
		if_false = monkeys[i][5]

		for j in range(len(monkey_items[i])):
			# run the "worry level operation"
			worry_level = monkey_items[i][j]
			if operator == "+":
				worry_level += op_arg
			elif operator == "*":
				if op_arg == "old":
					worry_level *= worry_level
				else:
					worry_level *= op_arg
	
			# pt. 1, divide by 3
			# pt. 2, mod sigma(test_divisor)
			worry_level = worry_level % worry_modulus

			if worry_level % test_divisor == 0:
				target_monkey = if_true
			else:
				target_monkey = if_false
			
			monkey_items[target_monkey].append(worry_level)
			# append it to the appropriate list
		
		monkey_items[i] = []


	return monkey_items

def solve_part_1():
	monkey_items = [m[0] for m in monkeys]
	for i in range(10000):
		run_one_round(monkey_items)
	
	print(
		sorted(monkey_inspection_counts)[-2] * sorted(monkey_inspection_counts)[-1]
	)

def solve_part_2():
	pass

solve_part_1()
