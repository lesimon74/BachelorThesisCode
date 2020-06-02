# Code to calculate score, not to norm.
numAA = len(mobility)
valueToNorm = np.zeros(numAA)
for x in range(0, numAA):
    valueToNorm[x] = mobility[x]

mean = np.mean(valueToNorm)
SetEnds = np.array([0, 1, 2, numAA-3, numAA-2, numAA-1])
valueToNorm[SetEnds] = mean

# For 6el6
#SetToMean2 = np.array([244, 245, 246, 247, 248, 249])
#valueToNorm[SetToMean2] = mean

# For 1t3r
#SetToMean3 = np.array([96, 97, 98, 99, 100, 101])
#valueToNorm[SetToMean3] = mean

mean = np.mean(valueToNorm)
for i in range(0, numAA):
    valueToNorm[i] = valueToNorm[i] - mean
standardDev = np.std(valueToNorm)
for i in range(0, numAA):
    valueToNorm[i] = valueToNorm[i]/standardDev
    
print(np.mean(valueToNorm)) # == 0
print(np.std(valueToNorm)) # == 1

mobileAreas = np.zeros(numAA)
mobileSites1abf = np.array([91, 92, 93, 94, 95, 96, 97, 98, 240, 241, 242, 243, 139, 140, 141, 8, 9, 10, 11, 191, 192, 193])
mobileSites2obi = np.array([121, 122, 123, 124, 125, 3, 4, 129, 130, 104, 105, 106, 107, 149, 151])
mobileSites6el6 = np.array([19, 20, 21, 22, 23, 86, 87, 88, 89, 90, 112, 113, 114, 115, 116, 117, 118, 147, 148, 149, 150, 151, 11, 12, 13])
mobileSites1t3r = np.array([36, 37, 38, 39, 40, 41, 14, 15, 16, 78, 79, 80, 81, 36+99, 37+99, 38+99, 39+99, 40+99, 41+99, 48+99, 49+99, 50+99, 51+99])

# Calculate score here:
print(np.sum(valueToNorm[mobileSites6el6])) #manually set these values

