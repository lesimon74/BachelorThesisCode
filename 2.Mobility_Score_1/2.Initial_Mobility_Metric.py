mobility = np.zeros(numAA) # save a mobility value for every aa
avgDist = np.zeros(len(trajectory))
tempStoreDistances = np.zeros(11)
for aa in range(5, numAA-5):
    frameNr = 0
    for frame in universe.trajectory:
        ca = universe.select_atoms('name CA')
        cartesians = ca.positions[aa]
        for aa2 in range(aa-5, aa+5):
            cartesians2 = ca.positions[aa2]
            tempStoreDistances[aa2-(aa-5)] = np.linalg.norm(cartesians-cartesians2)
        avgDist[frameNr] = np.sum(tempStoreDistances)
        frameNr = frameNr + 1
    print(aa) # To keep track of the calculation for the impatient people.
    mobility[aa] = np.std(avgDist)
