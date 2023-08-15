import random, time, copy

Width = 60
Height = 60

nextCells = []
for y in range(Width):
    column = []
    for x in range(Height):
        if random.randint(0, 1) == 0:
            column.append("#")
        else:
            column.append(" ")
    nextCells.append(column)

while True:
    print("\n\n\n\n\n")
    currentCells = copy.deepcopy(nextCells)
    for y in range(Height):
        for x in range(Width):
            print(currentCells[x][y], end=" ")
        print()

    for x in range(Width):
        for y in range(Height):
            leftCoord = (x - 1) % Width
            rightCoord = (x + 1) % Width
            aboveCoord = (y - 1) % Height
            belowCoord = (y + 1) % Height


            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == "#":
                numNeighbors += 1
            if currentCells[x][aboveCoord] == "#":
                numNeighbors += 1
            if currentCells[rightCoord][aboveCoord] == "#":
                numNeighbors += 1
            if currentCells[leftCoord][y] == "#":
                numNeighbors += 1
            if currentCells[rightCoord][y] == "#":
                numNeighbors += 1
            if currentCells[leftCoord][belowCoord] == "#":
                numNeighbors += 1
            if currentCells[x][belowCoord] == "#":
                numNeighbors += 1
            if currentCells[rightCoord][belowCoord] == "#":
                numNeighbors += 1


            if currentCells[x][y] == "#" and (numNeighbors == 2 or numNeighbors == 3):
                nextCells[x][y] = "#"
            elif currentCells[x][y] == " " and numNeighbors == 3:
                nextCells[x][y] = "#"
            else:
                nextCells[x][y] = " "
        time.sleep(2)