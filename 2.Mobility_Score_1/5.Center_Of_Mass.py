mobility = np.zeros(numAA)
avgDist = np.zeros(len(trajectory))
tempStoreDistances = np.zeros(11)
for aa in range(5, numAA-5):
    frameNr = 0
    for frame in universe.trajectory:
        cartesians = universe.residues[aa].atoms.center_of_mass()
        for aa2 in range(aa-5, aa+5):
            cartesians2 = universe.residues[aa2].atoms.center_of_mass()
            tempStoreDistances[aa2-(aa-5)] = np.linalg.norm(cartesians-cartesians2)
        avgDist[frameNr] = np.sum(tempStoreDistances)
        frameNr = frameNr + 1
    print(aa)
    mobility[aa] = np.std(avgDist)
