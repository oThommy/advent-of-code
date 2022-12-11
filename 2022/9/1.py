from dataclasses import dataclass
import numpy as np

def getInputStr(inputFileName):
	with open(inputFileName, 'r') as inputFile:
		return inputFile.read()

def getTransformedInput(inputFileName):
	return getInputStr(inputFileName).splitlines()

@dataclass
class Point:
	x: int
	y: int

	def getLocation(self):
		return (self.x, self.y)

def areAdjecent(tail: Point, head: Point):
	return abs(head.x - tail.x) <= 1 and abs(head.y - tail.y) <= 1

def simulateMotion(deltaX: int, deltaY: int, steps: int, tail: Point, head: Point, tailLocations: set):
	for _ in range(steps):
		head.x += deltaX
		head.y += deltaY

		if areAdjecent(tail, head):
			continue
			
		# move 1 step (diagonally or in a straight line) towards the head
		tail.x += np.sign(head.x - tail.x)
		tail.y += np.sign(head.y - tail.y)
		
		tailLocations.add(tail.getLocation())

	return tail, head, tailLocations

def main():
	input = getTransformedInput('example_input.txt')
	input = getTransformedInput('input.txt')
	motions = input

	tail = Point(0, 0)
	head = Point(0, 0)
	tailLocations = set(tail.getLocation())

	for motion in motions:
		direction, steps = motion.split()
		steps = int(steps)

		match direction:
			case 'U':
				deltaX = 0
				deltaY = 1
			case 'R':
				deltaX = 1
				deltaY = 0
			case 'D':
				deltaX = 0
				deltaY = -1
			case 'L':
				deltaX = -1
				deltaY = 0

		tail, head, tailLocations = simulateMotion(deltaX, deltaY, steps, tail, head, tailLocations)
		

	print(len(tailLocations))


if __name__ == '__main__':
	main()