import numpy as np

def getInputStr(inputFileName):
	with open(inputFileName, 'r') as inputFile:
		return inputFile.read()

def getTransformedInput(inputFileName):
	return [[int(treeHeight) for treeHeight in list(line)] for line in getInputStr(inputFileName).splitlines()]

def getViewingDistance(neighbourHeightLst, treeHeight):
	visibleTreeAmount = 0

	for neighbourHeight in neighbourHeightLst:
		visibleTreeAmount += 1

		if neighbourHeight >= treeHeight:
			break
	
	return visibleTreeAmount

def getScenicScore(i, j, grid):
	treeHeight = grid[i][j]

	return np.prod([
		getViewingDistance(grid[i,:j][::-1], treeHeight),
		getViewingDistance(grid[i,j+1:], treeHeight),
		getViewingDistance(grid[:i,j][::-1], treeHeight),
		getViewingDistance(grid[i+1:,j], treeHeight),
	])

def main():
	input = getTransformedInput('example_input.txt')
	input = getTransformedInput('input.txt')
	grid = np.array(input)

	n = len(grid)
	scenicScoreLst = []

	for i in range(1, n - 1):
		for j in range(1, n - 1):
			scenicScoreLst.append(getScenicScore(i, j, grid))

	print(max(scenicScoreLst))


if __name__ == '__main__':
	main()