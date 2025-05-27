'''
Lab10_Maximum Power transfer
Vmtr1: VA node(=VP+)
Vmtr2: VB mode
'''

from power import Power
import time
import matplotlib.pyplot as plt
import numpy as np

pwr=Power()

pwr.get_device_info()
pwr.print_device_info()

pwr.open_device()
pwr.reset_analogIO()
print('==========================================\n')


# Resistor value
R1 = float(input('R1의 측정값을 입력하세요 (KOhm): '))
Rval = float(input('Rval의 측정값을 입력하세요 (KOhm) : '))
print('==========================================\n')


# Configure VP+ with 50mA current limit
pwr.set_channel_current('VP+',50e-3)
pwr.enable_channel('VP+')
pwr.analogIO_ON()


# Vraible declaration
counts=np.arange(0,10,1)
Vdc = 9
V_A_list = []
V_B_list = []


# Experiment
print('*** Experiment****')
print('Vdc  = % .2f (V)'%(Vdc))
print('R1   = % .2f (KOhm)'%(R1))
print('Rval = % .2f (KOhm)'%(Rval))

for i in counts:
    pwr.set_channel_voltage('VP+',Vdc)
    time.sleep(0.5)
    pwr.measure_vmtr()

    V_A_list.append(pwr.get_vmtr(0))
    V_B_list.append(pwr.get_vmtr(1))


pwr.analogIO_OFF()
print('==========================================\n')
print('*** Finished****')
del pwr


# Calculation
V_A_avg =np.average(V_A_list)
V_B_avg =np.average(V_B_list)
V_R1 = V_A_avg - V_B_avg
V_R2 = V_B_avg
P_R1 = V_R1**2 / (R1*1e3)
P_R2 = V_R2**2 / (Rval*1e3)

print('V_R1 =% .2f (V)'%(V_R1))
print('V_R2 =% .2f (V)'%(V_R2))
print('P_R1 =% .2f (mW)'%(P_R1*1e3))
print('P_R2 =% .2f (mW)'%(P_R2*1e3))



