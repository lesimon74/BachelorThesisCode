# compute distance histogram and get wasserstein distance
from scipy.stats import wasserstein_distance
print(numAA)

distancePerBin = 20/50

mobility = np.zeros(numAA) # save a value for every aa to calculate a mobility value
mobilityStd = np.zeros(numAA)
avgDist = np.zeros(len(trajectory))
StoreDistances = np.zeros(numAA)
prevBins = np.zeros(50)
currentBins = np.zeros(50)
for aa in range(0, numAA):
    frameNr = 0
    for frame in universe.trajectory:
        ca = universe.select_atoms('name CA')
        cartesians = ca.positions[aa]
        if frameNr == 0:
            for aa2 in range(0, numAA):
                cartesians2 = ca.positions[aa2]
                StoreDistances[aa2] = np.linalg.norm(cartesians-cartesians2)
            # clean bins
            for y in range(0, 50):
                prevBins[y] = 0
            for x in range(0, numAA):
                binStuff = int(StoreDistances[x] / distancePerBin)
                if(binStuff < 50):
                    prevBins[binStuff] = prevBins[binStuff] + 1
        else:
            for aa2 in range(0, numAA):
                cartesians2 = ca.positions[aa2]
                StoreDistances[aa2] = np.linalg.norm(cartesians-cartesians2)
            #clean bins
            for x in range(0, 50):
                currentBins[x] = 0
            for x in range(0, numAA):
                binStuff = int(StoreDistances[x] / distancePerBin)
                if(binStuff < 50):
                    currentBins[binStuff] = currentBins[binStuff] + 1
            ### Here compare the histograms
            avgDist[frameNr] = wasserstein_distance(prevBins, currentBins)/((np.sum(prevBins)+np.sum(currentBins))/1000)
            ###
            for aaIndex in range(0, 50):
                prevBins[aaIndex] = currentBins[aaIndex]
        frameNr = frameNr + 1
    print(aa)
    mobility[aa] = np.mean(avgDist)
    mobilityStd[aa] = np.std(avgDist)
