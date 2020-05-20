# For 2obi
plt.figure()
SetToZero = np.array([0, 1, 2, numAA-3, numAA-2, numAA-1])
mobility[SetToZero] = 0
plt.xlabel('AA No. from 0 to 164')
plt.ylabel('Mobility')
plt.plot(mobility)
max = 5
min = 0
#catalytic triad
plt.vlines(46-5-1, min, max)
plt.vlines(81-5-1, min, max)
plt.vlines(136-5-1, min, max)
#allosteric site
plt.vlines(23-5-1, min, max)
plt.vlines(100-5-1, min, max)
plt.vlines(102-5-1, min, max)
# not 100% certain but binding sites with a high probability
plt.vlines(71, min, max)
plt.vlines(110-5-1, min, max)
plt.vlines(111-5-1, min, max)
plt.vlines(131-5-1, min, max)
plt.vlines(133-5-1, min, max)
plt.vlines(135-5-1, min, max)

plt.savefig('2obiReport1.png', dpi = 400, bbox_inches='tight')
