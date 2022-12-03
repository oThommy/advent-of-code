def getInput(inputFile):
	input = []

	with open(inputFile, 'r') as inputFile:
		for line in inputFile:
			input.append(line)

	return input

def main():
	# input = getInput('example_input.txt')
	input = getInput('input.txt')
	caloriesLst = [0]
	for calories in input:
		if calories == '\n':
			caloriesLst.append(0)
		else:
			caloriesLst[-1] += int(calories.split('\n')[0])
	print(sum(sorted(caloriesLst)[-3:]))
	


if __name__ == '__main__':
	main()