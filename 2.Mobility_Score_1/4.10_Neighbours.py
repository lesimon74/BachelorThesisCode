mobility = np.zeros(numAA)
avgDist = np.zeros(len(trajectory))
tempStoreDistances = np.zeros(21)
for aa in range(10, numAA-10):
    frameNr = 0
    for frame in universe.trajectory:
        ca = universe.select_atoms('name CA')
        cartesians = ca.positions[aa]
        for aa2 in range(aa-10, aa+10):
            cartesians2 = ca.positions[aa2]
            tempStoreDistances[aa2-(aa-10)] = np.linalg.norm(cartesians-cartesians2)
        avgDist[frameNr] = np.sum(tempStoreDistances)
        frameNr = frameNr + 1
    print(aa)
    mobility[aa] = np.std(avgDist)
