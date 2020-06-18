# Don't forget to uncomment SetToMean2 and SetToMean3 for certain peptides!

# Normalize
Moviness = mobility
numAA = len(Moviness) # Set manually, or else it can lead to mistakes.
mean = np.mean(Moviness)

SetEnds = np.array([0, 1, 2, numAA-3, numAA-2, numAA-1])
SetEnds2 = np.array([0, 1, 2, 3, 4, numAA-5, numAA-4, numAA-3, numAA-2, numAA-1])
SetEnds3 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, numAA-10, numAA-9, numAA-8, numAA-7, numAA-6, numAA-5, numAA-4, numAA-3, numAA-2, numAA-1])
Moviness[SetEnds] = mean

# For 6el6
#SetToMean2 = np.array([244, 245, 246, 247, 248, 249])
#Moviness[SetToMean2] = mean

# For 1t3r
#SetToMean3 = np.array([96, 97, 98, 99, 100, 101])
#Moviness[SetToMean3] = mean

# For 3hpq
#SetToMean4 = np.array([211, 212, 213, 214, 215, 216])
#Moviness[SetToMean4] = mean

# For 1dba
#SetToMean5 = np.array([213, 214, 215, 216, 217, 218, 219])
#Moviness[SetToMean5] = mean

# Lower-bound correction
SmallestMoviness = 99999
for x in range(0, numAA):
    if SmallestMoviness > Moviness[x]:
        SmallestMoviness = Moviness[x]
for y in range(0, numAA):
    Moviness[y] = Moviness[y] - SmallestMoviness

# Normierung mit Max = 1
maxValue = 0
for x in Moviness:
    if x > maxValue:
        maxValue = x
for y in range(0, numAA):
    Moviness[y] = Moviness[y] / maxValue

# Calculate pearson correlation
#from scipy.stats.stats import pearsonr
#print(pearsonr(BindingSite, Moviness))
#print(pearsonr(rmsfArray, Moviness))

from sklearn.metrics import roc_auc_score
print(roc_auc_score(BindingSite, Moviness))

mobility = Moviness
