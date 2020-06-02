# For 2obi
numAA = 165
plt.figure()
#SetToZero = np.array([0, 1, 2, numAA-3, numAA-2, numAA-1])
#mobility[SetToZero] = 0
plt.xlabel('AA No. from 0 to 164', fontsize=18)
plt.ylabel('Mobility [arb. unit]', fontsize=18)
plt.plot(mobility)
plt.plot(mobility2)
plt.legend(['old fit', 'new fit'], loc='upper left')
#plt.legend(['wasserstein distance', 'standard deviation of wasserstein distance'], loc='upper left')
max = 1
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

mingreen = 0
maxgreen = max/2
# aas which move a lot:
plt.vlines(121, mingreen, maxgreen, color="g")
plt.vlines(122, mingreen, maxgreen, color="g")
plt.vlines(123, mingreen, maxgreen, color="g")
plt.vlines(124, mingreen, maxgreen, color="g")
plt.vlines(125, mingreen, maxgreen, color="g")
plt.vlines(3, mingreen, maxgreen, color="g")
plt.vlines(4, mingreen, maxgreen, color="g")
plt.vlines(129, mingreen, maxgreen, color="g")
plt.vlines(130, mingreen, maxgreen, color="g")
plt.vlines(104, mingreen, maxgreen, color="g")
plt.vlines(105, mingreen, maxgreen, color="g")
plt.vlines(106, mingreen, maxgreen, color="g")
plt.vlines(107, mingreen, maxgreen, color="g")
plt.vlines(149, mingreen, maxgreen, color="g")
plt.vlines(150, mingreen, maxgreen, color="g")
plt.vlines(151, mingreen, maxgreen, color="g")

plt.savefig('2obiFitVer4.png', dpi = 400, bbox_inches='tight')
plt.close()
