import daqX

dev = daqX.daqDevice('DaqBoard2K0')
chan = 0
gain = 1
flags = ['DafUnipolar','DafUnsigned']

read = dev.AdcRd(chan, gain, flags)
print read, 'Volts'

dev.Close()
