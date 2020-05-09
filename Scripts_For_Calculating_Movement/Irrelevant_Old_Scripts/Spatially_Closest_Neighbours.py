# Search for spatially closest neighbours

searchBondedNeighbours = False
searchForHowManyNextNeighbours = 5

Moviness = np.zeros(numAA) # save a value for every aa to calculate a moviness value
MovinessStd = np.zeros(len(Moviness)) # Standard deviation of avgDist
avgDist = np.zeros(len(trajectory)) # gives 50000 here (here 1000)
tempStoreDistances = np.zeros(165)

        
for aa in range(0, 165):
    frameNr = 0
    for frame in universe.trajectory:
        ca = universe.select_atoms('name CA')
        cartesians = ca.positions
        for aa2 in range(0,165):
            tempStoreDistances[aa2] = np.sqrt(np.sum(np.square(cartesians[aa]-cartesians[aa2])))
        sortedStuff = np.sort(tempStoreDistances)
        avgDist[frameNr] = sortedStuff[1] + sortedStuff[2] + sortedStuff[3] + sortedStuff[4] + sortedStuff[5] + sortedStuff[6] + sortedStuff[7] + sortedStuff[8] # not sortedStuff[0] because distance to itself is zero
        frameNr = frameNr + 1
    Moviness[aa] = np.mean(avgDist)
    MovinessStd[aa] = np.std(avgDist)
    print(aa)
