def getInput(inputFileName):
	with open(inputFileName, 'r') as inputFile:
		return inputFile.read().splitlines()

def main():
	# input = getInput('example_input.txt')
	input = getInput('input.txt')

	totalSum = 0
	for i in range(0, len(input), 3):
		sharedItem: str = list(set.intersection(*[set(rucksack) for rucksack in input[i:i+3]]))[0]
		if sharedItem == '':
			continue
		elif sharedItem.islower():
			totalSum += ord(sharedItem) % ord('a') + 1
		else:
			totalSum += ord(sharedItem) % ord('A') + 27

	print(totalSum)


if __name__ == '__main__':
	main()