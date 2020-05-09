#Precompute bins for wasserstein and CDF
Bins0 = np.zeros(shape=(numAA,50), dtype=float)
Bins1 = np.zeros(shape=(numAA,50), dtype=float)
Bins2 = np.zeros(shape=(numAA,50), dtype=float)
Bins3 = np.zeros(shape=(numAA,50), dtype=float)
Bins4 = np.zeros(shape=(numAA,50), dtype=float)
Bins5 = np.zeros(shape=(numAA,50), dtype=float)
Bins6 = np.zeros(shape=(numAA,50), dtype=float)
Bins7 = np.zeros(shape=(numAA,50), dtype=float)
Bins8 = np.zeros(shape=(numAA,50), dtype=float)
Bins9 = np.zeros(shape=(numAA,50), dtype=float)
Bins10 = np.zeros(shape=(numAA,50), dtype=float)

distancePerBin = 20/50

for aa in range(0, numAA):
    distances = np.zeros(numAA)
    for aa2 in range(0, numAA):
        distances[aa2] = np.linalg.norm(frameZero[aa] - frameZero[aa2])
    for x in range(0, numAA):
        binIndex = int(distances[x] / distancePerBin)
        if (binIndex < 50):
            Bins0[aa][binIndex] = Bins0[aa][binIndex] + 1
            
for aa in range(0, numAA):
    distances = np.zeros(numAA)
    for aa2 in range(0, numAA):
        distances[aa2] = np.linalg.norm(frame49[aa] - frame49[aa2])
    for x in range(0, numAA):
        binIndex = int(distances[x] / distancePerBin)
        if (binIndex < 50):
            Bins1[aa][binIndex] = Bins1[aa][binIndex] + 1

for aa in range(0, numAA):
    distances = np.zeros(numAA)
    for aa2 in range(0, numAA):
        distances[aa2] = np.linalg.norm(frame99[aa] - frame99[aa2])
    for x in range(0, numAA):
        binIndex = int(distances[x] / distancePerBin)
        if (binIndex < 50):
            Bins2[aa][binIndex] = Bins2[aa][binIndex] + 1

for aa in range(0, numAA):
    distances = np.zeros(numAA)
    for aa2 in range(0, numAA):
        distances[aa2] = np.linalg.norm(frame149[aa] - frame149[aa2])
    for x in range(0, numAA):
        binIndex = int(distances[x] / distancePerBin)
        if (binIndex < 50):
            Bins3[aa][binIndex] = Bins3[aa][binIndex] + 1
            
for aa in range(0, numAA):
    distances = np.zeros(numAA)
    for aa2 in range(0, numAA):
        distances[aa2] = np.linalg.norm(frame199[aa] - frame199[aa2])
    for x in range(0, numAA):
        binIndex = int(distances[x] / distancePerBin)
        if (binIndex < 50):
            Bins4[aa][binIndex] = Bins4[aa][binIndex] + 1
            
for aa in range(0, numAA):
    distances = np.zeros(numAA)
    for aa2 in range(0, numAA):
        distances[aa2] = np.linalg.norm(frame249[aa] - frame249[aa2])
    for x in range(0, numAA):
        binIndex = int(distances[x] / distancePerBin)
        if (binIndex < 50):
            Bins5[aa][binIndex] = Bins5[aa][binIndex] + 1

for aa in range(0, numAA):
    distances = np.zeros(numAA)
    for aa2 in range(0, numAA):
        distances[aa2] = np.linalg.norm(frame299[aa] - frame299[aa2])
    for x in range(0, numAA):
        binIndex = int(distances[x] / distancePerBin)
        if (binIndex < 50):
            Bins6[aa][binIndex] = Bins6[aa][binIndex] + 1

for aa in range(0, numAA):
    distances = np.zeros(numAA)
    for aa2 in range(0, numAA):
        distances[aa2] = np.linalg.norm(frame349[aa] - frame349[aa2])
    for x in range(0, numAA):
        binIndex = int(distances[x] / distancePerBin)
        if (binIndex < 50):
            Bins7[aa][binIndex] = Bins7[aa][binIndex] + 1

for aa in range(0, numAA):
    distances = np.zeros(numAA)
    for aa2 in range(0, numAA):
        distances[aa2] = np.linalg.norm(frame399[aa] - frame399[aa2])
    for x in range(0, numAA):
        binIndex = int(distances[x] / distancePerBin)
        if (binIndex < 50):
            Bins8[aa][binIndex] = Bins8[aa][binIndex] + 1

for aa in range(0, numAA):
    distances = np.zeros(numAA)
    for aa2 in range(0, numAA):
        distances[aa2] = np.linalg.norm(frame449[aa] - frame449[aa2])
    for x in range(0, numAA):
        binIndex = int(distances[x] / distancePerBin)
        if (binIndex < 50):
            Bins9[aa][binIndex] = Bins9[aa][binIndex] + 1

for aa in range(0, numAA):
    distances = np.zeros(numAA)
    for aa2 in range(0, numAA):
        distances[aa2] = np.linalg.norm(frame499[aa] - frame499[aa2])
    for x in range(0, numAA):
        binIndex = int(distances[x] / distancePerBin)
        if (binIndex < 50):
            Bins10[aa][binIndex] = Bins10[aa][binIndex] + 1
