bindingSelection = bindingSites1abf # Only this value and "mobility" need to be modified when switching to other peptides
site = ca.positions[bindingSelection]
print(site)
sumX = 0
sumY = 0
sumZ = 0
for aaIndex in range(0, len(site)):
    sumX = sumX + site[aaIndex][0]
    sumY = sumY + site[aaIndex][1]
    sumZ = sumZ + site[aaIndex][2]
meanOfBindingSite = np.array([sumX/len(site), sumY/len(site), sumZ/len(site)])
print(len(site))
print(meanOfBindingSite)

distances = np.zeros(shape=(numAA, 2))
for aaIndex in range(0, numAA):
    distances[aaIndex][0] = np.linalg.norm(meanOfBindingSite - ca.positions[aaIndex])
    distances[aaIndex][1] = aaIndex
distances = distances[distances[:,0].argsort()]
print(distances)

closeButNotBindingSite = np.zeros(len(site))
iterator = 0
for x in range(0, numAA):
    if np.isin(distances[x][1], bindingSelection) == False:
        closeButNotBindingSite[iterator] = distances[x][1]
        iterator = iterator + 1
        if iterator >= len(closeButNotBindingSite):
            break

print(closeButNotBindingSite)
