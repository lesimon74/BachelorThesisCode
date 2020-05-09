# New Fit progressive

Moviness = np.zeros(numAA) # calculate moviness for every aa
AaPositions = np.ndarray(shape=(numAA,3), dtype=float)
PrevAaPositions = np.ndarray(shape=(numAA,3), dtype=float)
frameNr = 0
for frame in universe.trajectory:
    for aa in range(0, numAA):
        AaPositions[aa] = universe.residues[aa].atoms.center_of_mass()
    universe.trajectory[frameNr - 50]
    for aa in range(0, numAA):
        PrevAaPositions[aa] = universe.residues[aa].atoms.center_of_mass()
    universe.trajectory[frameNr]
    for aa in range(0, numAA):
        Moviness[aa] = Moviness[aa] + np.linalg.norm(AaPositions[aa] - PrevAaPositions[aa])
    frameNr = frameNr + 1
    # Prints progress to make visible if program works or is hanging
    if frameNr % 50 == 0:
        print(universe.trajectory.frame)

print(Moviness)
