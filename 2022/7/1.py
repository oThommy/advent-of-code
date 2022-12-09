from dataclasses import dataclass

def getInputStr(inputFileName):
	with open(inputFileName, 'r') as inputFile:
		return inputFile.read()

def getTransformedInput(inputFileName):
	return getInputStr(inputFileName).splitlines()

@dataclass
class File:
	name: str
	size: int

class Directory:
	def __init__(self, name, parentDirectory=None):
		self.name = name
		self.parentDirectory = parentDirectory
		self.fileLst = []
		self.directoryLst = []
		self.cachedSize = None

	def addFile(self, file):
		self.fileLst.append(file)

	def addDirectory(self, directory):
		self.directoryLst.append(directory)

	def getDirectory(self, targetDirectoryName):
		return next((directory for directory in self.directoryLst if directory.name == targetDirectoryName), None)

	def getTreeStr(self, depth=0):
		res = '  ' * depth + f'- {self.name} (dir)' + '\n'

		for file in self.fileLst:
			res += '  ' * (depth + 1) + f'- {file.name} (file, size={file.size})' + '\n'

		if not self.directoryLst:
			return res

		for directory in self.directoryLst:
			res += directory.getTreeStr(depth + 1)

		return res

	def getSize(self):
		if self.cachedSize is not None:
			return self.cachedSize

		self.cachedSize = 0

		for file in self.fileLst:
			self.cachedSize += file.size
		
		if not self.directoryLst:
			return self.cachedSize
		
		for directory in self.directoryLst:
			self.cachedSize += directory.getSize()
		
		return self.cachedSize

	def __repr__(self):
		return self.name

def handleConsoleLine(consoleLine: str, currentDirectory: Directory, isPrintingList: bool, directoryLst: list[Directory]):
	if consoleLine.startswith('$ cd'):
		isPrintingList = False
		directoryName = consoleLine.split('$ cd ')[1]

		if directoryName == '..':
			currentDirectory = currentDirectory.parentDirectory
			return currentDirectory, isPrintingList, directoryLst

		currentDirectory = currentDirectory.getDirectory(directoryName)
	elif consoleLine == '$ ls':
		isPrintingList = True
	elif isPrintingList:
		if consoleLine.startswith('dir'):
			subDirectory = Directory(consoleLine.split()[1], currentDirectory)
			currentDirectory.addDirectory(subDirectory)
			directoryLst.append(subDirectory)
		else:
			size, name = consoleLine.split()
			currentDirectory.addFile(File(name, int(size)))

	return currentDirectory, isPrintingList, directoryLst

def main():
	input = getTransformedInput('example_input.txt')
	input = getTransformedInput('input.txt')
	consoleLines = input[1:] # skip going into root directory, because currentDirectory is already defined in this way
	
	rootDirectory = Directory('/')
	currentDirectory = rootDirectory
	directoryLst = [rootDirectory]
	isPrintingList = False
	
	for consoleLine in consoleLines:
		currentDirectory, isPrintingList, directoryLst = handleConsoleLine(consoleLine, currentDirectory, isPrintingList, directoryLst)

	print(rootDirectory.getTreeStr())
	print(sum(directory.getSize() for directory in directoryLst if directory.getSize() <= 10**5))


if __name__ == '__main__':
	main()