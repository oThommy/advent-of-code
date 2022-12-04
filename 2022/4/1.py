def getInputStr(inputFileName):
	with open(inputFileName, 'r') as inputFile:
		return inputFile.readlines()

def getTransformedInput(inputFileName):
	return getInputStr(inputFileName)

def main():
	input = getTransformedInput('example_input.txt')
	input = getTransformedInput('input.txt')

	fullyContainedPairs = 0
	for elfPair in input:
		range1, range2 = elfPair.split(',')
		elf1 = {
			'sectionNumMin': int(range1.split('-')[0]),
			'sectionNumMax': int(range1.split('-')[1]),
		}
		elf2 = {
			'sectionNumMin': int(range2.split('-')[0]),
			'sectionNumMax': int(range2.split('-')[1]),
		}
		fullyContainedPairs += (elf1['sectionNumMin'] >= elf2['sectionNumMin'] and elf1['sectionNumMax'] <= elf2['sectionNumMax']) or \
							   (elf2['sectionNumMin'] >= elf1['sectionNumMin'] and elf2['sectionNumMax'] <= elf1['sectionNumMax'])

	print(fullyContainedPairs)


if __name__ == '__main__':
	main()