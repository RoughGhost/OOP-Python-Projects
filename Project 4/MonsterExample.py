import random


class Monster():
    def __init__(self, nRows, nCols, maxSpeed):
        self.nRows = nRows  # save away
        self.nCols = nCols
        self.myRow = random.randrange(self.nRows)  # Chooses a random row
        self.myCol = random.randrange(self.nCols)
        self.mySpeedX = random.randrange(-maxSpeed, maxSpeed + 1)
        self.mySpeedY = random.randrange(-maxSpeed, maxSpeed + 1)

    def move(self):
        self.myRow = (self.myRow + self.mySpeedY) % self.nRows
        self.myCol = (self.myCol + self.mySpeedX) % self.nCols


N_MONSTERS = 20
N_ROWS = 100   # could be any size
N_COLS = 200   # could be any size
MAX_SPEED = 4


monsterList = []  # start with an empty list
for i in range(N_MONSTERS):
    oMonster = Monster(N_ROWS, N_COLS, MAX_SPEED)  # create a Monster
    monsterList.append(oMonster)  # add Monster to our list

# Later, when playing the game ...

for oMonster in monsterList:
    oMonster.move()
