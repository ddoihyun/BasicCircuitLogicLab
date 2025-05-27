'''
Lab11_Superposition
Vmtr1: VA node(=Vref1)
Vmtr2: VB mode
Vmtr3: VC mode (=Vref2)
'''

from power import Power
import time
#import matplotlib.pyplot as plt
import numpy as np

pwr=Power()

pwr.get_device_info()
pwr.print_device_info()

pwr.open_device()
pwr.reset_analogIO()
print('==========================================\n')

# Resistor value
R1 = float(input('R1의 측정값을 입력하세요 (KOhm) : '))
R2 = float(input('R2의 측정값을 입력하세요 (KOhm) : '))
R3 = float(input('R3의 측정값을 입력하세요 (KOhm) : '))
print('==========================================\n')


# Configure Vref1 and Vref2 sources
pwr.enable_channel('Vref1')
pwr.enable_channel('Vref2')
pwr.analogIO_ON()

# Vraible declaration
counts=np.arange(0,10,1)
V_A_list = []
V_B_list = []
V_C_list = []


########## Experiment (a)#####
print('*** Experiment (a) ***')
print('Vref1  = % .2f (V)'%(5))
print('Vref2  = % .2f (V)'%(0))

pwr.set_channel_voltage('Vref1',5)
pwr.set_channel_voltage('Vref2',0)
time.sleep(1)

for i in counts:
    pwr.measure_vmtr()
    time.sleep(0.5)
    V_A_list.append(pwr.get_vmtr(0))
    V_B_list.append(pwr.get_vmtr(1))
    V_C_list.append(pwr.get_vmtr(2))

# Calculation
V_A_avg_a =np.average(V_A_list)
V_B_avg_a =np.average(V_B_list)
V_C_avg_a =np.average(V_C_list)
I_R1_a = (V_A_avg_a - V_B_avg_a) / (R1*1e3)
I_R2_a = (V_B_avg_a - V_C_avg_a) / (R2*1e3)
I_R3_a = (V_B_avg_a ) / (R3*1e3)


print('V_A =% .2f (V)'%(V_A_avg_a))
print('V_B =% .2f (V)'%(V_B_avg_a))
print('V_C =% .2f (V)'%(V_C_avg_a))
print('I_R1 =% .2f (mA)'%(I_R1_a*1e3))
print('I_R2 =% .2f (mA)'%(I_R2_a*1e3))
print('I_R3 =% .2f (mA)'%(I_R3_a*1e3))

V_A_list.clear()
V_B_list.clear()
V_C_list.clear()


print('\n')
########## Experiment (b)#####
print('*** Experiment (b) ***')
print('Vref1  = % .2f (V)'%(0))
print('Vref2  = % .2f (V)'%(10))

pwr.set_channel_voltage('Vref1',0)
pwr.set_channel_voltage('Vref2',10)
time.sleep(1)

for i in counts:
    pwr.measure_vmtr()
    time.sleep(0.5)
    V_A_list.append(pwr.get_vmtr(0))
    V_B_list.append(pwr.get_vmtr(1))
    V_C_list.append(pwr.get_vmtr(2))

# Calculation
V_A_avg_b =np.average(V_A_list)
V_B_avg_b =np.average(V_B_list)
V_C_avg_b =np.average(V_C_list)
I_R1_b = (V_A_avg_b - V_B_avg_b) / (R1*1e3)
I_R2_b = (V_B_avg_b - V_C_avg_b) / (R2*1e3)
I_R3_b = (V_B_avg_b ) / (R3*1e3)

print('V_A =% .2f (V)'%(V_A_avg_b))
print('V_B =% .2f (V)'%(V_B_avg_b))
print('V_C =% .2f (V)'%(V_C_avg_b))
print('I_R1 =% .2f (mA)'%(I_R1_b*1e3))
print('I_R2 =% .2f (mA)'%(I_R2_b*1e3))
print('I_R3 =% .2f (mA)'%(I_R3_b*1e3))

V_A_list.clear()
V_B_list.clear()
V_C_list.clear()


print('\n')
########## Experiment (c)#####
print('*** Experiment (c) ***')
print('*** Calculation from (a) + (b) ***')
# Calculation
V_A_avg_c = V_A_avg_a + V_A_avg_b
V_B_avg_c = V_B_avg_a + V_B_avg_b
V_C_avg_c = V_C_avg_a + V_C_avg_b
I_R1_c = I_R1_a + I_R1_b
I_R2_c = I_R2_a + I_R2_b
I_R3_c = I_R3_a + I_R3_b

print('V_A =% .2f (V)'%(V_A_avg_c))
print('V_B =% .2f (V)'%(V_B_avg_c))
print('V_C =% .2f (V)'%(V_C_avg_c))
print('I_R1 =% .2f (mA)'%(I_R1_c*1e3))
print('I_R2 =% .2f (mA)'%(I_R2_c*1e3))
print('I_R3 =% .2f (mA)'%(I_R3_c*1e3))



print('\n')
########## Experiment (d)#####
print('*** Experiment (d) ***')
print('Vref1  = % .2f (V)'%(5))
print('Vref2  = % .2f (V)'%(10))

# Need to complete the code for experiment (d)



##############################




pwr.analogIO_OFF()
print('==========================================\n')
print('*** Finished****')
del pwr


