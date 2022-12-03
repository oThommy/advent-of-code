import os
import shutil
from pathlib import Path
import filecmp

MIN_DAY = 26
MAX_DAY = 25
TEMPLATE_DIR_PATH = Path.cwd() / 'template'

def main():
	for day in range(MIN_DAY, MAX_DAY + 1):
		dayDirectoryPath = Path.cwd() / str(day)
		shutil.rmtree(dayDirectoryPath)
		shutil.copytree(TEMPLATE_DIR_PATH, dayDirectoryPath)


if __name__ == '__main__':
	main()