# not prev. frame version, uses 10 equidistant timeframes
# center of mass
# compute distance histogram and get wasserstein distance
from scipy.stats import wasserstein_distance

distancePerBin = 20/50

Moviness = np.zeros(numAA) # save a value for every aa to calculate a moviness value
avgDist = np.zeros(len(trajectory))
StoreDistances = np.zeros(numAA)
currentBins = np.zeros(50)
wassersteinValues = np.zeros(11)

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
        wassersteinValues[0] = wasserstein_distance(Bins0[aa], currentBins)
        wassersteinValues[1] = wasserstein_distance(Bins1[aa], currentBins)
        wassersteinValues[2] = wasserstein_distance(Bins2[aa], currentBins)
        wassersteinValues[3] = wasserstein_distance(Bins3[aa], currentBins)
        wassersteinValues[4] = wasserstein_distance(Bins4[aa], currentBins)
        wassersteinValues[5] = wasserstein_distance(Bins5[aa], currentBins)
        wassersteinValues[6] = wasserstein_distance(Bins6[aa], currentBins)
        wassersteinValues[7] = wasserstein_distance(Bins7[aa], currentBins)
        wassersteinValues[8] = wasserstein_distance(Bins8[aa], currentBins)
        wassersteinValues[9] = wasserstein_distance(Bins9[aa], currentBins)
        wassersteinValues[10] = wasserstein_distance(Bins10[aa], currentBins)
        avgDist[frameNr] = np.mean(wassersteinValues)
        frameNr = frameNr + 1
    print(aa)
    Moviness[aa] = np.mean(avgDist)
