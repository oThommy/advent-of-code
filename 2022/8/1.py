import numpy as np

def getInputStr(inputFileName):
	with open(inputFileName, 'r') as inputFile:
		return inputFile.read()

def getTransformedInput(inputFileName):
	return [[int(treeHeight) for treeHeight in list(line)] for line in getInputStr(inputFileName).splitlines()]

def isTreeVisible(i, j, grid):
	treeHeight = grid[i][j]
	
	return any([
		np.all(grid[i,:j] < treeHeight),
		np.all(grid[i,j+1:] < treeHeight),
		np.all(grid[:i,j] < treeHeight),
		np.all(grid[i+1:,j] < treeHeight),
	])

def main():
	input = getTransformedInput('example_input.txt')
	input = getTransformedInput('input.txt')
	grid = np.array(input)

	n = len(grid)
	visibleTreesAmount = 4 * n - 4

	for i in range(1, n - 1):
		for j in range(1, n - 1):
			visibleTreesAmount += isTreeVisible(i, j, grid)

	print(visibleTreesAmount)


if __name__ == '__main__':
	main()