# Lower-bound correction
Moviness = mobility
nummAA = len(mobility)
SmallestMoviness = 99999
for x in range(0, numAA):
    if SmallestMoviness > Moviness[x]:
        SmallestMoviness = Moviness[x]
for y in range(0, numAA):
    Moviness[y] = Moviness[y] - SmallestMoviness

SetEnds = np.array([0, 1, 2, numAA-3, numAA-2, numAA-1])
Moviness[SetEnds] = np.mean(Moviness)

# For 6el6
SetToMean2 = np.array([244, 245, 246, 247, 248, 249])
Moviness[SetToMean2] = np.mean(Moviness)

# For 1t3r
#SetToMean3 = np.array([96, 97, 98, 99, 100, 101])
#Moviness[SetToMean3] = np.mean(Moviness)

# Norm with max = 1
maxValue = 0
for x in Moviness:
    if x > maxValue:
        maxValue = x
for y in range(0, numAA):
    Moviness[y] = Moviness[y] / maxValue

# Calculate pearson correlation
from scipy.stats.stats import pearsonr
print(pearsonr(BindingSite, Moviness))
mobility = Moviness
