with open('input02.txt', encoding='utf-8') as f:
	data = f.read().splitlines()

def line_score(l):
	opp, dean = l.split(' ')
	shape_values = {'X': 1, 'Y': 2, 'Z': 3, 'A': 1, 'B': 2, 'C': 3}
	game_state = (shape_values[dean] - shape_values[opp]) % 3
	outcome_scores = {0: 3, 1: 6, 2: 0}

	return shape_values[dean] + outcome_scores[game_state]

def alt_line_score(l):
	opp, result = l.split(' ')
	game_score = {'X': 0, 'Y': 3, 'Z': 6}[result]
	opp_shape_score = {'A': 1, 'B': 2, 'C': 3}[opp]

	shape_score = opp_shape_score + {'X': -1, 'Y': 0, 'Z': 1}[result]
	shape_score = (shape_score - 1) % 3 + 1
	return shape_score + game_score

print(sum(map(lambda l: line_score (l), data)))
print(sum(map(lambda l: alt_line_score (l), data)))