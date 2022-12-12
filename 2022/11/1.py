from dataclasses import dataclass
from typing import List
import re

def getInputStr(inputFileName):
	with open(inputFileName, 'r') as inputFile:
		return inputFile.read()

def getTransformedInput(inputFileName):
	return getInputStr(inputFileName).split('\n' * 2)

class Monkey:
	inventory: List[int]
	operationStr: str
	testNum: int
	targetMonkeyIndexIfTrue: int
	targetMonkeyIndexIfFalse: int

def main():
	input = getTransformedInput('example_input.txt')
	input = getTransformedInput('input.txt')
	monkeyDescriptions = input

	receivedItems = dict()
	inspectationCount = dict()
	monkeyLst = []

	for monkeyDescription in monkeyDescriptions:
		inventory = re.search(r'Starting items: ([^\n]+)', monkeyDescription).group(1).split(',').map(int)

	for _ in range(20):
		# single round
			
			receivedItems[monkeyTarget] = []

if __name__ == '__main__':
	main()