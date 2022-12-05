from collections import deque
import re

def getInputStr(inputFileName):
	with open(inputFileName, 'r') as inputFile:
		return inputFile.read()

def getTransformedInput(inputFileName):
	return getInputStr(inputFileName).split('\n\n')

def main():
	input = getTransformedInput('example_input.txt')
	input = getTransformedInput('input.txt')
	
	crateLines, stacksAmount = input[0].split('\n 1')
	crateLines = crateLines.splitlines()[::-1]
	stacksAmount = int(max(stacksAmount.split()))
	stacks = [deque() for _ in range(stacksAmount)]

	for crateLine in crateLines:
		for i in range(stacksAmount):
			crate = crateLine[1 + i * 4]
			if crate == ' ':
				continue
			stacks[i].append(crate)

	instructions = input[1].splitlines()
	for instruction in instructions:
		matchRes = re.search(r'move (\d+) from (\d+) to (\d+)', instruction)
		crateAmount = int(matchRes.group(1))
		sourceStack = int(matchRes.group(2)) - 1
		destinationStack = int(matchRes.group(3)) - 1

		for _ in range(crateAmount):
			stacks[destinationStack].append(stacks[sourceStack].pop())

	topCrates = ''
	for stack in stacks:
		if not stack:
			continue
		topCrates += stack[-1]

	print(topCrates)


if __name__ == '__main__':
	main()