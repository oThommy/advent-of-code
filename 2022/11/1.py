from dataclasses import dataclass, field
import math
from operator import attrgetter
from typing import List
import re


# FIXME: remove
from pprint import pprint

import numpy as np

def getInputStr(inputFileName):
	with open(inputFileName, 'r') as inputFile:
		return inputFile.read()

def getTransformedInput(inputFileName):
	return getInputStr(inputFileName).split('\n' * 2)

@dataclass
class Monkey:
	inventory: List[int]
	operationStr: str
	testNum: int
	targetMonkeyIndexIfTrue: int
	targetMonkeyIndexIfFalse: int
	inspectedItemsAmount: int = field(init=False, default=0)

def main():
	input = getTransformedInput('example_input.txt')
	input = getTransformedInput('input.txt')
	monkeyDescriptions = input

	monkeyLst: List[Monkey] = []

	for monkeyDescription in monkeyDescriptions:
		monkeyData = {
			'inventory': [int(item) for item in re.search(r'Starting items: ([^\n]+)', monkeyDescription).group(1).split(',')],
			'operationStr': re.search(r'old .+(?=\n)', monkeyDescription).group(),
			'testNum': int(re.search(r'divisible by (\d+)', monkeyDescription).group(1)),
			'targetMonkeyIndexIfTrue': int(re.search(r'If true: throw to monkey (\d+)', monkeyDescription).group(1)),
			'targetMonkeyIndexIfFalse': int(re.search(r'If false: throw to monkey (\d+)', monkeyDescription).group(1)),
		}

		monkeyLst.append(Monkey(**monkeyData))

	for _ in range(20):
		# single round
		for monkey in monkeyLst:
			while(monkey.inventory):
				item = monkey.inventory.pop(0)
				monkey.inspectedItemsAmount += 1
				worryLevel = eval(monkey.operationStr, { 'old': item })
				worryLevel = math.floor(worryLevel / 3)

				if worryLevel % monkey.testNum == 0:
					monkeyLst[monkey.targetMonkeyIndexIfTrue].inventory.append(worryLevel)
				else:
					monkeyLst[monkey.targetMonkeyIndexIfFalse].inventory.append(worryLevel)
	
	print(np.product(sorted(monkey.inspectedItemsAmount for monkey in monkeyLst)[-2:]))


if __name__ == '__main__':
	main()