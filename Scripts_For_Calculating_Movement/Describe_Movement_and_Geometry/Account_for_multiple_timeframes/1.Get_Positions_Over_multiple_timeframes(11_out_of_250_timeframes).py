# If the trajectory file to analyze has 250 timeframes
# For simplicity only the information about 11 equidistant timeframes are taken into account.
print(len(universe.trajectory))
frameNr = 0

frameZero = np.ndarray(shape=(numAA,3), dtype=float)
frame49 = np.ndarray(shape=(numAA,3), dtype=float)
frame99 = np.ndarray(shape=(numAA,3), dtype=float)
frame149 = np.ndarray(shape=(numAA,3), dtype=float)
frame199 = np.ndarray(shape=(numAA,3), dtype=float)
frame249 = np.ndarray(shape=(numAA,3), dtype=float)
frame24 = np.ndarray(shape=(numAA,3), dtype=float)
frame74 = np.ndarray(shape=(numAA,3), dtype=float)
frame124 = np.ndarray(shape=(numAA,3), dtype=float)
frame174 = np.ndarray(shape=(numAA,3), dtype=float)
frame224 = np.ndarray(shape=(numAA,3), dtype=float)

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
    if frameNr == 24:
        for aa in range(0, numAA):
            cartesians = universe.residues[aa].atoms.center_of_mass()
            frame24[aa] = cartesians
    if frameNr == 74:
        for aa in range(0, numAA):
            cartesians = universe.residues[aa].atoms.center_of_mass()
            frame74[aa] = cartesians
    if frameNr == 124:
        for aa in range(0, numAA):
            cartesians = universe.residues[aa].atoms.center_of_mass()
            frame124[aa] = cartesians
    if frameNr == 174:
        for aa in range(0, numAA):
            cartesians = universe.residues[aa].atoms.center_of_mass()
            frame174[aa] = cartesians
    if frameNr == 224:
        for aa in range(0, numAA):
            cartesians = universe.residues[aa].atoms.center_of_mass()
            frame224[aa] = cartesians
    frameNr = frameNr + 1
    
# Renamer so that code for trajectories with 500 frames can be used for trajectories with 250 frames
# This works, because the order of timeframes doesn't matter.
frame299 = frame24
frame349 = frame74
frame399 = frame124
frame449 = frame174
frame499 = frame224
