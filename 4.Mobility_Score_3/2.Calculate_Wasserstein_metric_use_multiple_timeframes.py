# compute distance histogram and get wasserstein distance, uses multiple timeframes per amino acid and timeframe.
from scipy.stats import wasserstein_distance
print(numAA)

distancePerBin = 20/50

mobility = np.zeros(numAA) # save a value for every aa to calculate a moviness value
mobilityStd = np.zeros(numAA)
avgDist = np.zeros(len(trajectory))
StoreDistances = np.zeros(numAA)
prevBins = np.zeros(50)
currentBins = np.zeros(50)
ca = universe.select_atoms('name CA')
for aa in range(0, numAA):
    frameNr = 0
    for frame in universe.trajectory:
        cartesians = ca.positions[aa]
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
        for frameSelection in range(50, 500, 50):
            universe.trajectory[frameNr - frameSelection]
            cartesians = ca.positions[aa]
            for aa2 in range(0, numAA):
                cartesians2 = ca.positions[aa2]
                StoreDistances[aa2] = np.linalg.norm(cartesians-cartesians2)
                #clean bins
            for x in range(0, 50):
                prevBins[x] = 0
            for x in range(0, numAA):
                binStuff = int(StoreDistances[x] / distancePerBin)
                if(binStuff < 50):
                    prevBins[binStuff] = prevBins[binStuff] + 1

            ### Here compare the histograms
            avgDist[frameNr] = avgDist[frameNr] + wasserstein_distance(prevBins, currentBins)/((np.sum(prevBins)+np.sum(currentBins))/1000)
            ###
        universe.trajectory[frameNr]
        frameNr = frameNr + 1
    print(aa)
    mobility[aa] = np.mean(avgDist)
    mobilityStd[aa] = np.std(avgDist)
    for x in range(0, len(trajectory)):
        avgDist[x] = 0
