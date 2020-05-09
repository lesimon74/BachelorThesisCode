# Search how many C-alpha there are within a certain radius in each timeframe.

searchBondedNeighbours = False
radius1 = 5
radius2 = 6
radius3 = 7
radius4 = 8
radius5 = 9
radius6 = 10
radius7 = 11
radius8 = 12
radius9 = 13
radius10 = 14

#searchForHowManyNextNeighbours = 5

Moviness = np.zeros(numAA) # save a value for every aa to calculate a moviness value
MovinessStd1 = np.zeros(len(Moviness)) # Standard deviation of avgDist
MovinessStd2 = np.zeros(len(Moviness)) # Standard deviation of avgDist
MovinessStd3 = np.zeros(len(Moviness)) # Standard deviation of avgDist
MovinessStd4 = np.zeros(len(Moviness)) # Standard deviation of avgDist
MovinessStd5 = np.zeros(len(Moviness)) # Standard deviation of avgDist
MovinessStd6 = np.zeros(len(Moviness)) # Standard deviation of avgDist
MovinessStd7 = np.zeros(len(Moviness)) # Standard deviation of avgDist
MovinessStd8 = np.zeros(len(Moviness)) # Standard deviation of avgDist
MovinessStd9 = np.zeros(len(Moviness)) # Standard deviation of avgDist
MovinessStd10 = np.zeros(len(Moviness)) # Standard deviation of avgDist
NumInRadius1 = np.zeros(len(trajectory)) # gives 50000 here (here 1000)
NumInRadius2 = np.zeros(len(NumInRadius1))
NumInRadius3 = np.zeros(len(NumInRadius1))
NumInRadius4 = np.zeros(len(NumInRadius1))
NumInRadius5 = np.zeros(len(NumInRadius1))
NumInRadius6 = np.zeros(len(NumInRadius1))
NumInRadius7 = np.zeros(len(NumInRadius1))
NumInRadius8 = np.zeros(len(NumInRadius1))
NumInRadius9 = np.zeros(len(NumInRadius1))
NumInRadius10 = np.zeros(len(NumInRadius1))
tempStoreDistances = np.zeros(numAA)


for aa in range(0, numAA):
    frameNr = 0
    for frame in universe.trajectory:
        ca = universe.select_atoms('name CA')
        cartesians = ca.positions
        for aa2 in range(0, numAA):
            tempStoreDistances[aa2] = np.sqrt(np.sum(np.square(cartesians[aa]-cartesians[aa2]))) #store all distances for aa2.
        counter1 = 0
        counter2 = 0
        counter3 = 0
        counter4 = 0
        counter5 = 0
        counter6 = 0
        counter7 = 0
        counter8 = 0
        counter9 = 0
        counter10 = 0
        for i in range(0, numAA):
            if tempStoreDistances[i] < radius1:
                counter1 = counter1 + 1
            if tempStoreDistances[i] < radius2:
                counter2 = counter2 + 1
            if tempStoreDistances[i] < radius3:
                counter3 = counter3 + 1
            if tempStoreDistances[i] < radius4:
                counter4 = counter4 + 1
            if tempStoreDistances[i] < radius5:
                counter5 = counter5 + 1
            if tempStoreDistances[i] < radius6:
                counter6 = counter6 + 1
            if tempStoreDistances[i] < radius7:
                counter7 = counter7 + 1
            if tempStoreDistances[i] < radius8:
                counter8 = counter8 + 1
            if tempStoreDistances[i] < radius9:
                counter9 = counter9 + 1
            if tempStoreDistances[i] < radius10:
                counter10 = counter10 + 1
        NumInRadius1[frameNr] = counter1
        NumInRadius2[frameNr] = counter2
        NumInRadius3[frameNr] = counter3
        NumInRadius4[frameNr] = counter4
        NumInRadius5[frameNr] = counter5
        NumInRadius6[frameNr] = counter6
        NumInRadius7[frameNr] = counter7
        NumInRadius8[frameNr] = counter8
        NumInRadius9[frameNr] = counter9
        NumInRadius10[frameNr] = counter10
        frameNr = frameNr + 1
    MovinessStd1[aa] = np.std(NumInRadius1)
    MovinessStd2[aa] = np.std(NumInRadius2)
    MovinessStd3[aa] = np.std(NumInRadius3)
    MovinessStd4[aa] = np.std(NumInRadius4)
    MovinessStd5[aa] = np.std(NumInRadius5)
    MovinessStd6[aa] = np.std(NumInRadius6)
    MovinessStd7[aa] = np.std(NumInRadius7)
    MovinessStd8[aa] = np.std(NumInRadius8)
    MovinessStd9[aa] = np.std(NumInRadius9)
    MovinessStd10[aa] = np.std(NumInRadius10)
    # print(aa) # To track progress while code is runnning.
