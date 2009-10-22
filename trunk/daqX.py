import ctypes as ct
from ctypes import wintypes as wt
from daqxh import *

#initialize Daqx.dll
daq = ct.windll.daqx

class deviceProps(ct.Structure):
    _fields_ = [("deviceType", wt.DWORD),
                ("basePortAddress", wt.DWORD),
                ("dmaChannel", wt.DWORD),
                ("protocol", wt.DWORD),
                ("alias", ct.c_char_p),
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

    
#Error Handler Functions

def DefaultErrorHandler(handle):
    """Displays an error message and then exits the application program"""
    
    errCode = ct.c_int
    daq.daqDefaultErrorHandler(handle, errCode)

    return errCode.value

def FormatError(errorNum):
    """Returns the text-string equivalent for the
        specified error condition code"""

    msg = ct.c_char_p
    daq.daqFormatError(errorNum, msg)

    return msg.value

def GetLastError(handle, err):
    """Retrieves the last error condition code registered by the driver"""

    errCode = ct.c_int(err)
    daq.daqGetLastError(handle, errCode)

    return errCode.value

def ProcessError(handle, err):
    """Initiates an error for processing by the driver"""

    errCode = ct.c_int(err)
    daq.daqGetLastError(handle, errCode)

def SetDefaultErrorHandler(handler):
    """Sets the driver to use the default error handler specified
        for all devices"""

    handlerpnt = ct.POINTER(handler)
    daq.daqSetDefaultErrorHandler(handlerpnt)

def SetErrorHandler(handle, handler):
    """Specifies the routine to call when an error occurs in any function\
        for the specified device"""

    handlepnt = ct.POINTER(handler)
    daq.daqSetErrorHandler(handle, handlepnt)

def GetDriverVersion():
    """Retrieves the revision level of the driver currently in use"""

    version = wt.DWORD(1)
    pversion = ct.pointer(version)
    daq.daqGetDriverVersion(pversion)

    return version.value

#Group event handling function
    
"""
def daqWaitForEvents(devices, events, eventCount, eventSet, waitMode):
    ""Waits on specific device events to occur on the specified devices""
    arraySize = len(devices)
    handles = []
    for i in range(arraySize):
        handles.append(i.handle)
"""

###Handle Class definition

class daqDevice():

    def __init__(self, deviceName):

        self.deviceName = deviceName   
        pdeviceName = ct.c_char_p(deviceName)
        self.handle = daq.daqOpen(pdeviceName)

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
                    val = ofValues(DaqHardwareVersion,[int(val)])
                if i == 'protocol':
                    val = ofValues(DaqProtocol,[int(val)])
                properties[i]=val

            
        return properties
        
    #Event Handling Functions

    def SetTimeout(self, mSecTimeout):
        """Sets the time-out for waiting on either a single event or
            multiple events"""

        mSecTimeout = ct.c_int(mSecTimeout)
        daq.daqSetTimeout(self.handle, mSecTimeout)

    def WaitForEvent(self, event):
        """Waits on a specific event to occur on the specified event"""

        daq.daqWaitForEvent(self.handle, event)

    #Utility Functions    
    
    def GetInfo(self, chan, whichInfo):
        """Retrieves hardware information for the specified device"""

        chan = ct.c_int(chan)
        info = ct.c_int(0)
        pinfo = ct.pointer(info)
        daq.daqGetInfo(self.handle, chan, whichInfo, pinfo)

        return info.value

    #Custom ADC Aquisition Functions

    def AdcSetScan(self, channels, gains, flags):
        """Configures an aquisition scan group consisting of multiple channels"""

        gains = ofKeys(bipolarGains, gains)
        flags = ofKeys(daqAdcFlag, flags)
        chan_array = ct.ARRAY(wt.DWORD, len(channels))
        pchan_array = ct.pointer(chan_array(*channels))
        gain_array = ct.ARRAY(wt.DWORD, len(gains))
        pgain_array = ct.pointer(gain_array(*gains))
        flag_array = ct.ARRAY(wt.ARRAY, len(flags))
        pflag_array = ct.pointer(flag_array(*flags))
        
        daq.daqAdcSetScan(self.handle, pchan_array, pgain_array, pflag_array,
                          wt.DWORD(len(channels)))

    def AdcGetScan(self):
        """Reads the current scan group, which consists of all configured\
            channels"""
        channels, gains, flags = []
        chan_array = ct.ARRAY(wt.DWORD, 512)
        pchan_array = ct.pointer(chan_array(*channels))
        gain_array = ct.ARRAY(wt.DWORD, 512)
        pgain_array = ct.pointer(gain_array(*gains))
        flag_array = ct.ARRAY(wt.ARRAY, 512)
        pflag_array = ct.pointer(flag_array(*flags))
        chanCount = ct.c_int(0)
        pchanCount = ct.pointer(chanCount)

        daq.daqAdcSetScan(self.handle, pchan_array, pgain_array, pflag_array,
                            pchanCount)                          

        gainVals = ofValues(bipolarGains, gains)
        flagVals = ofValues(daqAdcFlag, flags)
        vals = {'Channels' : channels, 'Gains' : gainVals,
                'Flags' : flagVals, 'Channelcount' : chanCount}
        return vals

    #One-Step ADC functions

    def AdcRd(self, chan, gain, flags):
        """Takes a single reading from the given local A/D channel using a\
            software trigger"""
        flags = ofKeys(DaqAdcFlag, flags)
        gain = bipolarGains[gain]
        flag_array = ct.ARRAY(wt.ARRAY, len(flags))
        pflag_array = ct.pointer(flag_array(*flags))
        sample = wt.DWORD(0)
        psample = ct.pointer(sample)

        daq.daqAdcRd(self.handle, wt.DWORD(chan), psample, wt.DWORD(gain),
                     pflag_array)

        return sample.value
