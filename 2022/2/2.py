def getInput(inputFileName):
	input = []

	with open(inputFileName, 'r') as inputFile:
		for line in inputFile:
			input.append(line.rstrip().replace(' ', ''))

	return input

def main():
	input = getInput('example_input.txt')
	input = getInput('input.txt')

	shape_score = {
		'A': {
			'X': 3,
			'Y': 1,
			'Z': 2,
		},
		'B': {
			'X': 1,
			'Y': 2,
			'Z': 3,
		},
		'C': {
			'X': 2,
			'Y': 3,
			'Z': 1,
		},
	}

	totalScore = 0
	for round in input:
		elfChoice = round[0]
		playerChoice = round[1]

		totalScore += shape_score[elfChoice][playerChoice]
		totalScore += (ord(playerChoice) % ord('X')) * 3

	print(totalScore)


if __name__ == '__main__':
	main()