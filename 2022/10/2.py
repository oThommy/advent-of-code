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
	screen = ''

	while instructionIter or currentInstruction is not None:
		currentCyle += 1
		pixelPosition = (currentCyle - 1) % 40

		if currentCyle <= 240:
			screen += '#' if abs(pixelPosition - X) <= 1 else '.'

			if currentCyle % 40 == 0:
				screen += '\n'
		
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

	print(screen)


if __name__ == '__main__':
	main()