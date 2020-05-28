# Code to determine biggest hole in peptide

# Easy procedure:
# List all points for which to calculate distance to closest atom. The furthest one wins. The winner should have
# Calphas on 5 out of 6 sides (+x, -x, +y, -y, +z, -z) (One can also determine the 2nd and 3rd biggest hole).


CheckIfInsidePeptide = np.array([0, 0, 0, 0, 0, 0]) # Treated like a boolean array. But to be able to use np.sum, a
# non-bool array is used.

counter = 0
secondCounter = 0
thirdCounter = 0
fourthCounter = 0
fifthCounter = 0
FurthestAADistance = 0
SecondFurthest = 0
ThirdFurthest = 0
FourthFurthest = 0
FifthFurthest = 0
Furthest6 = 0
Furthest7 = 0
Furthest8 = 0
Furthest9 = 0
Furthest10 = 0
ClosestDistanceForCurrentGridPoint = 100
BiggestHole = np.array([0, 0, 0])
SecondBiggestHole = np.array([0, 0, 0])
ThirdBiggestHole = np.array([0, 0, 0])
FourthBiggestHole = np.array([0, 0, 0])
FifthBiggestHole = np.array([0, 0, 0])
BiggestHole6 = np.array([0, 0, 0])
BiggestHole7 = np.array([0, 0, 0])
BiggestHole8 = np.array([0, 0, 0])
BiggestHole9 = np.array([0, 0, 0])
BiggestHole10 = np.array([0, 0, 0])
print(datetime.now(tz=None))
for x in np.arange(BottomX, TopX, 0.3):
    print(x)
    for y in np.arange(BottomY, TopY, 0.3):
        for z in np.arange(BottomZ, TopZ, 0.3):
            counter = counter + 1
            # Check if inside peptide
            # First check if there are amino acids in the positive and negative x direction.
            for xCheck in PreSortedX:
                if (CheckIfInsidePeptide[0] == 1) and (CheckIfInsidePeptide[1] == 1):
                    break
                if x < xCheck[0]:
                    if (xCheck[1] < y < xCheck[2]) and (xCheck[3] < z < xCheck[4]):
                        CheckIfInsidePeptide[0] = 1
                elif (xCheck[1] < y < xCheck[2]) and (xCheck[3] < z < xCheck[4]):
                    CheckIfInsidePeptide[1] = 1
            if CheckIfInsidePeptide[0] == 0 or CheckIfInsidePeptide[1] == 0:
                secondCounter = secondCounter + 1
            # Same in positive and negative y direction
            for yCheck in PreSortedY:
                if CheckIfInsidePeptide[2] == 1 and CheckIfInsidePeptide[3] == 1:
                    break
                if y < yCheck[0]:
                    if (yCheck[1] < x < yCheck[2]) and (yCheck[3] < z < yCheck[4]):
                        CheckIfInsidePeptide[2] = 1
                elif (yCheck[1] < x < yCheck[2]) and (yCheck[3] < z < yCheck[4]):
                    CheckIfInsidePeptide[3] = 1
            if CheckIfInsidePeptide[2] == 0 or CheckIfInsidePeptide[3] == 0:
                thirdCounter = thirdCounter + 1
            # And also in positive and negative z direction.
            for zCheck in PreSortedZ:
                if CheckIfInsidePeptide[4] == 1 and CheckIfInsidePeptide[5] == 1:
                    break
                if z < zCheck[0]:
                    if (zCheck[1] < x < zCheck[2]) and (zCheck[3] < y < zCheck[4]):
                        CheckIfInsidePeptide[4] = 1
                elif (zCheck[1] < x < zCheck[2]) and (zCheck[3] < y < zCheck[4]):
                    CheckIfInsidePeptide[5] = 1
            if CheckIfInsidePeptide[4] == 0 or CheckIfInsidePeptide[5] == 0:
                fourthCounter = fourthCounter + 1
            # And here check if there are enough amino acids around it to be considered as a hole.
            if np.sum(CheckIfInsidePeptide) > 4:
                fifthCounter = fifthCounter + 1
                grid = np.array([x, y, z])
                for pos in ca.positions:
                    distance = np.linalg.norm(pos-grid)
                    if distance < ClosestDistanceForCurrentGridPoint:
                        ClosestDistanceForCurrentGridPoint = distance
                if ClosestDistanceForCurrentGridPoint > FurthestAADistance: # True if new biggest hole is found
                    if np.linalg.norm(grid-BiggestHole) > 3:
                        ThirdFurthest = SecondFurthest
                        SecondFurthest = FurthestAADistance
                        FurthestAADistance = ClosestDistanceForCurrentGridPoint
                        ThirdBiggestHole = SecondBiggestHole
                        SecondBiggestHole = BiggestHole
                        BiggestHole = grid
                    else:
                        FurthestAADistance = ClosestDistanceForCurrentGridPoint
                        BiggestHole = grid
                elif ClosestDistanceForCurrentGridPoint > SecondFurthest:
                    if np.linalg.norm(grid-BiggestHole) > 3:
                        if np.linalg.norm(grid-SecondBiggestHole) > 3:
                            ThirdFurthest = SecondFurthest
                            SecondFurthest = ClosestDistanceForCurrentGridPoint
                            ThirdBiggestHole = SecondBiggestHole
                            SecondBiggestHole = grid
                        else:
                            SecondFurthest = ClosestDistanceForCurrentGridPoint
                            SecondBiggestHole=grid
                elif ClosestDistanceForCurrentGridPoint > ThirdFurthest:
                    if np.linalg.norm(grid-BiggestHole) > 3:
                        if np.linalg.norm(grid-SecondBiggestHole) > 3:
                            ThirdFurthest = ClosestDistanceForCurrentGridPoint
                            ThirdBiggestHole = grid
            # revert before looping to next grid value
            ClosestDistanceForCurrentGridPoint = 100
            CheckIfInsidePeptide = [0, 0, 0, 0, 0, 0]
            
print(FurthestAADistance)
print(BiggestHole)
