import numpy as np
import random

height, width = 0, 0
bombs = 0


height = int(input("Enter height: "))
width = int(input("Enter width: "))
bombs = int(input("Enter number of bombs: "))

print(height, " ", width, " ", bombs)

board = np.zeros((height, width))
visibleBoard = np.zeros((height, width), dtype='str')

def checkIfBomb(x, y):
    return (board[x,y]==-1)

def checkIfRevealed(x, y):
    return (visibleBoard[x,y]!="X")

def revealSpot(x, y):
    if not checkIfBomb(x,y) and not checkIfRevealed(x,y):
        visibleBoard[x,y]=board[x,y]
        if board[x,y]==0:
            revealSurrounding(x,y)
        return True
    return False

def revealSurrounding(x, y):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if x+i>=0 and x+i<height and y+j>=0 and y+j<width:
                revealSpot(x+i,y+j)
    return

def printBoard():
    for x in range(width):
        print("-", end="-")
    print("-", end="-")
    print("-")

    for x in range(height):
        print("|", end=" ")
        for y in range(width):
            print(visibleBoard[x,y], end=" ")
        print("|")

    for x in range(width):
        print("-", end="-")
    print("-", end="-")
    print("-")


random_x=0
random_y=0

for x in range(bombs):
    while True:
        temp_x = random.randint(1, height)-1
        temp_y = random.randint(1, width)-1
        if (random_x != temp_x and random_y != temp_y):
            random_x = temp_x
            random_y = temp_y
            break
    board[random_x, random_y] = -1

for x in range(height):
    for y in range(width):
        if board[x,y] != -1:
            counter = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if x+i>=0 and x+i<height and y+j>=0 and y+j<width and board[x+i,y+j] == -1:
                        counter += 1
            board[x,y] = counter

for x in range(height):
    for y in range(width):
        visibleBoard[x,y] = "X"

printBoard()

while True:
    inX = int(input("enter x:"))
    inY = int(input("enter y:"))
    if checkIfBomb(inX, inY):
        printBoard()
        print("YOU LOSE!")
        break
    revealSpot(inX, inY)
    printBoard()
