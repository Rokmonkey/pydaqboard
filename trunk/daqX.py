import ctypes as ct
from ctypes import wintypes as wt
from daqxh import *

#initialize Daqx.dll
daq = ct.windll.daqx

class deviceProps(ct.Structure):
    _fields_ = [("deviceType", wt.DWORD),
                ("basePortAddress", wt.DWORD),
                ("dmaChannel", wt.DWORD),
                ("socket", wt.DWORD),
                ("interruptLevel", wt.DWORD),
                ("protocol", wt.DWORD),
                ("alias", ct.c_char*64),
                ("maxAdChannels", wt.DWORD),
                ("maxDaChannels", wt.DWORD),
                ("maxDigInputBits", wt.DWORD),
                ("maxDigOutputBits", wt.DWORD),
                ("maxCtrChannels", wt.DWORD),
                ("mainUnitAdChannels", wt.DWORD),
                ("mainUnitDaChannels", wt.DWORD),
                ("mainUnitDigInputBits", wt.DWORD),
                ("mainUnitDigOutputBits", wt.DWORD),
                ("mainUnitCtrChannels", wt.DWORD),
                ("adFifoSize", wt.DWORD),
                ("daFifoSize", wt.DWORD),
                ("adResolution", wt.DWORD),
                ("daResolution", wt.DWORD),
                ("adMinFreq", ct.c_float),
                ("adMaxFreq", ct.c_float),
                ("daMinFreq", ct.c_float),
                ("daMaxFreq", ct.c_float)]

class daqDeviceListT(ct.Structure):
    _fields_ = [("devicename", ct.c_char * 64)]

#Device Initialization Functions

def GetDeviceCount():
    """Returns the number of currently configured devices"""

    deviceCount = ct.c_int(0)
    deviceCountpnt = ct.pointer(deviceCount)
    daq.daqGetDeviceCount(deviceCountpnt)
    
    return deviceCount.value

def GetDeviceList():
    """Returns a list of currently configured device names"""

    devices = []
    count = GetDeviceCount()
    countpnt = ct.pointer(ct.c_int(count))
    devlist = (daqDeviceListT*count)()
    
    daq.daqGetDeviceList(devlist, countpnt)
    
    for i in devlist:
        devices.append(i.devicename)
        
    return devices

def GetDriverVersion():
    """Retrieves the revision level of the driver currently in use"""

    version = wt.DWORD(1)
    pversion = ct.pointer(version)
    daq.daqGetDriverVersion(pversion)

    return version.value

###Handle Class definition

class daqDevice():

    def __init__(self, deviceName):

        self.deviceName = deviceName   
        pdeviceName = ct.c_char_p(deviceName)
        self.handle = daq.daqOpen(pdeviceName)
        self.props = self.GetDeviceProperties()

    def Online(self):
        """Determines if a device is online"""

        online = ct.c_bool(False)
        onlinepnt = ct.pointer(online)
        daq.daqOnline(self.handle, onlinepnt)

        return online.value

    def Close(self):
        """Used to close a device"""

        daq.daqClose(self.handle)

    def GetDeviceProperties(self):
        """Returns the properties for a specified device"""

        properties = {}
    
        deviceNamepnt = ct.c_char_p(self.deviceName)
        devProps = deviceProps()
        devicePropspnt = ct.pointer(devProps)
        daq.daqGetDeviceProperties(deviceNamepnt,devicePropspnt)
        
        for i in dir(devProps):
            if not i.startswith('_'):
                val = getattr(devProps, i)
                if i == 'deviceType':
                    val = DaqHardwareVersion.ofValues(int(val))
                if i == 'protocol':
                    val = DaqProtocol.ofValues(int(val))
                properties[i]=val
            
        return properties

    def ADConvert(self, request):
        """Converts returned 16bit integer to a voltage of a Dbk2000 Bipolar no gain"""
        cal = 20.0/(2**16)
        val = request*cal - 10.0
        return val
        
    #Event Handling Functions

    def SetTimeout(self, mSecTimeout):
        """Sets the time-out for waiting on either a single event or
            multiple events"""

        mSecTimeout = wt.DWORD(mSecTimeout)
        daq.daqSetTimeout(self.handle, mSecTimeout)

    def WaitForEvent(self, event):
        """Waits on a specific event to occur on the specified event"""

        event = DaqWaitMode.ofKeys(event)
        
        daq.daqWaitForEvent(self.handle, event)

    #ADC Acquisition Functions

    def AdcSetAcq(self, mode, preTrigCount = 0, postTrigCount = 0):
        """Configures the acquisition mode and the pre- and post-trigger scan durations"""

        mode = DaqAdcAcqMode.ofKeys(mode)
        preTrigCount = wt.DWORD(preTrigCount)
        postTrigCount = wt.DWORD(postTrigCount)
        
        daq.daqAdcSetAcq(self.handle, mode, preTrigCount, postTrigCount)

    #ADC Rate Functions

    def AdcSetRate(self, mode, state, reqValue):
        """Configures the acquisition scan rate"""

        mode = DaqAdcRateMode.ofKeys(mode)
        state = DaqAdcAcqState.ofKeys(state)
        reqValue = ct.c_float(reqValue)
        actValue = ct.c_float(0.0)
        pactValue = ct.pointer(actValue)

        daq.daqAdcSetRate(self.handle, mode, state, reqValue, pactValue)

        return actValue.value

    #Utility Functions    
    
    def GetInfo(self, chan, whichInfo):
        """Retrieves hardware information for the specified device"""

        chan = ct.c_int(chan)
        info = ct.c_int(0)
        pinfo = ct.pointer(info)
        whichInfo = daqInfo.ofKeys(whichInfo)
        daq.daqGetInfo(self.handle, chan, whichInfo, pinfo)

        return info.value

    #Custom ADC Aquisition Functions

    def AdcSetScan(self, channels, gains, flags):
        """Configures an aquisition scan group consisting of multiple channels"""

        chanCount = len(channels)
        gains = DaqAdcGain.ofKeys(gains)
        flags = orFlags(DaqAdcFlag.ofKeys(flags))
        
        chan_array = (wt.DWORD * chanCount)()
        gain_array = (wt.DWORD * chanCount)()
        flag_array = (wt.DWORD * chanCount)()

        for i in range(chanCount):
            chan_array[i] = channels[i]
        for i in range(chanCount):
            gain_array[i] = gains[i]
        for i in range(chanCount):
            flag_array[i] = flags[i]

        pchan_array = ct.pointer(chan_array)
        pgain_array = ct.pointer(gain_array)
        pflag_array = ct.pointer(flag_array)
        
        daq.daqAdcSetScan(self.handle, pchan_array, pgain_array, pflag_array,
                          wt.DWORD(chanCount))

    def AdcGetScan(self):
        """Reads the current scan group, which consists of all configured\
            channels"""
        channels=gains=flags = []
        chan_array = (wt.DWORD*512)()
        pchan_array = ct.pointer(chan_array)
        gain_array = (wt.DWORD*512)()
        pgain_array = ct.pointer(gain_array)
        flag_array = (wt.DWORD*512)()
        pflag_array = ct.pointer(flag_array)
        
        chanCount = ct.c_int(0)
        pchanCount = ct.pointer(chanCount)

        daq.daqAdcSetScan(self.handle, pchan_array, pgain_array, pflag_array,
                            pchanCount)

        for i in gain_array:
            gains.append(i)
        for i in flag_array:
            flags.append(i)
        for i in chan_array:
            channels.append(i)

        gainVals = DaqAdcGain.ofValues(gains)
        flagVals = DaqAdcFlag.ofValues(flags)

        vals = {'Channels' : channels, 'Gains' : gainVals,
                'Flags' : flagVals, 'Channelcount' : chanCount}
        return vals

    #One-Step ADC functions

    def AdcRd(self, chan, gain, flags):
        """Takes a single reading from the given local A/D channel using a software trigger"""

        flags = orFlags(DaqAdcFlag.ofKeys(flags))
        gain = DaqAdcGain.ofKeys(gain)
        sample = ct.c_long(0)
        psample = ct.pointer(sample)

        daq.daqAdcRd(self.handle, chan, psample, wt.DWORD(gain),
                     flags)

        return sample.value

    #ADC Acquisition Trigger

    def SetTriggerEvent(self, trigSource, trigSensitivity, channel, gainCode,
                        flags, channelType, level, variance, event):
        """Sets an acquisition trigger start event or stop event"""

        trigSource = DaqAdcTriggerSource.ofKeys(trigSource)
        if trigSensitivity != None:
            trigSensitivity = DaqEnhTrigSensT.ofKeys(trigSensitivity)
        gainCode = DaqAdcGain.ofKeys(gainCode)
        flags = orFlags(DaqAdcFlag.ofKeys(flags))
        channelType = DaqChannelType.ofKeys(channelType)
        event = DaqTriggerEvent.ofKeys(event)

        daq.daqSetTriggerEvent(self.handle, trigSource, trigSensitivity,
                               channel, wt.DWORD(gainCode[0]), flags[0], channelType,
                               ct.c_float(level), ct.c_float(variance), event)
    

    #ADC Transfer Buffer

    def AdcTransferSetBuffer(self, transferMask, scanCount):
        """Configure transfer buffer for acquired data"""

        buf = (wt.WORD * scanCount)()
        pbuf = ct.pointer(buf)
        transferMask = orFlags(DaqAdcTransferMask.ofKeys(transferMask))
        scanCount = wt.DWORD(scanCount)
        daq.daqAdcTransferSetBuffer(self.handle, pbuf, scanCount, transferMask)

        return buf

    def AdcTransferStart(self):
        """Initiates an ADC acquisition transfer"""

        daq.daqAdcTransferStart(self.handle)

    def AdcTransferStop(self):
        """Stops a current ADC buffer transfer, if one is active"""

        daq.daqAdcTransferStop(self.handle)

    def AdcTransferGetStat(self):
        """Retrieves the current state of an acquisition transfer"""
        
        active = wt.DWORD(0)
        retCount = wt.DWORD(0)
        pactive = ct.pointer(active)
        pretCount = ct.pointer(retCount)

        daq.daqAdcTransferGetStat(self.handle, pactive, pretCount)

        return {'active':active.value, 'retCount':retCount.value}

    #ADC Acquisition Control

    def AdcArm(self):
        """Arms an ADC acquisition by enabling the currently defined ADC"""

        daq.daqAdcArm(self.handle)

    def AdcDisarm(self):
        """Disarms an ADC acquisition, if one is currently active"""

        daq.daqAdcDisarm(self.handle)

    #One step DAC functions

    def DacWt(self, deviceType, chan, dataVal):
        """Sets the output value of a local or expansion DAC channel"""

        deviceType = DaqDacDeviceType.ofKeys(deviceType)
        if dataVal >= 10.0:
            dataVal = 65535
        if dataVal <= -10.0:
            dataVal = 0
        else:
            dataVal = (dataVal+10.0)/(20.0/65535)

        daq.daqDacWt(self.handle, deviceType, chan, wt.WORD(int(dataVal)))
