from dataclasses import dataclass
import itertools
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

def areAdjecent(point1: Point, point2: Point):
	return abs(point2.x - point1.x) <= 1 and abs(point2.y - point1.y) <= 1

def simulateMotion(deltaX: int, deltaY: int, steps: int, ropeKnots: list[Point], tailLocations: set):
	head = ropeKnots[0]

	for _ in range(steps):
		head.x += deltaX
		head.y += deltaY
		pairedKnots = list(itertools.pairwise(ropeKnots))

		# move each consecutive knot accordingly
		for i, (leadingKnot, currentKnot) in enumerate(pairedKnots):
			if areAdjecent(currentKnot, leadingKnot):
				continue
			
			# move 1 step (diagonally or in a straight line) towards the leading knot
			currentKnot.x += np.sign(leadingKnot.x - currentKnot.x)
			currentKnot.y += np.sign(leadingKnot.y - currentKnot.y)

			if i == len(pairedKnots) - 1:
				tailLocations.add(currentKnot.getLocation())

	return ropeKnots, tailLocations

def main():
	input = getTransformedInput('example_input.txt')
	input = getTransformedInput('example_input_2.txt')
	input = getTransformedInput('input.txt')
	motions = input

	ropeKnots = [Point(0, 0) for _ in range(10)]
	tailLocations = set(ropeKnots[-1].getLocation())

	for motion in motions:
		direction, steps = motion.split()
		steps = int(steps)

		match direction:
			case 'U':
				ropeKnots, tailLocations = simulateMotion(0, 1, steps, ropeKnots, tailLocations)
			case 'R':
				ropeKnots, tailLocations = simulateMotion(1, 0, steps, ropeKnots, tailLocations)
			case 'D':
				ropeKnots, tailLocations = simulateMotion(0, -1, steps, ropeKnots, tailLocations)
			case 'L':
				ropeKnots, tailLocations = simulateMotion(-1, 0, steps, ropeKnots, tailLocations)

	print(len(tailLocations))


if __name__ == '__main__':
	main()