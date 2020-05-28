# Improved version of OldFit.py. Now it doesn't only take the movement of the previous timeframe into account. This way it can differentiate between bigger and smaller conformational changes.

mobility2 = np.zeros(numAA)
AaPositions = np.ndarray(shape=(numAA,3), dtype=float)
PrevAaPositions = np.ndarray(shape=(numAA,3), dtype=float)
frameNr = 0
for frame in universe.trajectory:
    for frameSelection in range(50, 500, 25):
        for aa in range(0, numAA):
            AaPositions[aa] = universe.residues[aa].atoms.center_of_mass()
        universe.trajectory[frameNr - frameSelection]
        for aa in range(0, numAA):
            PrevAaPositions[aa] = universe.residues[aa].atoms.center_of_mass()
        universe.trajectory[frameNr]
        for aa in range(0, numAA):
            mobility2[aa] = mobility2[aa] + np.linalg.norm(AaPositions[aa] - PrevAaPositions[aa])
    frameNr = frameNr + 1
    # Prints progress to make visible if program works or is hanging
    if frameNr % 20 == 0:
        print(universe.trajectory.frame)
print(mobility2)
