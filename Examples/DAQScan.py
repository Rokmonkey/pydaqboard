import daqX

dev = daqX.daqDevice('DaqBoard2K0')
channels = [0]
gains = ['DgainX1']
flags = ['DafBipolar']
scans = 10

print 'Attempting to set acquistion mode....'
acqmode = 'DaamNShot'
dev.AdcSetAcq(acqmode, postTrigCount = scans)

print('Attempting Scan...')

dev.AdcSetScan(channels, gains, flags)

print('Scan Set')

mode = 'DarmPeriod'
state = 'DaasPostTrig'
freq = 1000000.0 #Sample every 1,000,000 nanoseconds

print('Attempting to set rate...')

dev.AdcSetRate(mode, state, freq)

print 'Attempting to Set Transfer Buffer...'

transMask = ['DatmUpdateSingle','DatmCycleOn']

buf = dev.AdcTransferSetBuffer(transMask, scans)

print 'Buffer Set, Setting Trigger Events...'

dev.SetTriggerEvent('DatsImmediate',None, 0, gains, flags, 'DaqTypeAnalogLocal', 0, 0, 'DaqStartEvent')

print 'Start set, Stop Trigger...'

dev.SetTriggerEvent('DatsScanCount',None, 0, gains, flags, 'DaqTypeAnalogLocal', 0, 0, 'DaqStopEvent')

print 'Trigger set'

dev.AdcTransferStart()

print 'Transfer Started, arming...'

dev.AdcArm()

print 'Scanning...'

#dev.WaitForEvent() #Wait until complete or 5 second timeout

while True:
    stat = dev.AdcTransferGetStat()
    #print(stat['retCount'])
    active = stat['active']
    if not (active & 0x01):
        break

dev.AdcDisarm()
print 'Scan complete'
dev.AdcTransferStop()

print 'Transfer Stopped'

for i in buf:
    print dev.ADConvert(i)

dev.Close()




