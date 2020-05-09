# center of mass
# compute distance histogram and get wasserstein distance
from scipy.stats import wasserstein_distance

distancePerBin = 20/50

Moviness = np.zeros(numAA) # save a value for every aa to calculate a moviness value
MovinessStd = np.zeros(len(Moviness))
avgDist = np.zeros(len(trajectory))
StoreDistances = np.zeros(numAA)
prevBins = np.zeros(50)
currentBins = np.zeros(50)
for aa in range(0, numAA):
    frameNr = 0
    for frame in universe.trajectory:
        cartesians = universe.residues[aa].atoms.center_of_mass()
        if frameNr == 0:
            for aa2 in range(0, numAA):
                cartesians2 = universe.residues[aa2].atoms.center_of_mass()
                StoreDistances[aa2] = np.sqrt(np.sum(np.square(cartesians-cartesians2)))
            # clean bins
            for y in range(0, 50):
                prevBins[y] = 0
            for x in range(0, numAA):
                binStuff = int(StoreDistances[x] / distancePerBin)
                if(binStuff < 50):
                    prevBins[binStuff] = prevBins[binStuff] + 1
        else:
            for aa2 in range(0, numAA):
                cartesians2 = universe.residues[aa2].atoms.center_of_mass()
                StoreDistances[aa2] = np.sqrt(np.sum(np.square(cartesians-cartesians2)))
            #clean bins
            for x in range(0, 50):
                currentBins[x] = 0
            for x in range(0, numAA):
                binStuff = int(StoreDistances[x] / distancePerBin)
                if(binStuff < 50):
                    currentBins[binStuff] = currentBins[binStuff] + 1
            ### Here compare the histograms
            avgDist[frameNr] = wasserstein_distance(prevBins, currentBins)
            ###
            for aaIndex in range(0, 50):
                prevBins[aaIndex] = currentBins[aaIndex]
        frameNr = frameNr + 1
    print(aa)
    Moviness[aa] = np.mean(avgDist)
    MovinessStd[aa] = np.std(avgDist) # Here this value is useless
