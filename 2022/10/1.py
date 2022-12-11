from typing import Optional
from dataclasses import dataclass

def getInputStr(inputFileName):
	with open(inputFileName, 'r') as inputFile:
		return inputFile.read()

def getTransformedInput(inputFileName):
	return getInputStr(inputFileName).splitlines()

@dataclass
class Instruction:
	finishingCycle: int
	V: int

def main():
	input = getTransformedInput('example_input.txt')
	input = getTransformedInput('input.txt')
	instructionIter = iter(input)
	
	X = 1
	currentCyle = 0
	currentInstruction: Optional[Instruction] = None
	signalStrengthSum = 0

	while instructionIter or currentInstruction is not None:
		currentCyle += 1

		if currentCyle % 40 == 20 and currentCyle <= 220:
			signalStrengthSum += currentCyle * X
		
		if currentInstruction:
			currentInstruction: Instruction
			if currentInstruction.finishingCycle == currentCyle:
				X += currentInstruction.V
				currentInstruction = None
			
			# only when current instruction is done executing, should it go to the next instruction
			continue

		instructionName, *V = next(instructionIter, 'FINISHED').split()

		# all instructions have finished executing
		if instructionName == 'FINISHED':
			break
		
		# instruction is addx, so it should finish next cycle
		if instructionName == 'addx':
			currentInstruction = Instruction(currentCyle + 1, int(V[0]))

		# instruction is noop, so it finishes this cycle and doesn't require any further action

	print(signalStrengthSum)
	

if __name__ == '__main__':
	main()