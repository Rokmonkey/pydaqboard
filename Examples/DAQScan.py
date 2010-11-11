from daq import daqDevice
from daqh import DgainX4, DafBipolar, DaamNShot, DarmFrequency, DaasPostTrig, \
            DatmUpdateSingle, DatmCycleOff, DatsImmediate, DaqTypeAnalogLocal, \
            DaqStartEvent, DatsScanCount, DaqStopEvent, DaafAcqActive

def volt_to_strain(volts):
    strains = range(len(volts))
    #Lists are Gauge 1, 2, 3, 4, 5
    #Gauges are set up on channels 0, 1, 2, 3, 4
    calibration = [4589, 4529, 4440, 4485, 4454]
    offset = [-4, -3, -4, -5, 0]
    for i in range(len(volts)):
        strains[i] = volts[i]*calibration[i]+offset[i]

    return strains

def strain_to_curvature(strainlist):

    thickness = 1.0/16.0
    curvaturelist = []
    for strain in strainlist:
        strain /= 1000000.0
        curvature = strain/thickness
        curvaturelist.append(curvature)

    return curvaturelist

dev = daqDevice('DaqBoard2K0')
channels = [0]
gains = [DgainX4]
flags = [DafBipolar]
scans = 100

print 'Attempting to set acquistion mode....'
acqmode = DaamNShot
dev.AdcSetAcq(acqmode, postTrigCount = scans)

print('Attempting Scan...')

dev.AdcSetScan(channels, gains, flags)

print('Scan Set')

mode = DarmFrequency
state = DaasPostTrig
freq = 100.0 #1000 Hertz

print('Attempting to set rate...')

dev.AdcSetRate(mode, state, freq)

print 'Attempting to Set Transfer Buffer...'

transMask = DatmUpdateSingle|DatmCycleOff

buf = dev.AdcTransferSetBuffer(transMask, scans, len(channels))

print 'Buffer Set, Setting Trigger Events...'

dev.SetTriggerEvent(DatsImmediate,None, 0, gains[0], flags[0], DaqTypeAnalogLocal, 0, 0, DaqStartEvent)

print 'Start set, Stop Trigger...'

dev.SetTriggerEvent(DatsScanCount,None, 0, gains[0], flags[0], DaqTypeAnalogLocal, 0, 0, DaqStopEvent)

print 'Trigger set'

dev.AdcTransferStart()

print 'Transfer Started, arming...'

dev.AdcArm()

print 'Scanning...'

#dev.WaitForEvent() #Wait until complete or 5 second timeout
retCount = 0
while True:
    stat = dev.AdcTransferGetStat()
    retCount = stat['retCount']
    active = stat['active']
    if not (active & DaafAcqActive):
        break

dev.AdcDisarm()
print 'Scan complete'
dev.AdcTransferStop()

print 'Transfer Stopped'
f = open('Strains2.txt','w+')
vals = []

count = 0
tmp = []
for i in range(retCount):
    for j in range(len(channels)):
        read = buf[(len(channels)*i) + j]
        tmp.append(read)
    volts = map(dev.ADConvert, tmp)
    strain = volt_to_strain(volts)
    curv = strain_to_curvature(strain)
    tmp = ''
    for i in volts:
        tmp+=str(i)+','
    tmp+='\n'
    f.write(tmp)
    tmp = []

f.close()

dev.Close()




