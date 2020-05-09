# compare to r instead of delta r
# center of mass
# spatially closest 10 neighbours
searchBondedNeighbours = False
searchsearchForHowManyNextNeighbours = 10

Moviness = np.zeros(numAA) # save a value for every aa to calculate a moviness value
MovinessStd = np.zeros(len(Moviness)) # Standard deviation of avgDist
avgDist = np.zeros(len(trajectory))
tempStoreDistances = np.zeros(numAA)
for aa in range(0, numAA):
    frameNr = 0
    atomID = aa
    for frame in universe.trajectory:
        cartesians = universe.residues[aa].atoms.center_of_mass()
        
        for aa2 in range(0, numAA):
            cartesians2 = universe.residues[aa2].atoms.center_of_mass()
            tempStoreDistances[aa2] = np.sqrt(np.sum(np.square(cartesians-cartesians2)))
        sortedStuff = np.sort(tempStoreDistances)
        avgDist[frameNr] = sortedStuff[1] + sortedStuff[2] + sortedStuff[3] + sortedStuff[4] + sortedStuff[5] + sortedStuff[6] + sortedStuff[7] + sortedStuff[8] + sortedStuff[9] + sortedStuff[10] # not sortedStuff[0] because distance to itself is zero
        frameNr = frameNr + 1
    print(aa)
    Moviness[aa] = np.mean(avgDist) # Here this value is useless
    MovinessStd[aa] = np.std(avgDist)
