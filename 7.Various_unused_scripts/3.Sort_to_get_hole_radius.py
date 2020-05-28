position = BiggestHole
Dist = np.ndarray(shape=(numAA,2), dtype=float)
countercc = 0
ca = universe.select_atoms('name CA')
for pos in ca.positions:
    Dist[countercc][0] = np.linalg.norm(pos - position)
    Dist[countercc][1] = countercc
    countercc = countercc + 1
sortedStuff = Dist[Dist[:,0].argsort()]
print(sortedStuff)
