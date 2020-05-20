mobility = np.zeros(numAA)
avgDist = np.zeros(len(trajectory))
tempStoreDistances = np.zeros(numAA)
for aa in range(0, numAA):
    frameNr = 0
    for frame in universe.trajectory:
        ca = universe.select_atoms('name CA')
        cartesians = ca.positions[aa]
        for aa2 in range(0, numAA):
            cartesians2 = ca.positions[aa2]
            tempStoreDistances[aa2] = np.linalg.norm(cartesians-cartesians2)
        sortedStuff = np.sort(tempStoreDistances)
        avgDist[frameNr] = sortedStuff[1] + sortedStuff[2] + sortedStuff[3] + sortedStuff[4] + sortedStuff[5] # not sortedStuff[0] because distance to itself is zero
        frameNr = frameNr + 1
    print(aa)
    mobility[aa] = np.std(avgDist)
