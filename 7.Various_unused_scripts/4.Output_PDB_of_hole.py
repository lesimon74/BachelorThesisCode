# Output pdb of hole
Pocket = np.zeros(numAA)
PocketIndex = np.array([int(round(sortedStuff[0][1])), int(round(sortedStuff[1][1])), int(round(sortedStuff[2][1])), int(round(sortedStuff[3][1])), int(round(sortedStuff[4][1])), int(round(sortedStuff[5][1])), int(round(sortedStuff[6][1])), int(round(sortedStuff[7][1])), int(round(sortedStuff[8][1])), int(round(sortedStuff[9][1]))])
Pocket[PocketIndex] = 1
print(Pocket)
universeCopy1 = universe
universeCopy1.add_TopologyAttr('tempfactors')
counter = 0
residueNumber = 0
distances = np.zeros(universeCopy1.atoms.n_atoms)

with Writer("6el6_Holes.pdb", multiframe=False, bonds=None, n_atoms=universeCopy1.atoms.n_atoms) as PDB:
    universeCopy1.trajectory[0]
    for res in universeCopy1.residues:
        if res.resname == "SOL":
            break
        atomNum = len(res.atoms)
        for x in range(0, atomNum):
            distances[counter+x] = Pocket[residueNumber]
        counter = counter + atomNum
        residueNumber = residueNumber + 1
    universeCopy1.atoms.tempfactors = distances
    PDB.write(universeCopy1.atoms)
print(distances)

from scipy.stats.stats import pearsonr
print(pearsonr(BindingSite, Pocket))
