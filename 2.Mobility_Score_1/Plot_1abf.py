# For 1abf
plt.figure()
SetToZero = np.array([0, 1, 2, numAA-3, numAA-2, numAA-1])
mobility[SetToZero] = 0
plt.xlabel('AA No. from 0 to 304')
plt.ylabel('Mobility')
plt.plot(mobility)
min = 0
max = 5
plt.vlines(8, min, max)
plt.vlines(12, min, max)
plt.vlines(14, min, max)
plt.vlines(88, min, max)
plt.vlines(106, min, max)
plt.vlines(145, min, max)
plt.vlines(149, min, max)
plt.vlines(202, min, max)
plt.vlines(203, min, max)
plt.vlines(230, min, max)

plt.savefig('1abfReport1.png', dpi = 400, bbox_inches='tight')
plt.close()
