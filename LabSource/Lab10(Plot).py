#import matplotlib.pyplot as plt

#Rval = [0.5, 1.0, 2.0, 3.01, 4.09, 5.04, 7.55, 10.0]
#VR1 = [7.69, 6.59, 5.15, 4.24, 3.58, 3.12, 2.38, 1.93]
#VR2 = [1.42, 2.47, 3.89, 4.80, 5.45, 5.89, 6.66, 7.06]

#plt.plot(Rval, VR1, label='VR1')
#plt.plot(Rval, VR2, label='VR2')
#plt.xlabel('Rval(R2)')
#plt.ylabel('Voltage(V)')
#plt.title('VR1 and VR2')
#plt.legend()
#plt.grid(True)
#plt.show()




import matplotlib.pyplot as plt

Rval = [0.5, 1.0, 2.0, 3.01, 4.09, 5.04, 7.55, 10.00]
P1 = [21.76, 16.40, 10.00, 6.78, 4.83, 3.68, 2.14, 1.40]
P2 = [4.05, 6.09, 7.59, 7.66, 7.26, 6.89, 5.92, 4.99]

plt.plot(Rval, P1, label='P1')
plt.plot(Rval, P2, label='P2')

plt.xlabel('Rval(R2)')
plt.ylabel('P(mW)')

plt.title('P1 and P2')
plt.legend()
plt.grid(True)
plt.show()





