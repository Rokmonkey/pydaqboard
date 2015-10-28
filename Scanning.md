
```
from daq import daqDevice
import daqh #Used later on

dev = daqDevice('DaqBoard2K0')
```

Import daq.py and turn the device on. 'DaqBoard2K0' is the name of the device installed on the computer, yours may be different, use the GetDeviceList() function to see the names of the devices installed on your own computer.

And you are done.  You're device is online and ready for configuration.

## Setup the scan configuration ##

Setting up the scan configuration is simple to script, however making sure you have the correct flags, gains, channel groups setup correctly is very device specific and if you are getting error messages through a pop-up menu rather than through the Python shell, look up the error code and check if your setup is correct.

For the purpose of this example, a scan will be configured for channel 0, across the full -10.0 to +10.0 range of the DaqBoard2000.  Best thing to do after initializing is to setup those variables like so:

```
channels = [0]
gains = [daqh.DgainX1]
flags = [daqh.DafBipolar]
scans = 10
```

channels, gains and flags must be passed as lists even if you are using one variable.  They are passed to the library as arrays and will get very angry if not done so.

So what we have done here is defined the channels we want as just channel 0.  We are using a gain of 'DgainX1' and a flag of 'DafBipolar' which sums up to, no gain at all, going both positive and negative.  Bipolar is defined as a range from -maxVolt to +maxVolt, and with a gain of X1 on a DaqBoard2000 such as in this example it is a range from -10.0V to +10.0V.

We also defined a variable scans here.  It is used later on to help configure the size of the buffer where the scan will get added too.  It's mentioned here to keep the scan configuration variables together.

Generally, before you configure the scan, it is common practice to setup the Acquisition mode like so:

```
acqmode = daqhDaamNShot
dev.AdcSetAcq(acqmode, postTrigCount = scans)
```

Here we set the acquisition mode to 'DaamNShot' which basically runs the number of preTrigScans, triggers the full scan, then scans the number of postTrigScans, and disarms the acquistion.  For simplicities sake, our scan will be just 10 postTrigScans as you see here.

Now once the acquisition mode is set you can setup the scan configuration like so:

```
dev.AdcSetScan(channels, gains, flags)
```

Remember, if you want to run a scan on more than one channel using AdcSetScan, your lists for channels, gains and flags must correspond, where `gains[0]` is the gain key for `channels[0]`, and `flags[0]` is all of the flags for `channels[0]` all `|` together.

And thats that, scan is configured.

## Setup the scan rate and transfer buffer ##

Each scan is configured with a sampling rate like so:

```
mode = daqh.DarmPeriod
state = daqh.DaasPostTrig
period = 1000000.0

dev.AdcSetRate(mode, state, period)
```

The function should be self explanatory.  Mode, is a keyword to describe how you will time the scan, in this case 'DarmPeriod' is used to scan using a set period.  'DarmFrequency' is also available, though I have had little luck getting it to be nice.  State indicates the acquisition state the scan rate applies to, either post-trigger or pre-trigger.

Once that is set up, a buffer must be allocated.  This requires more attention in low-level languages like C, but not so for Python.  It will return a list of the values scanned in.  The command takes two arguments, a list of transfer flags, and the number of scans to properly allocate space, in the case of this tutorial that is 10 scans.

```
transMask = [daqh.DatmUpdateSingle,daqh.DatmCycleOn]

buf = dev.AdcTransferSetBuffer(transMask, scans)
```

More information regarding the flags is available in the programmers documentation of your Daqboards API shipped with the device.  Here, 'DatmUpdateSingle' updates the buffer each scan, and 'DatmCycleOn' will loop over the buffer if the end of the buffer is reached thus overwriting data, and is terminated when the transfer is stopped or reaches the trigger count defined.

## Setup trigger events ##

Once the scan itself has been configured, next, the start and stop trigger events have to be configured.

```
dev.SetTriggerEvent(daqh.DatsImmediate,None, 0, gains, flags, daqh.DaqTypeAnalogLocal, 0, 0, daqh.DaqStartEvent)

dev.SetTriggerEvent(daqh.DatsScanCount,None, 0, gains, flags, daqh.DaqTypeAnalogLocal, 0, 0, daqh..DaqStopEvent)
```

daqx.SetTriggerEvent() has a large number of arguments, however, for most applications this isn't needed.  Here, we are using software triggers to make things simple.  The first trigger event is the start event and is configured to trigger as soon as the transfer is armed, with the 'DatsImmediate' flag.

The second event is a Stop event, and is configured to stop after a set number of scans we defined with daqx.AdcSetAcq and set up the post-trig scan count.  As soon as the required number of scans will run.

## Arm and trigger the acquisition ##

```
dev.AdcTransferStart()

dev.AdcArm()

while True:
    stat = dev.AdcTransferGetStat()
    active = stat['active']
    if not (active & daqh.DaafAcqActive):
        break
```

Here we do a little bit of actual coding and not just simple configuration.  We start the transfer with dev.AdcTransferStart() to prepare the transfer, then arm it with dev.AdcArm() which executes the trigger event and begins the scan.  As that continues to work we enter the main loop.

Without this while loop the program would arm the transfer then immediately disarm it.  We don't want that, so what occurs here is we request the status of the transfer occurring.  dev.AdcTransferGetStat() returns a dictionary of the flags describing the current transfer status.  To check the flag, we check the `DaafAcqActive` flag which is no longer set if the scan has ended.  If the transfer is no longer active we can break the loop and disarm the transfer.

## Disarm and evaluate the results ##

Once the transfer is finished, the transfer should be disarmed and stopped and then the results can be evaluated.

```
dev.AdcDisarm()
dev.AdcTransferStop()
```

dev.AdcDisarm() will disarm the transfer and dev.AdcTransferStop() stops it so nothing is being read.

```
for i in buf:
    print dev.ADConvert(i)

dev.Close()
```

Remember, we defined a variable `buf` where the data scanned is returned to. The buffer is returned as a list, so it can be iterated across as we do here. dev.ADConvert() is a simple conversion function within the daq module.  It is created for a very specific type of scan, a BiPolar, 1x Gain on a Daqboard2000.  In normal applications it is much more proper to write your own function specific to the scan configured.

Once the data is evaluated, remember to close the device to eliminate any issues that may arise from a device being brought online more than once.