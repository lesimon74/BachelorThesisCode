# If the trajectory file to analyze has 500 timeframes
# For simplicity only the information about 11 equidistant timeframes are taken into account.
print(len(universe.trajectory))
frameNr = 0

frameZero = np.ndarray(shape=(numAA,3), dtype=float)
frame49 = np.ndarray(shape=(numAA,3), dtype=float)
frame99 = np.ndarray(shape=(numAA,3), dtype=float)
frame149 = np.ndarray(shape=(numAA,3), dtype=float)
frame199 = np.ndarray(shape=(numAA,3), dtype=float)
frame249 = np.ndarray(shape=(numAA,3), dtype=float)
frame299 = np.ndarray(shape=(numAA,3), dtype=float)
frame349 = np.ndarray(shape=(numAA,3), dtype=float)
frame399 = np.ndarray(shape=(numAA,3), dtype=float)
frame449 = np.ndarray(shape=(numAA,3), dtype=float)
frame499 = np.ndarray(shape=(numAA,3), dtype=float)

for ts in universe.trajectory:
    if frameNr == 0:
        for aa in range(0, numAA):
            cartesians = universe.residues[aa].atoms.center_of_mass()
            frameZero[aa] = cartesians
    if frameNr == 49:
        for aa in range(0, numAA):
            cartesians = universe.residues[aa].atoms.center_of_mass()
            frame49[aa] = cartesians
    if frameNr == 99:
        for aa in range(0, numAA):
            cartesians = universe.residues[aa].atoms.center_of_mass()
            frame99[aa] = cartesians
    if frameNr == 149:
        for aa in range(0, numAA):
            cartesians = universe.residues[aa].atoms.center_of_mass()
            frame149[aa] = cartesians
    if frameNr == 199:
        for aa in range(0, numAA):
            cartesians = universe.residues[aa].atoms.center_of_mass()
            frame199[aa] = cartesians
    if frameNr == 249:
        for aa in range(0, numAA):
            cartesians = universe.residues[aa].atoms.center_of_mass()
            frame249[aa] = cartesians
    if frameNr == 299:
        for aa in range(0, numAA):
            cartesians = universe.residues[aa].atoms.center_of_mass()
            frame299[aa] = cartesians
    if frameNr == 349:
        for aa in range(0, numAA):
            cartesians = universe.residues[aa].atoms.center_of_mass()
            frame349[aa] = cartesians
    if frameNr == 399:
        for aa in range(0, numAA):
            cartesians = universe.residues[aa].atoms.center_of_mass()
            frame399[aa] = cartesians
    if frameNr == 449:
        for aa in range(0, numAA):
            cartesians = universe.residues[aa].atoms.center_of_mass()
            frame449[aa] = cartesians
    if frameNr == 499:
        for aa in range(0, numAA):
            cartesians = universe.residues[aa].atoms.center_of_mass()
            frame499[aa] = cartesians
    frameNr = frameNr + 1
