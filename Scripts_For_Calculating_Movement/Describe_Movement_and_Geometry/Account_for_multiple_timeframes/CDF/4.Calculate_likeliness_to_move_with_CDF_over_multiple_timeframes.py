# center of mass
#  not wasserstein, but with cumulative distribution function (modified version for simplicity
# and faster computation)

distancePerBin = 20/50

Moviness = np.zeros(numAA) # save a value for every aa to calculate a moviness value
avgDist = np.zeros(len(trajectory))
StoreDistances = np.zeros(numAA)
currentBins = np.zeros(50)
CDFValues = np.zeros(11)

for aa in range(0, numAA):
    frameNr = 0
    for frame in universe.trajectory:
        cartesians = universe.residues[aa].atoms.center_of_mass()
        for aa2 in range(0, numAA):
            cartesians2 = universe.residues[aa2].atoms.center_of_mass()
            StoreDistances[aa2] = np.linalg.norm(cartesians-cartesians2)
        # clear bins
        currentBins = np.zeros(50)
        for x in range(0, numAA):
            binStuff = int(StoreDistances[x] / distancePerBin)
            if (binStuff < 50):
                currentBins[binStuff] = currentBins[binStuff] + 1
        #Modify bins for CDF
        for x in range(1, 50):
            currentBins[x] = currentBins[x-1] + currentBins[x]
        CDFValues[0] = np.sum(np.abs(Bins0CDF[aa] - currentBins))
        CDFValues[1] = np.sum(np.abs(Bins1CDF[aa] - currentBins))
        CDFValues[2] = np.sum(np.abs(Bins2CDF[aa] - currentBins))
        CDFValues[3] = np.sum(np.abs(Bins3CDF[aa] - currentBins))
        CDFValues[4] = np.sum(np.abs(Bins4CDF[aa] - currentBins))
        CDFValues[5] = np.sum(np.abs(Bins5CDF[aa] - currentBins))
        CDFValues[6] = np.sum(np.abs(Bins6CDF[aa] - currentBins))
        CDFValues[7] = np.sum(np.abs(Bins7CDF[aa] - currentBins))
        CDFValues[8] = np.sum(np.abs(Bins8CDF[aa] - currentBins))
        CDFValues[9] = np.sum(np.abs(Bins9CDF[aa] - currentBins))
        CDFValues[10] = np.sum(np.abs(Bins10CDF[aa] - currentBins))
        avgDist[frameNr] = np.mean(CDFValues)
        frameNr = frameNr + 1
    print(aa)
    Moviness[aa] = np.mean(avgDist)
