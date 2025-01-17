# For 6el6
numAA = 260
plt.figure()
SetToZero = np.array([0, 1, 2, 244, 245, 246, 247, 248, 249, numAA-3, numAA-2, numAA-1])
mobility[SetToZero] = 0
mobility2[SetToZero] = 0
plt.xlabel('AA No. from 0 to 259', fontsize=18)
plt.ylabel('Mobility [arb. unit]', fontsize=18)
plt.plot(mobility)
plt.plot(mobility2)
#plt.legend(['wasserstein distance', 'standard deviation of wasserstein distance'], loc='upper left')
#plt.legend(['old fit', 'new fit'], loc='upper left')
plt.legend(['Apoprotein','Holoprotein'], loc='upper left')
min = 0
max = 4.2
plt.vlines(11, min, max)
plt.vlines(33, min, max)
plt.vlines(34, min, max)
plt.vlines(36, min, max)
plt.vlines(37, min, max)
plt.vlines(40, min, max)
plt.vlines(44, min, max)
plt.vlines(47, min, max)
plt.vlines(71, min, max)
plt.vlines(73, min, max)
plt.vlines(74, min, max)
plt.vlines(77, min, max)
plt.vlines(78, min, max)
plt.vlines(81, min, max)
plt.vlines(93, min, max)
plt.vlines(112, min, max)
plt.vlines(116, min, max)
plt.vlines(137, min, max)
plt.vlines(205, min, max)
plt.vlines(206, min, max)
plt.vlines(209, min, max)

mingreen = 0
maxgreen = max/2
# aas which move a lot:
#plt.vlines(19, mingreen, maxgreen, color="g")
#plt.vlines(20, mingreen, maxgreen, color="g")
#plt.vlines(21, mingreen, maxgreen, color="g")
#plt.vlines(22, mingreen, maxgreen, color="g")
#plt.vlines(23, mingreen, maxgreen, color="g")
#plt.vlines(86, mingreen, maxgreen, color="g")
#plt.vlines(87, mingreen, maxgreen, color="g")
#plt.vlines(88, mingreen, maxgreen, color="g")
#plt.vlines(89, mingreen, maxgreen, color="g")
#plt.vlines(90, mingreen, maxgreen, color="g")
#plt.vlines(112, mingreen, maxgreen, color="g")
#plt.vlines(113, mingreen, maxgreen, color="g")
#plt.vlines(114, mingreen, maxgreen, color="g")
#plt.vlines(115, mingreen, maxgreen, color="g")
#plt.vlines(116, mingreen, maxgreen, color="g")
#plt.vlines(117, mingreen, maxgreen, color="g")
#plt.vlines(118, mingreen, maxgreen, color="g")
#plt.vlines(147, mingreen, maxgreen, color="g")
#plt.vlines(148, mingreen, maxgreen, color="g")
#plt.vlines(149, mingreen, maxgreen, color="g")
#plt.vlines(150, mingreen, maxgreen, color="g")
#plt.vlines(151, mingreen, maxgreen, color="g")
#plt.vlines(11, mingreen, maxgreen, color="g")
#plt.vlines(12, mingreen, maxgreen, color="g")
#plt.vlines(13, mingreen, maxgreen, color="g")

plt.savefig('6el6ApoHoloWassersteinMultiFrameStdVer3.png', dpi = 400, bbox_inches='tight')
plt.close()
