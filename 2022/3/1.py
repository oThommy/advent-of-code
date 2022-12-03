def getInput(inputFileName):
	with open(inputFileName, 'r') as inputFile:
		return inputFile.read().splitlines()

def main():
	# input = getInput('example_input.txt')
	input = getInput('input.txt')

	totalSum = 0
	for rucksack in input:
		compartment1 = set(rucksack[:len(rucksack) // 2])
		compartment2 = set(rucksack[len(rucksack) // 2:])
		sharedItem = list(compartment1.intersection(compartment2))[0]
		if sharedItem == '':
			continue
		elif sharedItem.islower():
			totalSum += ord(sharedItem) % ord('a') + 1
		else:
			totalSum += ord(sharedItem) % ord('A') + 27




	print(totalSum)


if __name__ == '__main__':
	main()