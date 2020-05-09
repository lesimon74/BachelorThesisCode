universe = Universe(pdb_, xtc_)
trajectory = universe.trajectory

ca = universe.select_atoms('name CA')
numAA = len(universe.select_atoms('name CA'))
print(numAA)
