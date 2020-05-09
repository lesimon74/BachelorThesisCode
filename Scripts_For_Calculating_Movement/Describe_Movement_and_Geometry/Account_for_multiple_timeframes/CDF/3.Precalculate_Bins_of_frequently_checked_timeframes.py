# Calculate the CDF version of Bins0, Bins1, ..., Bins10
Bins0CDF = np.zeros(shape=(numAA,50), dtype=float)
Bins1CDF = np.zeros(shape=(numAA,50), dtype=float)
Bins2CDF = np.zeros(shape=(numAA,50), dtype=float)
Bins3CDF = np.zeros(shape=(numAA,50), dtype=float)
Bins4CDF = np.zeros(shape=(numAA,50), dtype=float)
Bins5CDF = np.zeros(shape=(numAA,50), dtype=float)
Bins6CDF = np.zeros(shape=(numAA,50), dtype=float)
Bins7CDF = np.zeros(shape=(numAA,50), dtype=float)
Bins8CDF = np.zeros(shape=(numAA,50), dtype=float)
Bins9CDF = np.zeros(shape=(numAA,50), dtype=float)
Bins10CDF = np.zeros(shape=(numAA,50), dtype=float)

for aa in range(0, numAA):
    Bins0CDF[aa][0] = Bins0[aa][0]
    for bIndex in range(1, 50):
        Bins0CDF[aa][bIndex] = Bins0CDF[aa][bIndex-1] + Bins0[aa][bIndex]
        
for aa in range(0, numAA):
    Bins1CDF[aa][0] = Bins1[aa][0]
    for bIndex in range(1, 50):
        Bins1CDF[aa][bIndex] = Bins1CDF[aa][bIndex-1] + Bins1[aa][bIndex]

for aa in range(0, numAA):
    Bins2CDF[aa][0] = Bins2[aa][0]
    for bIndex in range(1, 50):
        Bins2CDF[aa][bIndex] = Bins2CDF[aa][bIndex-1] + Bins2[aa][bIndex]
        
for aa in range(0, numAA):
    Bins3CDF[aa][0] = Bins3[aa][0]
    for bIndex in range(1, 50):
        Bins3CDF[aa][bIndex] = Bins3CDF[aa][bIndex-1] + Bins3[aa][bIndex]
        
for aa in range(0, numAA):
    Bins4CDF[aa][0] = Bins4[aa][0]
    for bIndex in range(1, 50):
        Bins4CDF[aa][bIndex] = Bins4CDF[aa][bIndex-1] + Bins4[aa][bIndex]

for aa in range(0, numAA):
    Bins5CDF[aa][0] = Bins5[aa][0]
    for bIndex in range(1, 50):
        Bins5CDF[aa][bIndex] = Bins5CDF[aa][bIndex-1] + Bins5[aa][bIndex]
        
for aa in range(0, numAA):
    Bins6CDF[aa][0] = Bins6[aa][0]
    for bIndex in range(1, 50):
        Bins6CDF[aa][bIndex] = Bins6CDF[aa][bIndex-1] + Bins6[aa][bIndex]
        
for aa in range(0, numAA):
    Bins7CDF[aa][0] = Bins7[aa][0]
    for bIndex in range(1, 50):
        Bins7CDF[aa][bIndex] = Bins7CDF[aa][bIndex-1] + Bins7[aa][bIndex]

for aa in range(0, numAA):
    Bins8CDF[aa][0] = Bins8[aa][0]
    for bIndex in range(1, 50):
        Bins8CDF[aa][bIndex] = Bins8CDF[aa][bIndex-1] + Bins8[aa][bIndex]
        
for aa in range(0, numAA):
    Bins9CDF[aa][0] = Bins9[aa][0]
    for bIndex in range(1, 50):
        Bins9CDF[aa][bIndex] = Bins9CDF[aa][bIndex-1] + Bins9[aa][bIndex]

for aa in range(0, numAA):
    Bins10CDF[aa][0] = Bins10[aa][0]
    for bIndex in range(1, 50):
        Bins10CDF[aa][bIndex] = Bins10CDF[aa][bIndex-1] + Bins10[aa][bIndex]
