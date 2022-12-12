import re

monkeyDescription = '''Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3'''


inventory = [int(item) for item in re.search(r'Starting items: ([^\n]+)', monkeyDescription).group(1).split(',')]
operationStr = re.match(r'old (.+)(?=\n)')
testNum: int
targetMonkeyIndexIfTrue: int
targetMonkeyIndexIfFalse: int
print(inventory)
print()