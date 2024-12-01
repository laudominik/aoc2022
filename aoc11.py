class Monkey:
    def __init__(self, items, operation, test, iftrue, iffalse):
        self.items = items
        self.operation = operation
        self.test = test
        self.iftrue = iftrue
        self.iffalse = iffalse
        self.examinations = 0

    def turn(self, monkeys):
        
        for item in self.items:
            item = self.operation(item)
            self.examinations += 1  
            item %= 9699690
            if self.test(item):
                monkeys[self.iftrue].items.append(item)
            else:
                monkeys[self.iffalse].items.append(item)
        self.items = []

def turn(monkeys):
    for monkey in monkeys:
        monkey.turn(monkeys)

monkeys = [
    Monkey([97, 81, 57, 57, 91, 61], lambda x: x * 7, lambda x: x % 11 == 0, 5, 6),
    Monkey([88, 62, 68, 90], lambda x: x * 17, lambda x: x % 19 == 0, 4, 2),
    Monkey([74, 87], lambda x: x + 2, lambda x: x % 5 == 0, 7, 4),
    Monkey([53, 81, 60, 87, 90, 99, 75], lambda x: x + 1, lambda x: x % 2 == 0, 2, 1),
    Monkey([57], lambda x: x + 6, lambda x: x % 13 == 0, 7, 0),
    Monkey([54, 84, 91, 55, 59, 72, 75, 70], lambda x: x * x, lambda x: x % 7 == 0, 6, 3),
    Monkey([95, 79, 79, 68, 78], lambda x: x + 3, lambda x: x % 3 == 0, 1, 3),
    Monkey([61, 97, 67], lambda x: x + 4, lambda x: x % 17 == 0, 0, 5),
]

for i in range(10000):
    print(i)
    turn(monkeys)


examinations = [monkey.examinations for monkey in monkeys]
examinations.sort(reverse=True)
print(examinations[0] * examinations[1])