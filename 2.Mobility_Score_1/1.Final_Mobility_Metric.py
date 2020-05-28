mobility = np.zeros(numAA) # save a value for every aa to calculate a mobility value
avgDist = np.zeros(len(trajectory))
tempStoreDistances = np.zeros(numAA)
for aa in range(0, numAA):
    frameNr = 0
    for frame in universe.trajectory:
        ca = universe.select_atoms('name CA')
        cartesians = ca.positions
        for aa2 in range(0, numAA):
            tempStoreDistances[aa2] = np.linalg.norm(cartesians[aa]-cartesians[aa2])
        sortedStuff = np.sort(tempStoreDistances)
        avgDist[frameNr] = sortedStuff[1] + sortedStuff[2] + sortedStuff[3] + sortedStuff[4] + sortedStuff[5] + sortedStuff[6] + sortedStuff[7] + sortedStuff[8] + sortedStuff[9] + sortedStuff[10] # not sortedStuff[0] because distance to itself is zero
        frameNr = frameNr + 1
    print(aa)
    mobility[aa] = np.std(avgDist)
