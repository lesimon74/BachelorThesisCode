# Correct for the ends
UseMoviness = False

# Lower-bound correction
SmallestMovinessStd = 99999
for x in range(0, numAA):
    if SmallestMovinessStd > MovinessStd[x]:
        SmallestMovinessStd = MovinessStd[x]
for y in range(0, numAA):
    MovinessStd[y] = MovinessStd[y] - SmallestMovinessStd

SetEnds = np.array([0, 1, 2, numAA-3, numAA-2, numAA-1])
MovinessStd[SetEnds] = np.mean(MovinessStd)

# For 6el6
#SetEnds2 = np.array([244, 245, 246, 247, 248, 249])
#MovinessStd[SetEnds2] = np.mean(MovinessStd)
# For 1t3r
#SetToMean3 = np.array([96, 97, 98, 99, 100, 101])
#MovinessStd[SetToMean3] = np.mean(MovinessStd)

# Norm with max = 1
maxValue = 0
for x in MovinessStd:
    if x > maxValue:
        maxValue = x
for y in range(0, numAA):
    MovinessStd[y] = MovinessStd[y] / maxValue

# Calculate pearson correlation
from scipy.stats.stats import pearsonr
print(pearsonr(BindingSite, MovinessStd))

for z in range (0, numAA):
    print(MovinessStd[z])

