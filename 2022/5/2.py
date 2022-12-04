def getInputStr(inputFileName):
	with open(inputFileName, 'r') as inputFile:
		return inputFile.readlines()

def getTransformedInput(inputFileName):
	return getInputStr(inputFileName)

def main():
	input = getTransformedInput('example_input.txt')
	input = getTransformedInput('input.txt')
	


if __name__ == '__main__':
	main()