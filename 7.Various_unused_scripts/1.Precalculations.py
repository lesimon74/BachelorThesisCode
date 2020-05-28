# Header for code below, which doesn't have to be executed every time
from datetime import datetime
ca = universe.select_atoms('name CA')
Moviness = wasserstein6el6Moviness
#Make sure Moviness is obtained from the Wasserstein distance
limit = np.mean(Moviness) + 0.15
print(limit)
# Get Box coordinates:
TopX = 0
BottomX = 200
TopY = 0
BottomY = 200
TopZ = 0
BottomZ  = 200
counter = 0
for calpha in ca.positions:
    if Moviness[counter] > limit:
        if calpha[0] > TopX:
            TopX = calpha[0]
        if calpha[0] < BottomX:
            BottomX = calpha[0]
        if calpha[1] > TopY:
            TopY = calpha[1]
        if calpha[1] < BottomY:
            BottomY = calpha[1]
        if calpha[2] > TopZ:
            TopZ = calpha[2]
        if calpha[2] < BottomZ:
            BottomZ = calpha[2]
    counter = counter + 1
print(TopX)
print(BottomX)
print(TopY)
print(BottomY)
print(TopZ)
print(BottomZ)

PreSortedX = np.ndarray(shape=(numAA,5), dtype=float)
Index = 0
for pos in ca.positions:
    PreSortedX[Index][0] = pos[0]
    PreSortedX[Index][1] = pos[1] - 2.0
    PreSortedX[Index][2] = pos[1] + 2.0
    PreSortedX[Index][3] = pos[2] - 2.0
    PreSortedX[Index][4] = pos[2] + 2.0
    Index = Index + 1
PreSortedX = PreSortedX[PreSortedX[:,0].argsort()]

PreSortedY = np.ndarray(shape=(numAA,5), dtype=float)
Index = 0
for pos in ca.positions:
    PreSortedY[Index][0] = pos[1]
    PreSortedY[Index][1] = pos[0] - 2.0
    PreSortedY[Index][2] = pos[0] + 2.0
    PreSortedY[Index][3] = pos[2] - 2.0
    PreSortedY[Index][4] = pos[2] + 2.0
    Index = Index + 1
PreSortedY = PreSortedY[PreSortedY[:,0].argsort()]

PreSortedZ = np.ndarray(shape=(numAA,5), dtype=float)
Index = 0
for pos in ca.positions:
    PreSortedZ[Index][0] = pos[2]
    PreSortedZ[Index][1] = pos[0] - 2.0
    PreSortedZ[Index][2] = pos[0] + 2.0
    PreSortedZ[Index][3] = pos[1] - 2.0
    PreSortedZ[Index][4] = pos[1] + 2.0
    Index = Index + 1
PreSortedZ = PreSortedZ[PreSortedZ[:,0].argsort()]
print(PreSortedY)
print(PreSortedZ)
