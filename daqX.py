import ctypes as ct
from ctypes import wintypes as wt

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

#Device Initialization Functions
    
def daqOpen(deviceName):
    """Open the appropriate daqboard"""

    deviceNamepnt = ct.c_char_p(deviceName)
    daq.daqOpen(deviceNamepnt)

def daqGetDeviceCount():
    """Returns the number of currently configured devices"""

    deviceCount = ct.c_int(0)
    deviceCountpnt = ct.pointer(deviceCount)
    daq.daqGetDeviceCount(deviceCountpnt)
    return deviceCount.value

def daqGetDeviceList():
    """Returns a list of currently configured device names"""

    string = ct.c_char_p('')
    count = ct.c_int(0)
    countpnt = ct.pointer(count)
    daq.daqGetDeviceList(string, countpnt)

    return string.value

def daqClose(handle):
    """Used to close a device"""

    daq.daqClose(handle)

def daqOnline(handle):
    """Determines if a device is online"""

    online = ct.c_bool(False)
    onlinepnt = ct.pointer(online)
    daq.daqOnline(handle, onlinepnt)

    return online.value

def daqGetDeviceProperties(deviceName):
    """Returns the properties for a specified device"""

    deviceNamepnt = ct.c_char_p(deviceName)
    devProps = deviceProps()
    devicePropspnt = ct.pointer(devProps)
    daq.daqGetDeviceProperties(deviceNamepnt,devicePropspnt)

    print(devProps)
    
#Error Handler Functions

def daqDefaultErrorHandler(handle):
    """Displays an error message and then exits the application program"""
    
    errCode = ct.c_int
    daq.daqDefaultErrorHandler(handle, errCode)

    return errCode.value

def daqFormatError(errorNum):
    """Returns the text-string equivalent for the
        specified error condition code"""

    msg = ct.c_char_p
    daq.daqFormatError(errorNum, msg)

    return msg.value

def daqGetLastError(handle, err):
    """Retrieves the last error condition code registered by the driver"""

    errCode = ct.c_int(err)
    daq.daqGetLastError(handle, errCode)

    return errCode.value

def daqProcessError(handle, err):
    """Initiates an error for processing by the driver"""

    errCode = ct.c_int(err)
    daq.daqGetLastError(handle, errCode)

def daqSetDefaultErrorHandler(handler):
    """Sets the driver to use the default error handler specified
        for all devices"""

    handlerpnt = ct.POINTER(handler)
    daq.daqSetDefaultErrorHandler(handlerpnt)

def daqSetErrorHandler(handle, handler):
    """Specifies the routine to call when an error occurs in any function
        for the specified device"""

    handlepnt = ct.POINTER(handler)
    daq.daqSetErrorHandler(handle, handlepnt)

def GetDriverVersion():
    """Retrieves the revision level of the driver currently in use"""

    version = ct.c_float
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
        info = c_int
        pinfo = pointer(info)
        daq.daqGetInfo(self.handle, chan, whichInfo, pinfo)

        return info.value

    
        

        

    
