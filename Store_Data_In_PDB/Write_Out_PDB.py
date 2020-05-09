print(len(Moviness))
universeCopy1 = universe
universeCopy1.add_TopologyAttr('tempfactors')
counter = 0
residueNumber = 0
distances = np.zeros(universeCopy1.atoms.n_atoms)

with Writer("1abfNewNormal.pdb", multiframe=False, bonds=None, n_atoms=universeCopy1.atoms.n_atoms) as PDB:
    universeCopy1.trajectory[0]
    for res in universeCopy1.residues:
        if res.resname == "SOL":
            break
        atomNum = len(res.atoms)
        for x in range(0, atomNum):
            distances[counter+x] = Moviness[residueNumber]
        counter = counter + atomNum
        residueNumber = residueNumber + 1
    universeCopy1.atoms.tempfactors = distances
    PDB.write(universeCopy1.atoms)
print(distances)
