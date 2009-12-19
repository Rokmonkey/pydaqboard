def orFlags(flags):

    if type(flags) != list:
        return flags
    elif len(flags) == 1:
        return flags[0]
    else:
        ret = []
        for i in flags:
            tmp = 0
            if type(i) == list:
                for v in i:
                    tmp |= v
                ret.append(tmp)
            else:
                tmp |= i
                ret = tmp
            
    return ret
    

class enum():


    def __init__(self, keys, values):
        self.keys = keys
        self.values = values

    def ofKeys(self, request):
        if type(request) != list:
            index = self.keys.index(request)
            ret = self.values[index]
        else:
            ret = []
            for i in request:
                index = self.keys.index(i)
                ret.append(self.values[index])

        return ret

    def ofValues(self, request):
        if type(request) != list:
            index = self.values.index(request)
            ret = self.keys[index]
        else:
            ret = []
            for i in request:
                index = self.values.index(i)
                ret.append(self.keys[index])
                
        return ret


#ADC Gain Definitions

DaqAdcGaindict = {
'DgainX1'              : 0,
'DgainX2'              : 1,
'DgainX4'              : 2,
'DgainX8'              : 3,
'DgainX16'             : 4, #DaqBoard2000 series only
'DgainX32'             : 5, #DaqBoard2000 series only
'DgainX64'             : 6, #DaqBoard2000 series only

#Base Unit Gain on DBK Connected Channel
#Reference Only : Use DBK Specific Codes in Applications

'DgainX1DbkNone'       : 0,
'DgainX2DbkNone'       : 4,
'DgainX4DbkNone'       : 8,
'DgainX8DbkNone'       : 12,
'DgainX16DbkNone'      : 16, #DaqBoard2000 series only
'DgainX32DbkNone'      : 20, #DaqBoard2000 series only
'DgainX64DbkNone'      : 24, #DaqBoard2000 series only

# Dbk4 - Filter Mode (jumper selectable) 
'Dbk4FilterX1'         : 0,
'Dbk4FilterX10'        : 1,
'Dbk4FilterX100'       : 2,
'Dbk4FilterX1000'      : 3,
'Dbk4FilterX2'         : 4,
'Dbk4FilterX20'        : 5,
'Dbk4FilterX200'       : 6,
'Dbk4FilterX2000'      : 7,
'Dbk4FilterX4'        : 8,
'Dbk4FilterX40'        : 9,
'Dbk4FilterX400'       : 10,
'Dbk4FilterX4000'      : 11,
'Dbk4FilterX8'         : 12,
'Dbk4FilterX80'        : 13,
'Dbk4FilterX800'       : 14,
'Dbk4FilterX8000'      : 15,

# Dbk4 - Bypass Mode (jumper selectable) 
'Dbk4BypassX1_583'     : 0,
'Dbk4BypassX15_83'     : 1,
'Dbk4BypassX158_3'     : 2,
'Dbk4BypassX1583'      : 3,
'Dbk4BypassX3_166'     : 4,
'Dbk4BypassX31_66'     : 5,
'Dbk4BypassX316_6'     : 6,
'Dbk4BypassX3166'      : 7,
'Dbk4BypassX6_332'     : 8,
'Dbk4BypassX63_32'     : 9,
'Dbk4BypassX633_2'     : 10,
'Dbk4BypassX6332'      : 11,
'Dbk4BypassX12_664'    : 12,
'Dbk4BypassX126_64'    : 13,
'Dbk4BypassX1266_4'    : 14,
'Dbk4BypassX12664'     : 15,

   # Dbk6 
   'Dbk6X1'               : 0,
   'Dbk6X4'               : 1,
   'Dbk6X16'              : 2,
   'Dbk6X64'              : 3,
   'Dbk6X2'               : 4,
   'Dbk6X8'               : 5,
   'Dbk6X32'              : 6,
   'Dbk6X128'             : 7,
   'Dbk6X256'             : 11,
   'Dbk6X512'             : 15,
   'Dbk6X1024'            : 19, #DaqBoard2000 series only
   'Dbk6X2048'           : 23, #DaqBoard2000 series only
   'Dbk6X4096'            : 27, #DaqBoard2000 series only

   # Dbk7 Bipolar 
   'Dbk7X1'               : 0,
   'Dbk7X2'               : 4,  #use with PCCard & DaqBoard/2000

   # Dbk8 
   'Dbk8X1'               : 0,
   'Dbk8X2'               : 4,  #use with PCCard & DaqBoard/2000

   # Dbk9 
   'Dbk9VoltageA'         : 0,
   'Dbk9VoltageB'         : 1,
   'Dbk9VoltageC'         : 2,
   'Dbk9VoltageD'         : 3,

   # PCCard Dbk9 use with PCCard & DaqBoard/2000 
   'DbkPCC9VoltageA'      : 4,
   'DbkPCC9VoltageB'      : 5,
   'DbkPCC9VoltageC'      : 6,
   'DbkPCC9VoltageD'      : 7,

   # Dbk12 
   'Dbk12X1'              : 0,
   'Dbk12X2'              : 1,
   'Dbk12X4'              : 2,
   'Dbk12X8'              : 3,
   'Dbk12X16'             : 7,
   'Dbk12X32'            : 11,
   'Dbk12X64'             : 15,
   'Dbk12X128'            : 19, #DaqBoard2000 series only
   'Dbk12X256'           : 23, #DaqBoard2000 series only
   'Dbk12X512'          : 27, #DaqBoard2000 series only

   # Dbk13 
   'Dbk13X1'              : 0,
   'Dbk13X10'             : 1,
   'Dbk13X100'            : 2,
   'Dbk13X1000'           : 3,
   'Dbk13X2'              : 4,
   'Dbk13X20'             : 5,
   'Dbk13X200'            : 6,
   'Dbk13X2000'           : 7,
   'Dbk13X4'              : 8,
   'Dbk13X40'             : 9,
   'Dbk13X400'            : 10,
   'Dbk13X4000'           : 11,
   'Dbk13X8'              : 12,
   'Dbk13X80'             : 13,
   'Dbk13X800'            : 14,
   'Dbk13X8000'           : 15,
   'Dbk13X16'             : 16, #DaqBoard2000 series only
   'Dbk13X160'            : 17, #DaqBoard2000 series only
   'Dbk13X1600'           : 18, #DaqBoard2000 series only
   'Dbk13X16000'          : 19, #DaqBoard2000 series only
   'Dbk13X32'             : 20, #DaqBoard2000 series only
   'Dbk13X320'            : 21, #DaqBoard2000 series only
   'Dbk13X3200'           : 22, #DaqBoard2000 series only
   'Dbk13X32000'          : 23, #DaqBoard2000 series only
   'Dbk13X64'             : 24, #DaqBoard2000 series only
   'Dbk13X640'            : 25, #DaqBoard2000 series only
   'Dbk13X6400'           : 26, #DaqBoard2000 series only
   'Dbk13X64000'          : 27, #DaqBoard2000 series only

   # Dbk14 Bipolar 
   'Dbk14BiCJC'           : 4,
   'Dbk14BiTypeJ'         : 2,
   'Dbk14BiTypeK'         : 2,
   'Dbk14BiTypeT'         : 6,
   'Dbk14BiTypeE'         : 9,
   'Dbk14BiTypeN28'       : 10,
   'Dbk14BiTypeN14'       : 2,
   'Dbk14BiTypeS'         : 6,
   'Dbk14BiTypeR'         : 6,
   'Dbk14BiTypeB'         : 10,

   # PCCard & DaqBoard/2000 Dbk14 Bipolar 
   # place main unit in -5 to +5v range  (additional x2 gain) 
   # bipolar gains only 
   'DbkPCC14BiCJC'        : 8,
   'DbkPCC14BiTypeJ'      : 6,
   'DbkPCC14BiTypeK'      : 6,
   'DbkPCC14BiTypeT'      : 10,
   'DbkPCC14BiTypeE'      : 13,
   'DbkPCC14BiTypeN28'    : 14,
   'DbkPCC14BiTypeN14'    : 6,
   'DbkPCC14BiTypeS'      : 10,
   'DbkPCC14BiTypeR'      : 10,
   'DbkPCC14BiTypeB'      : 14,

   # Dbk14 Unipolar 
   'Dbk14UniCJC'          : 8,
   'Dbk14UniTypeJ'        : 6,
   'Dbk14UniTypeK'        : 6,
   'Dbk14UniTypeT'        : 10,
   'Dbk14UniTypeE'        : 2,
   'Dbk14UniTypeN28'      : 14,
   'Dbk14UniTypeN14'      : 6,
   'Dbk14UniTypeS'        : 10,
   'Dbk14UniTypeR'        : 10,
   'Dbk14UniTypeB'        : 14,

   # Dbk15 Bipolar 
   'Dbk15BiX1'            : 0,
   'Dbk15BiX2'            : 1,

   # Dbk15 Unipolar : Output of card offset to +/-5 V 
   'Dbk15UniX1'           : 2,
   'Dbk15UniX2'           : 3,

   # Dbk16 
   'Dbk16ReadBridge'      : 0,
   'Dbk16SetOffset'       : 1,
   'Dbk16SetScalingGain'  : 2,
   'Dbk16SetInputGain'    : 3,

   # Dbk16 with X2 gain on main unit 
   'DbkPCC16ReadBridge'      : 4,  #use with PCCard & DaqBoard/2000
   'DbkPCC16SetOffset'       : 5,  #use with PCCard & DaqBoard/2000
   'DbkPCC16SetScalingGain'  : 6,  #use with PCCard & DaqBoard/2000
   'DbkPCC16SetInputGain'    : 7,  #use with PCCard & DaqBoard/2000

   # Dbk17 
   'Dbk17X1'              : 0,
   'Dbk17X2'              : 4,  #use with PCCard & DaqBoard/2000

   # Dbk18 
   'Dbk18X1'              : 0,
   'Dbk18X2'              : 4,  #use with PCCard & DaqBoard/2000

   # Dbk19 Bipolar 
   'Dbk19BiCJC'           : 0,
   'Dbk19BiTypeJ'         : 1,
   'Dbk19BiTypeK'         : 1,
   'Dbk19BiTypeT'         : 2,
   'Dbk19BiTypeE'         : 0,
   'Dbk19BiTypeN28'       : 3,
   'Dbk19BiTypeN14'       : 1,
   'Dbk19BiTypeS'         : 3,
   'Dbk19BiTypeR'         : 2,
   'Dbk19BiTypeB'         : 3,

   # PCCard & DaqBoard/2000 Dbk19 Bipolar 
   # place main unit in -5 to +5v range  (additional x2 gain) 
   # bipolar gains only 
   'DbkPCC19BiCJC'        : 4,
   'DbkPCC19BiTypeJ'      : 5,
   'DbkPCC19BiTypeK'      : 5,
   'DbkPCC19BiTypeT'      : 6,
   'DbkPCC19BiTypeE'     : 4,
   'DbkPCC19BiTypeN28'    : 7,
   'DbkPCC19BiTypeN14'    : 5,
   'DbkPCC19BiTypeS'      : 7,
   'DbkPCC19BiTypeR'      : 6,
   'DbkPCC19BiTypeB'      : 7,

   # Dbk19 Unipolar 
   'Dbk19UniCJC'          : 1,
   'Dbk19UniTypeJ'        : 2,
   'Dbk19UniTypeK'        : 2,
   'Dbk19UniTypeT'        : 3,
   'Dbk19UniTypeE'        : 1,
   'Dbk19UniTypeN28'      : 3,
   'Dbk19UniTypeN14'      : 2,
   'Dbk19UniTypeS'        : 3,
   'Dbk19UniTypeR'        : 3,
   'Dbk19UniTypeB'        : 3,

   # Dbk42 
   'Dbk42X1'              : 0,
   'Dbk42X2'              : 4,  #use with PCCard & DaqBoard/2000

   # Dbk43 
   'Dbk43ReadBridge'      : 0,
   'Dbk43SetOffset'       : 1,
   'Dbk43SetScalingGain'  : 2,
   'Dbk43SetInputGain'    : 3,

   # Dbk43 with X2 gain on main unit 
   'DbkPCC43ReadBridge'      : 4,  #use with PCCard & DaqBoard/2000
   'DbkPCC43SetOffset'       : 5,  #use with PCCard & DaqBoard/2000
   'DbkPCC43SetScalingGain'  : 6,  #use with PCCard & DaqBoard/2000
   'DbkPCC43SetInputGain'    : 7,  #use with PCCard & DaqBoard/2000

   # Dbk44 
   'Dbk44X1'              : 0,
   'Dbk44X2'              : 4,  #use with PCCard & DaqBoard/2000

   # Dbk45 
   'Dbk45X1'              : 0,
   'Dbk45X2'              : 4,  #use with PCCard & DaqBoard/2000

   # Dbk50 
   'Dbk50Range0'          : 0,
   'Dbk50Range10'         : 1,
   'Dbk50Range100'        : 2,
   'Dbk50Range300'        : 3,
   
   # Dbk50 with X2 gain on main unit 
   'DbkPCC50Range0'       : 4,  #use with PCCard & DaqBoard/2000
   'DbkPCC50Range10'      : 5,  #use with PCCard & DaqBoard/2000
   'DbkPCC50Range100'     : 6,  #use with PCCard & DaqBoard/2000
   'DbkPCC50Range300'     : 7,  #use with PCCard & DaqBoard/2000

   # Dbk51 
   'Dbk51Range0'          : 0,
   'Dbk51Range100mV'      : 1,
   'Dbk51Range1'          : 2,
   'Dbk51Range10'         : 3,

   # Dbk51 with X2 gain on main unit 
   'DbkPCC51Range0'       : 4,  #use with PCCard & DaqBoard/2000
   'DbkPCC51Range100mV'   : 5,  #use with PCCard & DaqBoard/2000
   'DbkPCC51Range1'       : 6,  #use with PCCard & DaqBoard/2000
   'DbkPCC51Range10'      : 7,  #use with PCCard & DaqBoard/2000

   # Dbk52 Bipolar 
   'Dbk52BiCJC'           : 4,
   'Dbk52BiTypeJ'         : 5,
   'Dbk52BiTypeK'         : 5,
   'Dbk52BiTypeT'         : 6,
   'Dbk52BiTypeE'         : 4,
   'Dbk52BiTypeN28'       : 7,
   'Dbk52BiTypeN14'       : 5,
   'Dbk52BiTypeS'         : 7,
   'Dbk52BiTypeR'         : 6,
   'Dbk52BiTypeB'         : 7,

   # PCCard & DaqBoard/2000 Dbk52 Bipolar 
   # place main unit in -5 to +5v range  (additional x2 gain) 
   # bipolar gains only 
   'DbkPCC52BiCJC'        : 4,
   'DbkPCC52BiTypeJ'      : 5,
   'DbkPCC52BiTypeK'      : 5,
   'DbkPCC52BiTypeT'      : 6,
   'DbkPCC52BiTypeE'      : 4,
   'DbkPCC52BiTypeN28'    : 7,
   'DbkPCC52BiTypeN14'    : 5,
   'DbkPCC52BiTypeS'      : 7,
   'DbkPCC52BiTypeR'      : 6,
   'DbkPCC52BiTypeB'      : 7,

   # Dbk52 Unipolar 
   'Dbk52UniCJC'          : 1,
   'Dbk52UniTypeJ'        : 2,
   'Dbk52UniTypeK'        : 2,
   'Dbk52UniTypeT'        : 3,
   'Dbk52UniTypeE'        : 1,
   'Dbk52UniTypeN28'      : 3,
   'Dbk52UniTypeN14'      : 2,
   'Dbk52UniTypeS'        : 3,
   'Dbk52UniTypeR'        : 3,
   'Dbk52UniTypeB'        : 3,

   # Dbk70 
   'Dbk70X1'              : 0,
   'Dbk70X2'              : 4,  #Use with PCCard or DaqBoard/2000 and DafBipolar (+/-5V)
                               #all others with DafUnipolar (or jumper) (0-5V)
   'Dbk70X4'              : 8,  #Use with DaqBoard/2000 and DafUnipolar (0-5V)   

   # Dbk80 
   'Dbk80X1'              : 0,
   'Dbk80X2'              : 4, #gain on DaqBook/Board itself
   'Dbk80X4'              : 4,
   'Dbk80X8'              : 8,
   'Dbk80X16'             : 16, #DaqBoard2000 series only
   'Dbk80X32'             : 20, #DaqBoard2000 series only
   'Dbk80X64'             : 24, #DaqBoard2000 series only


   # DaqBook/Board 100,112,120,200,216,260 ONLY! 
   # Dbk81 & Dbk82 - Bipolar Only 
   'Dbk81CJC'           : 0,
   'Dbk81TypeJ'         : 0,
   'Dbk81TypeK'         : 0,
   'Dbk81TypeT'         : 4,
   'Dbk81TypeE'         : 0,
   'Dbk81TypeN28'       : 4,
   'Dbk81TypeN14'       : 0,
   'Dbk81TypeS'         : 4,
   'Dbk81TypeR'         : 4,
   'Dbk81TypeB'         : 4,

   'Dbk81x100'          : 0, #Voltage Mode (+/- 50mV) Actual gain of 9

#PCCard & DaqBoard/2000 Dbk81 & Dbk82 - Bipolar Only
#places main unit in -5 to +5v range  (additional x2 gain)
#bipolar gains only


'DbkPCC81CJC'        : 4,
'DbkPCC81TypeJ'      : 4,
'DbkPCC81TypeK'      : 4,
'DbkPCC81TypeT'      : 8,
'DbkPCC81TypeE'      : 4,
'DbkPCC81TypeN28'    : 8,
'DbkPCC81TypeN14'    : 4,
'DbkPCC81TypeS'      : 8,
'DbkPCC81TypeR'      : 8,
'DbkPCC81TypeB'      : 8,
'DbkPCC81x100'       : 2,

   # Dbk207 #
   'Dbk207X1'             : 0,
   'Dbk207X2'             : 4,  #use with PCCard & DaqBoard/2000


   # Wavebook gain codes #
   'WgcX1'                : 0,
   'WgcX2'                : 1,
   'WgcX5'                : 2,
   'WgcX10'               : 3,
   'WgcX20'               : 4, #Wbk11, 12, 13, & Wbk14 only
   'WgcX50'               : 5, #Wbk11, 12, 13, & Wbk14 only
   'WgcX100'              : 6, #Wbk11, 12, 13, & Wbk14 only
   'WgcX200'              : 7, #Wbk10A with Wbk11,12,or 13 installed, & Wbk14 only

   #WaveBook digital gain codes NOT currently used! : Use WgcX1 and set DaqAdcFlags as required
   'WgcDigital8'          : 8, #8-Bit Digital              : proper DaqAdcFlags also required
   'WgcDigital16'         : 9, #16-Bit Digital             : proper DaqAdcFlags also required
   'WgcCtr16'             : 10,#16-Bit Countet/Timer       : proper DaqAdcFlags also required
   'WgcCtr32Low'          : 11,#32-Bit Counter (High Byte) : proper DaqAdcFlags also required
   'WgcCtr32High'         : 12,#32-Bit Counter (Low Byte)  : proper DaqAdcFlags also required
 
   # TempBook/66 voltage gain codes #
   'TgainX1'                : 0,
   'TgainX2'                : 1,
   'TgainX5'                : 2,
   'TgainX10'               : 3,
   'TgainX20'               : 5,
   'TgainX50'               : 6,
   'TgainX100'              : 7,
   'TgainX200'              : 11,

   # TempBook/66 Thermocouple Bipolar #
   'TbkBiCJC'               : 6,
   'TbkBiTypeJ'             : 7,
   'TbkBiTypeK'             : 7,
   'TbkBiTypeT'             : 11,
   'TbkBiTypeE'             : 6,
   'TbkBiTypeN28'           : 7,
   'TbkBiTypeN14'           : 7,
   'TbkBiTypeS'             : 11,
   'TbkBiTypeR'             : 11,
   'TbkBiTypeB'             : 11,
   
   # TempBook/66 Thermocouple Unipolar #
   'TbkUniCJC'              : 7,
   'TbkUniTypeJ'            : 11,
   'TbkUniTypeK'            : 11,
   'TbkUniTypeT'            : 11,
   'TbkUniTypeE'            : 7,
   'TbkUniTypeN28'          : 11,
   'TbkUniTypeN14'          : 11,
   'TbkUniTypeS'            : 11,
   'TbkUniTypeR'            : 11,
   'TbkUniTypeB'            : 11,

#pDaq gain types

'PgainDiv5'              : 8,
'PgainX1'                : 0,
'PgainX2'                : 1,
'PgainX4'                : 16,
'PgainX8'                : 17,
'PgainX16'               : 18,
'PgainX32'               : 19,
'PgainX64'               : 20,
'PgainX128'              : 21

}

DaqAdcGain = enum(DaqAdcGaindict.keys(), DaqAdcGaindict.values())
                  
#ADC Flag Definitions
DaqAdcFlagdict = {

   #Unipolar/Bipolar Flag
   'DafUnipolar'          : 0x00,
   'DafBipolar'           : 0x02,

   #Unsigned/Signed ADC Data Flag
   'DafUnsigned'          : 0x00,
   'DafSigned'            : 0x04,

   #Single Ended/Differential Flag
   'DafSingleEnded'       : 0x00,
   'DafDifferential'      : 0x08,
   'DafSingleEndedLow'    : 0x0000,  #pDaq Type
   'DafSingleEndedHigh'   : 0x1000,  #pDaq Type

   # SSH Hold/Sample Flag - For Internal Use Only 
   'DafSSHSample'         : 0x00,
   'DafSSHHold'           : 0x10,

   # Analog/High Speed Digital Flag 
   'DafAnalog'            : 0x00,
   'DafHighSpeedDigital'  : 0x01,
   # pDaq Digital or Counter Flag 
   'DafScanDigital'       : 0x01, 
   #WaveBook Digital Channel Flags    
   'DafDigital8'          : 0x001,
   'DafDigital16'         : 0x101,   
   # Daq2000 P2/P3 Digital Channel Flags 
   'DafP2Local8'          : 0x2001,
   'DafP2Exp8'            : 0x4001,
   'DafP3Local16'         : 0x0001,
 
   #WaveBook & Daq2000 Counter Channel Flags    
   'DafCtr16'             : 0x201,
   'DafCtr32Low'          : 0x401,
   'DafCtr32High'         : 0x801,
   # Daq2000 Counter Edge Flags 
   'DafCtrRisingEdge'     : 0x00000,
   'DafCtrFallingEdge'    : 0x10000,
   # pDaq & Daq2000 Counter Types 
   'DafCtrPulse'          : 0x20000,
   'DafCtrTotalize'       : 0x40000,
   # pDaq Digital and Counter Types 
   'DafDioDirect'         : 0x00000,
   'DafCtrFreq'           : 0x80000,
   'DafCtrDutyLo'         : 0x100000,
   'DafCtrDutyHi'         : 0x200000,

   # pDaq Notch Frequencies 
   'DafMeasDuration610'   : 0x000000,
   'DafMeasDuration370'   : 0x100000,
   'DafMeasDuration310'   : 0x200000,
   'DafMeasDuration130'   : 0x300000,
   'DafMeasDuration110'   : 0x400000,
   'DafMeasDuration40'    : 0x500000,
   'DafMeasDuration20'    : 0x600000,
   'DafMeasDuration12_5'  : 0x700000,
   
   #Daq2000 Settling Time Control 
   'DafSettle5us'         : 0x000000,
   'DafSettle10us'        : 0x800000,

   # Clear or shift the least significant nibble
   #- typically used with 12-bit ADCs 
   'DafIgnoreLSNibble'    : 0x00,
   'DafClearLSNibble'     : 0x20,
   'DafShiftLSNibble'     : 0x40,
   #Shift the least significant Digital Byte
   #- typically used with 8-bit WaveBook DIO port
   'DafDigitalShiftLSByte' :	0x40,

   # pDaq, TempBook, & DBK19/52 Thermocouple Type codes 
   'DafTcTypeNone'        : 0x00,
   'DafTcTypeJ'           : 0x80,
   'DafTcTypeK'           : 0x100,
   'DafTcTypeT'           : 0x180,
   'DafTcTypeE'           : 0x200,
   'DafTcTypeN28'         : 0x280,
   'DafTcTypeN14'         : 0x300,
   'DafTcTypeS'           : 0x380,
   'DafTcTypeR'           : 0x400,
   'DafTcTypeB'           : 0x480,
   'DafTcCJC'             : 0x500,

   #WaveBook Internal Channel Flags   
   'DafIgnoreType'        : 0x1000000,
   }

DaqAdcFlag = enum(DaqAdcFlagdict.keys(), DaqAdcFlagdict.values())


DaqHardwareVersiondict = {
    'DaqBook100'           : 0,
    'DaqBook112'           : 1,
    'DaqBook120'           : 2,
    'DaqBook200'           : 3, #DaqBook/200 or DaqBook/260
    'DaqBook216'           : 4,
    'DaqBoard100'          : 5,
    'DaqBoard112'          : 6,
    'DaqBoard200'          : 7,
    'DaqBoard216'          : 8,
    'Daq112'               : 9,
    'Daq216'               : 10,
    'WaveBook512'          : 11,
    'WaveBook516'          : 12,
    'TempBook66'           : 13,
    'PersonalDaq56'        : 14,
    'WaveBook516_250'      : 15,
    'WaveBook512_10V'      : 16,
    'DaqBoard2000'         : 17,
    'DaqBoard2001'         : 18,
    'DaqBoard2002'         : 19,
    'DaqBoard2003'         : 20,
    'DaqBoard2004'         : 21,
    'DaqBoard2005'         : 22,
    'DaqBook2000'          : 23,
    'DaqBook2001'          : 24,
    'DaqBook2002'          : 25,
    'DaqBook2003'          : 26,
    'DaqBook2004'          : 27,
    'DaqBook2005'          : 28,
    'WaveBook512A'         : 29,
    'WaveBook516A'         : 30,
    'PersonalDaq3000'      : 44
}
                  
DaqHardwareVersion = enum(DaqHardwareVersiondict.keys(), DaqHardwareVersiondict.values())

#Protocal Devinitsions
DaqProtocoldict = {
   'DaqProtocolNone'      : 0,    # Communications not established 
   'DaqProtocol4'         : 1,    # Standard LPT Port 4-bit mode 
   'DaqProtocol8'         : 2,    # Standard LPT Port 8-bit mode 
   'DaqProtocolSMC666'    : 3,    # SMC 37C666 EPP mode 
   'DaqProtocolFastEPP'   : 4,    # WBK20/21 Fast EPP mode 
   'DaqProtocolECP'       : 5,    # Enhanced Capability Port 
   'DaqProtocol8BitEPP'   : 6,    # 8-bit EPP mode 
   'DaqProtocolISA'       : 100,  # ISA bus card DaqBoard 100/200 
   'DaqProtocolPcCard'    : 200,  # PCCard for Daq (PCMCIA) 
   'DaqProtocolUSB'       : 300,  # USB protocol (PersonalDaq) 
   'DaqProtocolPCI'       : 400,  # PCI bus card DaqBoard 2000 
   'DaqProtocolCPCI'      : 500,  # Compact PCI bus card DaqBoard 2000 
}

DaqProtocol = enum(DaqProtocoldict.keys(), DaqProtocoldict.values())

#General Information Selector Definitions

DaqInfodict = {
   'DdiHardwareVersionInfo'      : 0, #(DaqHardwareVersion)
   'DdiProtocolInfo'             : 1,
   'DdiChTypeInfo'               : 2,
   'DdiChOptionTypeInfo'         : 3,
   'DdiADminInfo'                : 4, #ADC Minimum voltage input level in Volts (FLOAT)
   'DdiADmaxInfo'                : 5, #ADC Maximum voltage input level in Volts (FLOAT)
   'DdiChanCountInfo'            : 6,
   'DdiNVRAMDateInfo'            : 7, #Date String
   'DdiNVRAMTimeInfo'            : 8, #Time String
   'DdiDbk4MaxFreqInfo'          : 9,
   'DdiDbk4SetBaselineInfo'      : 10,
   'DdiDbk4ExcitationInfo'       : 11,
   'DdiDbk4ClockInfo'            : 12,
   'DdiDbk4GainInfo'             : 13, #internally used by daqAdcSetScan */
   'DdiDbk7SlopeInfo'            : 14,
   'DdiDbk7DebounceTimeInfo'     : 15,
   'DdiDbk7MinFreqInfo'          : 16,
   'DdiDbk7MaxFreqInfo'          : 17,
   'DdiDbk50GainInfo'            : 18, #internally used by daqAdcSetScan */
   'DdiWbk12FilterCutOffInfo'    : 19,
   'DdiWbk12FilterTypeInfo'      : 20,
   'DdiWbk12FilterModeInfo'      : 21,
   'DdiWbk12PreFilterModeInfo'   : 22,
   'DdiWbk13FilterCutOffInfo'    : 23,
   'DdiWbk13FilterTypeInfo'      : 24,
   'DdiWbk13FilterModeInfo'      : 25,
   'DdiWbk13PreFilterModeInfo'   : 26,
   'DdiWbk14LowPassModeInfo'     : 27,
   'DdiWbk14LowPassCutOffInfo'   : 28,
   'DdiWbk14HighPassCutOffInfo'  : 29,
   'DdiWbk14CurrentSrcInfo'      : 30,
   'DdiWbk14PreFilterModeInfo'   : 31,
   'DdiWbk14ExcSrcWaveformInfo'  : 32,
   'DdiWbk14ExcSrcFreqInfo'      : 33,
   'DdiWbk14ExcSrcAmplitudeInfo' : 34,
   'DdiWbk14ExcSrcOffsetInfo'    : 35,
   'DdiWgcX1Info'                : 36,
   'DdiWgcX2Info'                : 37,
   'DdiWgcX5Info'                : 38,
   'DdiWgcX10Info'               : 39,
   'DdiWgcX20Info'               : 40,
   'DdiWgcX50Info'               : 41,
   'DdiWgcX100Info'              : 42,
   'DdiWgcX200Info'              : 43,
   'DdiPreTrigFreqInfo'          : 44,
   'DdiPostTrigFreqInfo'         : 45,
   'DdiPreTrigPeriodInfo'        : 46,
   'DdiPostTrigPeriodInfo'       : 47,
   'DdiOptNVRAMDateInfo'         : 48,
   'DdiOptNVRAMTimeInfo'         : 49,
   'DdiExtFeatures'              : 50, #DaqHardwareExtFeatures
   'DdipDaqCalibrationTime'      : 50, #Personal Daq initial calibration period in ms 
   'DdiFifoSize'                 : 51, #FIFO capacity in WORD's of data.
   'DdiFifoCount'                : 52, #Count of WORD's of data currently in the FIFO
   'DdiSerialNumber'             : 53, #Serial Number String
   'DdiAdcClockSource'           : 54, #Current Clock Source
   'DdiFirmwareVersion'          : 55, #Firmware Version (String)
   'DdiHardwareVersion'          : 56, #Hardware Version (String)
   'DdiDriverVersion'            : 57, #Driver Version   (String)
   'DdiAdcTriggerScan'           : 58, #Trigger Scan Number (DWORD)          #Not Implemented
   'DdiAdcPreTriggerCount'       : 59, #Amount of Pre-Trigger Scans (DWORD)  #Not Implemented
   'DdiAdcPostTriggerCount'      : 60, #Amount of Post-Trigger Scans (DWORD) #Not Implemented
   'DdiDetectSensor'             : 61, #Detects the presence of an external sensor (DWORD) #WaveBook Wbk14 only
   'DdiWbk12PreFilterCutOffInfo' : 62, #Wbk12/Wbk12A pre-filter cutoff freq (FLOAT)
   'DdiWbk12PostFilterCutOffInfo': 63, #Wbk12A post-filter cutoff freq      (FLOAT)
   'DdiWbk13PreFilterCutOffInfo' : 64, #Wbk13/Wbk13A pre-filter cutoff freq (FLOAT)
   'DdiWbk13PostFilterCutOffInfo': 65, #Wbk13A post-filter cutoff freq      (FLOAT)
   'DdiAdcLastRawTransferCount'  : 66, #undocumented.
   }

DaqInfo = enum(DaqInfodict.keys(), DaqInfodict.values())

#Transfer Event Definitions
DaqTransferEventdict = {
'DteAdcData':0,
'DteAdcDone':1,
'DteDacData':2, #Unsupported
'DteDacDone':3, #Unsupported
'DteIOData':4, #Unsupported
'DteIODone':5 #Unsupported
}

DaqTransferEvent = enum(DaqTransferEventdict.keys(), DaqTransferEventdict.values())

#Transfer Event Wait Mode Definitions
DaqWaitModedict = {
   'DwmNoWait'            : 0,
   'DwmWaitForAny'        : 1,
   'DwmWaitForAll'        : 2
   }

DaqWaitMode = enum(DaqWaitModedict.keys(), DaqWaitModedict.values())

#ADC Acquisition mode Definitions
DaqAdcAcqModedict = {
   'DaamNShot'            : 0,
   'DaamNShotRearm'       : 1, #WaveBook only
   'DaamInfinitePost'     : 2,
   'DaamPrePost'          : 3
   }

DaqAdcAcqMode = enum(DaqAdcAcqModedict.keys(), DaqAdcAcqModedict.values())

DaqAdcAcqStatedict = {
    'DaasPreTrig':0,
    'DaasPostTrig':1
    }

DaqAdcAcqState = enum(DaqAdcAcqStatedict.keys(), DaqAdcAcqStatedict.values())

#ADC Transfer Mask Definitions
DaqAdcTransferMaskdict = {
   'DatmCycleOff'         : 0x00,
   'DatmCycleOn'          : 0x01,

   'DatmUpdateBlock'      : 0x00,
   'DatmUpdateSingle'     : 0x02,   
   'DatmUpdateAny'        : 0x04,

   'DatmUserBuf'          : 0x00,
   'DatmDriverBuf'        : 0x08,
   'DatmIgnoreOverruns'   : 0x10,

   #WaveBook Only : Enable user-buffer overflow protection. NOTE: This mode 
   #changes the usage of the active and retCount arguments of daqGetTransferStat
   'DatmPacingMode'       : 0x20
   }

DaqAdcTransferMask = enum(DaqAdcTransferMaskdict.keys(), DaqAdcTransferMaskdict.values())

DaqAdcTriggerSourcedict = {
   'DatsImmediate'        : 0,
   'DatsSoftware'         : 1,
   'DatsAdcClock'         : 2,
   'DatsGatedAdcClock'    : 3,
   'DatsExternalTTL'      : 4,
   'DatsHardwareAnalog'   : 5,
   'DatsSoftwareAnalog'   : 6,
   'DatsEnhancedTrig'     : 7,  #WaveBook series only
   'DatsDigPattern'       : 8,
   'DatsPulse'            : 9,  #WaveBook/516 only
   'DatsScanCount'        : 10, #Stop Event only
   'DatsCounter'          : 6  #DaqBoard2000 series only
   }

DaqAdcTriggerSource = enum(DaqAdcTriggerSourcedict.keys(), DaqAdcTriggerSourcedict.values())

#Enhanced Trigger Sens Definitions
DaqEnhTrigSensTdict = {
   'DetsRisingEdge'                 :   0,
   'DetsFallingEdge'                :   1,
   'DetsAboveLevel'                 :   2,
   'DetsBelowLevel'                 :   3,
   'DetsAfterRisingEdge'            :   4,
   'DetsAfterFallingEdge'           :   5,
   'DetsAfterAboveLevel'            :   6,
   'DetsAfterBelowLevel'            :   7,
   'DetsEQLevel'                    :   8,
   'DetsNELevel'                    :   9,  
   #WaveBook/516
   'DetsWindowAboveLevelBeforeTime' :   10,
   'DetsWindowAboveLevelAfterTime'  :   11,
   'DetsWindowBelowLevelBeforeTime' :   12,
   'DetsWindowBelowLevelAfterTime'  :   13
   }

DaqEnhTrigSensT = enum(DaqEnhTrigSensTdict.keys(), DaqEnhTrigSensTdict.values())

#Channel Type Definitions for Trigger Calculations
DaqChannelTypedict = {
    
'DaqTypeAnalogLocal'   : 0,
'DaqTypeDigitalLocal'  : 100000,
'DaqTypeDigitalExp'    : 200000,
'DaqTypeCounterLocal'  : 400000,

'DaqTypeDBK1'    : 1,
	
'DaqTypeDBK4'	: 4,
	
'DaqTypeDBK6'	: 6,
'DaqTypeDBK7'	: 7,
'DaqTypeDBK8'	: 8,
'DaqTypeDBK9'	: 9,
	
'DaqTypeDBK12'	: 12,
'DaqTypeDBK13'	: 13,
'DaqTypeDBK14'	: 14,
'DaqTypeDBK15'	: 15,
'DaqTypeDBK16'	: 16,
'DaqTypeDBK17'	: 17,
'DaqTypeDBK18'	: 18,
'DaqTypeDBK19'	: 19,
	
'DaqTypeDBK20'	: 20,
'DaqTypeDBK21'	: 21,
'DaqTypeDBK23'	: 23,
'DaqTypeDBK24'	: 24,
'DaqTypeDBK25'	: 25,
	
'DaqTypeDBK42'	: 42,
'DaqTypeDBK43'	: 43,
'DaqTypeDBK44'	: 44,
'DaqTypeDBK45'	: 45,

'DaqTypeDBK50'	: 50,
'DaqTypeDBK51'	: 51,
'DaqTypeDBK52'	: 52,
'DaqTypeDBK53'	: 53,
'DaqTypeDBK54'	: 54,
'DaqTypeDBK56'	: 56,
'DaqTypeDBK70'	: 70,

'DaqTypeDBK80'	: 80,
'DaqTypeDBK81'	: 81,
'DaqTypeDBK82'	: 82,

'DaqTypeDBK207'	: 207,
'DaqTypeDBK208'	: 208
}

DaqChannelType = enum(DaqChannelTypedict.keys(), DaqChannelTypedict.values())

#Trigger Event Flags
DaqTriggerEventdict = {
'DaqStartEvent'	: 0,
'DaqStopEvent'	: 1
}

DaqTriggerEvent = enum(DaqTriggerEventdict.keys(), DaqTriggerEventdict.values())

#ADC Acquisition/Transfer Active Flag Definitions
DaqAdcActiveFlagdict = {
'DaafAcqActive':0x01,
'DaafAcqTriggered':0x02,
'DaafTransferActive':0x04,
'DaafAcqArmed':0x08,
'DaafAcqDataPresent':0x10
}

DaqTriggerEvent = enum(DaqTriggerEventdict.keys(), DaqTriggerEventdict.values())

#Setup and Retrieve Freq. or Period */
DaqAdcRateModedict = {
   'DarmPeriod'           : 0,
   'DarmFrequency'        : 1,
   'DarmExtClockPacer'    : 2,
   'DarmTTLPacer'         : 3
}

DaqAdcRateMode = enum(DaqAdcRateModedict.keys(), DaqAdcRateModedict.values())

#DAC Device Type Definitions */
DaqDacDeviceTypedict = {
   'DddtLocal'            : 0,	
   'DddtDbk'              : 1,
   #Daq2000 Digital Streaming Control */   
   'DddtLocalDigital'     : 2
}

DaqDacDeviceType = enum(DaqDacDeviceTypedict.keys(), DaqDacDeviceTypedict.values())

DaqHardwareInfodict = {
    'DhiHardwareVersion':0,
    'DhiProtocol':1,
    'DhiADmin':3,
    'DhiADmax':4
    }

DaqHardwareInfo = enum(DaqHardwareInfodict.keys(), DaqHardwareInfodict.values())
