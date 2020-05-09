plt.figure()

plt.xlabel('AA No. from 10 to 305')
plt.ylabel('difference to initial stucture')
plt.plot(Moviness)
plt.plot(MovinessStd)
plt.legend(['mean deviation from initial structure', 'standard deviation of deviation from initial structure'], loc='upper left')

plt.savefig('Normal1abfNew.png', dpi = 400, bbox_inches='tight')
