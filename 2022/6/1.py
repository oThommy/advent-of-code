def getInputStr(inputFileName):
	with open(inputFileName, 'r') as inputFile:
		return inputFile.read()

def getTransformedInput(inputFileName):
	return getInputStr(inputFileName)

def main():
	input = getTransformedInput('example_input.txt')
	input = getTransformedInput('input.txt')
	
	for i, _ in enumerate(input):
		if len(set(input[i:i+4])) == 4:
			print(i+4)
			break

if __name__ == '__main__':
	main()