def getInput(inputFileName):
	input = []

	with open(inputFileName, 'r') as inputFile:
		for line in inputFile:
			input.append(line.rstrip().replace(' ', ''))

	return input

def main():
	input = getInput('example_input.txt')
	input = getInput('input.txt')

	loseLst = ['AZ', 'BX', 'CY']
	drawLst = ['AX', 'BY', 'CZ']
	winLst = ['AY', 'BZ', 'CX']

	totalScore = 0
	for round in input:
		roundScore = 0
		playerChoice = round[-1]
		
		if round in drawLst:
			roundScore += 3
		elif round in winLst:
			roundScore += 6
		
		if playerChoice == 'X':
			roundScore += 1
		elif playerChoice == 'Y':
			roundScore += 2
		elif playerChoice == 'Z':
			roundScore += 3

		totalScore += roundScore

	print(totalScore)


if __name__ == '__main__':
	main()