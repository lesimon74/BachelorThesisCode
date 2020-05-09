# search for ten next bonds (20 total)
searchBondedNeighbours = True # if false use next cell
searchForHowManyNextNeighbours = 10

atomIDdistances = np.zeros(2*searchForHowManyNextNeighbours+1) # store the reference distance values in here.
Moviness = np.zeros(numAA) # save a value for every aa to calculate a moviness value
MovinessStd = np.zeros(len(Moviness)) # Standard deviation of avgDist
avgDist = np.zeros(len(trajectory)-1) # gives 50000 here (here 1000)
for a in range(15, 155): # To set later to correct value
    frameNr = 0
    atomID = a
    for frame in universe.trajectory:
        ca = universe.select_atoms('name CA')
        cartesians = ca.positions
        if frameNr == 0:
            for x in range(atomID-searchForHowManyNextNeighbours, atomID+searchForHowManyNextNeighbours+1):
                dings = np.sqrt(np.sum(np.square(cartesians[x]-cartesians[atomID]))) #distance to atom Nr. atomID
                atomIDdistances[x-(atomID-searchForHowManyNextNeighbours)] = dings
            frameNr = frameNr + 1
        else:
            atomIDdistancesTemp = np.zeros(len(atomIDdistances))
            for x in range(atomID-searchForHowManyNextNeighbours, atomID+searchForHowManyNextNeighbours+1):
                dings = np.sqrt(np.sum(np.square(cartesians[x]-cartesians[atomID]))) #distance to atom Nr. atomID
                atomIDdistancesTemp[x-(atomID-searchForHowManyNextNeighbours)] = dings
            avgDist[frameNr-1] = np.sum(abs(atomIDdistancesTemp-atomIDdistances)) #first trajectory used as reference
            frameNr = frameNr + 1
    print(a)
    Moviness[a] = np.mean(avgDist)
    MovinessStd[a] = np.std(avgDist)
