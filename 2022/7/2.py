from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from functools import cached_property

def getInputStr(inputFileName):
	with open(inputFileName, 'r') as inputFile:
		return inputFile.read()

def getTransformedInput(inputFileName):
	return getInputStr(inputFileName).splitlines()

@dataclass
class File:
	name: str
	size: int

@dataclass
class Directory:
	name: str
	parentDirectory: Optional[Directory] = None
	fileLst: list = field(init=False, default_factory=list)
	directoryLst: list = field(init=False, default_factory=list)
	fileLst: list = field(init=False, default_factory=list)

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

	@cached_property
	def size(self):
		size = 0

		for file in self.fileLst:
			size += file.size
		
		if not self.directoryLst:
			return size
		
		for directory in self.directoryLst:
			size += directory.size
		
		return size

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

	requiredFreeSpace = 3 * 10**7 - (7 * 10**7 - rootDirectory.size)
	print(min(directory.size for directory in directoryLst if directory.size >= requiredFreeSpace))


if __name__ == '__main__':
	main()