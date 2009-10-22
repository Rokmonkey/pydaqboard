
def ofKeys(dictionary, keys):
    values = []
    for i in keys:
        values.append(dictionary[i])
    return values

def ofValues(dictionary, values):
    reverseDict = {}
    keys = []
    
    for k,v in dictionary.iteritems():
        reverseDict[v]=k
        
    for i in values:
        keys.append(reverseDict[i])
    return keys


#ADC Gain Definitions

baseUnits = {
'DgainX1'              : 0,
'DgainX2'              : 1,
'DgainX4'              : 2,
'DgainX8'              : 3,
'DgainX16'             : 4, #DaqBoard2000 series only
'DgainX32'             : 5, #DaqBoard2000 series only
'DgainX64'             : 6 #DaqBoard2000 series only
}
#Base Unit Gain on DBK Connected Channel
#Reference Only : Use DBK Specific Codes in Applications

baseUnitGain = {
'DgainX1DbkNone'       : 0,
'DgainX2DbkNone'       : 4,
'DgainX4DbkNone'       : 8,
'DgainX8DbkNone'       : 12,
'DgainX16DbkNone'      : 16, #DaqBoard2000 series only
'DgainX32DbkNone'      : 20, #DaqBoard2000 series only
'DgainX64DbkNone'      : 24 #DaqBoard2000 series only
}
#PCCard & DaqBoard/2000 Dbk81 & Dbk82 - Bipolar Only
#places main unit in -5 to +5v range  (additional x2 gain)
#bipolar gains only

bipolarGains = {
'DbkPCC81CJC'        : baseUnitGain['DgainX2DbkNone'],
'DbkPCC81TypeJ'      : baseUnitGain['DgainX2DbkNone'],
'DbkPCC81TypeK'      : baseUnitGain['DgainX2DbkNone'],
'DbkPCC81TypeT'      : baseUnitGain['DgainX4DbkNone'],
'DbkPCC81TypeE'      : baseUnitGain['DgainX2DbkNone'],
'DbkPCC81TypeN28'    : baseUnitGain['DgainX4DbkNone'],
'DbkPCC81TypeN14'    : baseUnitGain['DgainX2DbkNone'],
'DbkPCC81TypeS'      : baseUnitGain['DgainX4DbkNone'],
'DbkPCC81TypeR'      : baseUnitGain['DgainX4DbkNone'],
'DbkPCC81TypeB'      : baseUnitGain['DgainX4DbkNone']
}
#pDaq gain types

daqGain = {
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

#ADC Flag Definitions
DaqAdcFlag = {

   #Unipolar/Bipolar Flag
   'DafUnipolar'          : 0x00,
   'DafBipolar'           : 0x02,

   #Unsigned/Signed ADC Data Flag
   'DafUnsigned'          : 0x00,
   'DafSigned'            : 0x04,

   #Single Ended/Differential Flag
   'DafSingleEnded'       : 0x00,
   'DafDifferential'      : 0x08,
   'DafSingleEndedLow'    : 0x0000,  #// pDaq Type
   'DafSingleEndedHigh'   : 0x1000,  #// pDaq Type

   # SSH Hold/Sample Flag - For Internal Use Only */
   'DafSSHSample'         : 0x00,
   'DafSSHHold'           : 0x10,

   # Analog/High Speed Digital Flag */
   'DafAnalog'            : 0x00,
   'DafHighSpeedDigital'  : 0x01,
   # pDaq Digital or Counter Flag */
   'DafScanDigital'       : 0x01, 
   #WaveBook Digital Channel Flags */   
   'DafDigital8'          : 0x001,
   'DafDigital16'         : 0x101,   
   # Daq2000 P2/P3 Digital Channel Flags */
   'DafP2Local8'          : 0x2001,
   'DafP2Exp8'            : 0x4001,
   'DafP3Local16'         : 0x0001,
 
   #WaveBook & Daq2000 Counter Channel Flags */   
   'DafCtr16'             : 0x201,
   'DafCtr32Low'          : 0x401,
   'DafCtr32High'         : 0x801,
   # Daq2000 Counter Edge Flags */
   'DafCtrRisingEdge'     : 0x00000,
   'DafCtrFallingEdge'    : 0x10000,
   # pDaq & Daq2000 Counter Types */
   'DafCtrPulse'          : 0x20000,
   'DafCtrTotalize'       : 0x40000,
   # pDaq Digital and Counter Types */
   'DafDioDirect'         : 0x00000,
   'DafCtrFreq'           : 0x80000,
   'DafCtrDutyLo'         : 0x100000,
   'DafCtrDutyHi'         : 0x200000,

   # pDaq Notch Frequencies */
   'DafMeasDuration610'   : 0x000000,
   'DafMeasDuration370'   : 0x100000,
   'DafMeasDuration310'   : 0x200000,
   'DafMeasDuration130'   : 0x300000,
   'DafMeasDuration110'   : 0x400000,
   'DafMeasDuration40'    : 0x500000,
   'DafMeasDuration20'    : 0x600000,
   'DafMeasDuration12_5'  : 0x700000,
   
   #Daq2000 Settling Time Control */
   'DafSettle5us'         : 0x000000,
   'DafSettle10us'        : 0x800000,

   # Clear or shift the least significant nibble
   #- typically used with 12-bit ADCs */
   'DafIgnoreLSNibble'    : 0x00,
   'DafClearLSNibble'     : 0x20,
   'DafShiftLSNibble'     : 0x40,
   #Shift the least significant Digital Byte
   #- typically used with 8-bit WaveBook DIO port*/
   'DafDigitalShiftLSByte' :	0x40,

   # pDaq, TempBook, & DBK19/52 Thermocouple Type codes */
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

   #WaveBook Internal Channel Flags */  
   'DafIgnoreType'        : 0x1000000,
   }

DaqHardwareVersion = {
    'DaqBook100'           : 0,
    'DaqBook112'           : 1,
    'DaqBook120'           : 2,
    'DaqBook200'           : 3, #// DaqBook/200 or DaqBook/260
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
}
#Protocal Devinitsions
DaqProtocol = {
   'DaqProtocolNone'      : 0,    #/* Communications not established */
   'DaqProtocol4'         : 1,    #/* Standard LPT Port 4-bit mode */
   'DaqProtocol8'         : 2,    #/* Standard LPT Port 8-bit mode */
   'DaqProtocolSMC666'    : 3,    #/* SMC 37C666 EPP mode */
   'DaqProtocolFastEPP'   : 4,    #/* WBK20/21 Fast EPP mode */
   'DaqProtocolECP'       : 5,    #/* Enhanced Capability Port */
   'DaqProtocol8BitEPP'   : 6,    #/* 8-bit EPP mode */
   'DaqProtocolISA'       : 100,  #/* ISA bus card DaqBoard 100/200 */
   'DaqProtocolPcCard'    : 200,  #/* PCCard for Daq (PCMCIA) */
   'DaqProtocolUSB'       : 300,  #/* USB protocol (PersonalDaq) */
   'DaqProtocolPCI'       : 400,  #/* PCI bus card DaqBoard 2000 */
   'DaqProtocolCPCI'      : 500,  #/* Compact PCI bus card DaqBoard 2000 */
}
