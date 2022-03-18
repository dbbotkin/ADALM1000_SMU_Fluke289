import time
import os
from io import open
import pysmu
from pysmu import Mode #Session, 
import serial

''' SMU Voltage Range Settings 'from low to hi" USER can set in range from -5V to +5V'''
lowVolt = -5
hiVolt =  5
precision = 1 
''' 1.0, 0.10 or 0.01 the number of decimal placees--will affect number of samples'''

''' Setup serial USB to Fluke 289 DMM'''
DMM = serial.Serial()
DMM.port = '/dev/cu.usbserial-AC00FZQJ'    # Serial port; change to suit your USB

# Serial port setup and open for FLUKE 289 (don't change)
DMM.baudrate = 115200
DMM.bytesize = serial.EIGHTBITS
DMM.parity = serial.PARITY_NONE
DMM.stopbits = serial.STOPBITS_ONE
DMM.xonxoff = False
DMM.rtscts = False
DMM.dsrdtr = False
DMM.timeout = 0.1  # seconds
try:
    DMM.open()
except:
    print("Cannot open serial port...")
    exit()
    
'''Setup output file for data, this will be from your PC path'''
output_filename = 'dmm_out.csv'
output_directory = "/Users/donal/documents/" #''' MacOS; PC users will know what to do'''
os.chdir(output_directory)
file = open(output_filename, 'w', newline='')
file.write('Volt,Amps,V_a,I_a,V_b,I_b \n') #''' for the column headings (can be changed)'''

''' this function will get current reading from DMM set on mAmp or uAmp as needed'''
def QM():
    DMM.write(('qm' + '\r').encode('utf-8'))
    if DMM.read():
        data = (DMM.read(32).decode('utf-8'))        
    return ((data.split(','))[0][1:]) # dont change this
    
 
''' convert volt range for greater precision'''
lowVolt = int((lowVolt)/precision)
hiVolt = int((hiVolt)/precision+1)
session = pysmu.Session(ignore_dataflow=True)
#print (session) debug

smu = session.devices[0]
#smu = list_devices(session,0) more debug
#print (smu.serial)
#print (smu.fwver)

''' Set both channels to SMU mode. (different settings, just FYI'''
chan_a = smu.channels['A']
chan_b = smu.channels['B']
# CHAN_A source
#chan_a.mode = Mode.HI_Z
chan_a.mode = Mode.SVMI
#chan_a.mode = Mode.SVMI_SPLIT
#chan_a.mode = Mode.SIMV
# CHAN_B source
#chan_b.mode = Mode.HI_Z
chan_b.mode = Mode.SVMI
#chan_b.mode = Mode.SIMV
#chan_b.mode = Mode.SIMV_SPLIT

'''this sends settings to ADALM1000'''
def out_file(v_a,v_b):
    #print (volt)
    session.start(0)
    chan_a.constant(v_a)
    chan_b.constant(v_b)
    #if v_b == 5: debug
    time.sleep(2)
    amps = QM()    
    time.sleep(0)
    volt = v_a - v_b
    data = ()
    for x in smu.read(1):    
        out_data = ((x[0][0], x[0][1], x[1][0], x[1][1]))
        data = (str(out_data).replace('(',''))
        time.sleep(.1)
        if len(data) > 0:
            print (str(round(volt,2)) + ', ' + str(amps)+', '+ str(data.replace(')','')))
            file.write(str(round(volt,2)) +', ' + str(amps) +', ' + str(data).replace(')','')+'\n')

# deal with negative voltage
if lowVolt < 0 and hiVolt > 0:
    for vb in range(abs(lowVolt),0,-1):    
        v_a = 0.0
        v_b = float(vb*precision)
        out_file(v_a,v_b)
    for va in range(0,hiVolt):
        v_a = float(va*precision)
        v_b = 0.0
        out_file(v_a,v_b)
else:        
    for va in range(lowVolt,hiVolt): # when both lowVolt and hiVolt > 0
        v_a = float(va*precision)
        v_b = 0.0
        out_file(v_a,v_b)
    
# deal with both lowVolt and hiVolt negative voltage
if lowVolt < 0 and hiVolt < 0:
    for vb in range((lowVolt),abs(hiVolt),-1):    
        v_a = 0.0
        v_b = float(vb*precision)
        out_file(v_a,v_b)
        
    for va in range((hiVolt),(lowVolt)):
        v_a = float(va*precision)
        v_b = 0.0
        out_file(v_a,v_b)    

'''DONE, tidy up'''  
file.close()
chan_a.mode = Mode.HI_Z
chan_b.mode = Mode.HI_Z
chan_a.constant(0)
chan_b.constant(0)
#print (All finished")
