# Don't forget to uncomment SetToMean2 and SetToMean3 for certain peptides!

# Lower-bound correction
SmallestMobility = 99999
for x in range(0, numAA):
    if SmallestMobility > mobility[x]:
        SmallestMobility = mobility[x]
for y in range(0, numAA):
    mobility[y] = mobility[y] - Smallestmobility

# The ends naturally move a lot, so they are manually set to mean value.
SetToMean = np.array([0, 1, 2, numAA-3, numAA-2, numAA-1])
mobility[SetToMean] = np.mean(mobility)

# Manually modify the mobility value of amino acids at the end of a chain.

# For 6el6
#SetToMean2 = np.array([244, 245, 246, 247, 248, 249])
#mobility[SetToMean2] = np.mean(mobility)

# For 1t3r
#SetToMean3 = np.array([96, 97, 98, 99, 100, 101])
#mobility[SetToMean3] = np.mean(mobility)

# Calculate norm with max = 1
maxValue = 0
for x in mobility:
    if x > maxValue:
        maxValue = x
for y in range(0, numAA):
    mobility[y] = mobility[y] / maxValue

# Calculate pearson correlation
from scipy.stats.stats import pearsonr
print(pearsonr(BindingSite, mobility))

for z in range (0, numAA):
    print(mobility[z])
