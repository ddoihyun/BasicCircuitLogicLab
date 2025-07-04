'''
eebobard V 0.1
Coded By Youngsik Kim @ CSEE . HGU

Test the Power supply and Voltage meter function

 Set Vref1 : 4.0V
     Vref2 : -3.0V
     VP+ : 5.0V / 50mA
     Vcc : 3.3V


    Vmtr1, Vmtr2, Vmtr3, Vmtr4 : measure and print the voltage
    You can check it by connecting Vmtr1 --> Vre1, Vmtr2--> Vref2, Vmtr3 -> VP+, Vmtr4 -> Vcc
'''

from power import Power

import time

pwr=Power()

pwr.get_device_info()
pwr.print_device_info()

pwr.open_device()
pwr.reset_analogIO()
print('==========================================\n')


#get the number of channels for AnalogIO
pwr.get_number_of_channels()
# get the number of node for channel 1
pwr.get_nodes_of_channels(1)
# figure out channel 1, and node 2
pwr.what_is_channel_node(1,2)
print('==========================================\n')


# Configure VP+=5.0V with 50mA current
pwr.set_channel_voltage('Vref1',4.0)
pwr.set_channel_voltage('Vref2',-3.0)
pwr.set_channel_voltage('VP+',5.0)
pwr.set_channel_current('VP+',50e-3)
pwr.set_channel_voltage('Vcc',3.3)

pwr.enable_channel('Vref1')
pwr.enable_channel('Vref2')
pwr.enable_channel('VP+')
pwr.enable_channel('Vcc')

pwr.analogIO_ON()

time.sleep(1)

pwr.measure_vmtr()

pwr.analogIO_OFF()


print('Vmtr1=%.2f V\n'%(pwr.get_vmtr(0)))
print('Vmtr2=%.2f V\n'%(pwr.get_vmtr(1)))
print('Vmtr3=%.2f V\n'%(pwr.get_vmtr(2)))
print('Vmtr4=%.2f V'%(pwr.get_vmtr(3)))

del pwr













