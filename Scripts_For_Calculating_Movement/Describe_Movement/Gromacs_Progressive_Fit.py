# Fit progressive

Moviness = np.zeros(numAA) # calculate moviness for every aa.
MovinessStd = np.zeros(len(Moviness)) # Standard deviation of avgDist
AaPositions = np.ndarray(shape=(numAA,3), dtype=float)
PrevAaPositions = np.ndarray(shape=(numAA,3), dtype=float)
frameNr = 0
for frame in universe.trajectory:
    if frameNr == 0:
        for atomID in range(0, numAA):
            PrevAaPositions[atomID] = universe.residues[atomID].atoms.center_of_mass()
    else:
        for atomID in range(0, numAA):
            AaPositions[atomID] = universe.residues[atomID].atoms.center_of_mass()
            Moviness[atomID] = Moviness[atomID] + np.linalg.norm(AaPositions[atomID] - PrevAaPositions[atomID])
            PrevAaPositions[atomID] = AaPositions[atomID]
    frameNr = frameNr + 1
    
print(Moviness)
