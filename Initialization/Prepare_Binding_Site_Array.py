bindingSites6el6 = np.array([11, 33, 34, 36, 37, 40, 44, 47, 71, 73, 74, 77, 78, 81, 93, 112, 116, 137, 205, 206, 209])
bindingSites2obi = np.array([40, 75, 130, 17, 94, 96, 71, 104, 105, 125, 127, 129])
bindingSites1abf = np.array([8, 12, 14, 88, 106, 145, 149, 202, 203, 230])
bindingSites1t3rcorrect = np.array([24, 26, 27, 28, 29, 31, 47, 48, 49, 81, 83, 123, 125, 126, 127, 128, 130, 146, 147, 148, 180, 182])
BindingSite = np.zeros(numAA)
BindingSite[bindingSites6el6] = 1
print(BindingSite)
