# For 1abf
numAA = 305
plt.figure()
#SetToZero = np.array([0, 1, 2, numAA-3, numAA-2, numAA-1])
#mobility[SetToZero] = 0
plt.xlabel('AA No. from 0 to 304', fontsize=18)
plt.ylabel('Mobility [arb. unit]', fontsize=18)
plt.plot(mobility)
#plt.plot(mobility2)
#plt.legend(['old fit', 'new fit'], loc='upper left')
#plt.legend(['wasserstein distance', 'standard deviation of wasserstein distance'], loc='upper left')
min = 0
max = 1
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

mingreen = 0
maxgreen = max/2
# aas which move a lot:
plt.vlines(91, mingreen, maxgreen, color="g")
plt.vlines(92, mingreen, maxgreen, color="g")
plt.vlines(93, mingreen, maxgreen, color="g")
plt.vlines(94, mingreen, maxgreen, color="g")
plt.vlines(95, mingreen, maxgreen, color="g")
plt.vlines(96, mingreen, maxgreen, color="g")
plt.vlines(97, mingreen, maxgreen, color="g")
plt.vlines(98, mingreen, maxgreen, color="g")
plt.vlines(240, mingreen, maxgreen, color="g")
plt.vlines(241, mingreen, maxgreen, color="g")
plt.vlines(242, mingreen, maxgreen, color="g")
plt.vlines(243, mingreen, maxgreen, color="g")
plt.vlines(139, mingreen, maxgreen, color="g")
plt.vlines(140, mingreen, maxgreen, color="g")
plt.vlines(141, mingreen, maxgreen, color="g")
plt.vlines(8, mingreen, maxgreen, color="g")
plt.vlines(9, mingreen, maxgreen, color="g")
plt.vlines(10, mingreen, maxgreen, color="g")
plt.vlines(11, mingreen, maxgreen, color="g")
plt.vlines(191, mingreen, maxgreen, color="g")
plt.vlines(192, mingreen, maxgreen, color="g")
plt.vlines(193, mingreen, maxgreen, color="g")

plt.savefig('1abfNormal4Ver4.png', dpi = 400, bbox_inches='tight')
plt.close()
