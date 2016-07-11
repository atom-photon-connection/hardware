# D2KDask64.h
# Author: Dustin Stuart
# Date: 23 March 2016

from numpy import zeros
from ctypes import *

# Windows API data types
BOOLEAN = c_ubyte
HANDLE = c_void_p
ULONG_PTR = c_void_p

# Import DLL using the __stdcall convention
dll = WinDLL('D2K-Dask64')

# DAQ2000 Device
DAQ_2010 = 1
DAQ_2205 = 2
DAQ_2206 = 3
DAQ_2005 = 4
DAQ_2204 = 5
DAQ_2006 = 6
DAQ_2501 = 7
DAQ_2502 = 8
DAQ_2208 = 9
DAQ_2213 = 10
DAQ_2214 = 11
DAQ_2016 = 12
DAQ_2020 = 13
DAQ_2022 = 14

# DASK Data Types
I16 = c_short
I32 = c_long
F32 = c_float
F64 = c_double
U8  = c_ubyte
U16 = c_ushort
U32 = c_ulong

MAX_CARD = 32

# Error Number
error_code = {
	0 : "NoError",
	-1 : "ErrorUnknownCardType",
	-2 : "ErrorInvalidCardNumber",
	-3 : "ErrorTooManyCardRegistered",
	-4 : "ErrorCardNotRegistered",
	-5 : "ErrorFuncNotSupport",
	-6 : "ErrorInvalidIoChannel",
	-7 : "ErrorInvalidAdRange",
	-8 : "ErrorContIoNotAllowed",
	-9 : "ErrorDiffRangeNotSupport",
	-10 : "ErrorLastChannelNotZero",
	-11 : "ErrorChannelNotDescending",
	-12 : "ErrorChannelNotAscending",
	-13 : "ErrorOpenDriverFailed",
	-14 : "ErrorOpenEventFailed",
	-15 : "ErrorTransferCountTooLarge",
	-16 : "ErrorNotDoubleBufferMode",
	-17 : "ErrorInvalidSampleRate",
	-18 : "ErrorInvalidCounterMode",
	-19 : "ErrorInvalidCounter",
	-20 : "ErrorInvalidCounterState",
	-21 : "ErrorInvalidBinBcdParam",
	-22 : "ErrorBadCardType",
	-23 : "ErrorInvalidDaRefVoltage",
	-24 : "ErrorAdTimeOut",
	-25 : "ErrorNoAsyncAI",
	-26 : "ErrorNoAsyncAO",
	-27 : "ErrorNoAsyncDI",
	-28 : "ErrorNoAsyncDO",
	-29 : "ErrorNotInputPort",
	-30 : "ErrorNotOutputPort",
	-31 : "ErrorInvalidDioPort",
	-32 : "ErrorInvalidDioLine",
	-33 : "ErrorContIoActive",
	-34 : "ErrorDblBufModeNotAllowed",
	-35 : "ErrorConfigFailed",
	-36 : "ErrorInvalidPortDirection",
	-37 : "ErrorBeginThreadError",
	-38 : "ErrorInvalidPortWidth",
	-39 : "ErrorInvalidCtrSource",
	-40 : "ErrorOpenFile",
	-41 : "ErrorAllocateMemory",
	-42 : "ErrorDaVoltageOutOfRange",
	-43 : "ErrorInvalidSyncMode",
	-44 : "ErrorInvalidBufferID",
	-45 : "ErrorInvalidCNTInterval",
	-46 : "ErrorReTrigModeNotAllowed",
	-47 : "ErrorResetBufferNotAllowed",
	-48 : "ErrorAnaTriggerLevel",
	-49 : "ErrorDAQEvent",
	-50 : "ErrorInvalidCounterValue",
	-51 : "ErrorOffsetCalibration",
	-52 : "ErrorGainCalibration",
	-53 : "ErrorCountOutofSDRAMSize",
	-54 : "ErrorNotStartTriggerModule",
	-55 : "ErrorInvalidRouteLine",
	-56 : "ErrorInvalidSignalCode",
	-57 : "ErrorInvalidSignalDirection",
	-58 : "ErrorTRGOSCalibration",
	-59 : "ErrorNoSDRAM",
	-60 : "ErrorIntegrationGain",
	-61 : "ErrorAcquisitionTiming",
	-62 : "ErrorIntegrationTiming",
	-70 : "ErrorInvalidTimeBase",
	-71 : "ErrorUndefinedParameter",
	-110 : "ErrorCalAddress",
	-111 : "ErrorInvalidCalBank",
	-201 : "ErrorConfigIoctl",
	-202 : "ErrorAsyncSetIoctl",
	-203 : "ErrorDBSetIoctl",
	-204 : "ErrorDBHalfReadyIoctl",
	-205 : "ErrorContOPIoctl",
	-206 : "ErrorContStatusIoctl",
	-207 : "ErrorPIOIoctl",
	-208 : "ErrorDIntSetIoctl",
	-209 : "ErrorWaitEvtIoctl",
	-210 : "ErrorOpenEvtIoctl",
	-211 : "ErrorCOSIntSetIoctl",
	-212 : "ErrorMemMapIoctl",
	-213 : "ErrorMemUMapSetIoctl",
	-214 : "ErrorCTRIoctl",
	-215 : "ErrorGetResIoctl",
	-216 : "ErrorCalIoctl",
	-217 : "ErrorPMIntSetIoctl",
	-301 : "ErrorNotSuportOldDriver"
}

#NoError = 0
#ErrorUnknownCardType = -1
#ErrorInvalidCardNumber = -2
#ErrorTooManyCardRegistered = -3
#ErrorCardNotRegistered = -4
#ErrorFuncNotSupport = -5
#ErrorInvalidIoChannel = -6
#ErrorInvalidAdRange = -7
#ErrorContIoNotAllowed = -8
#ErrorDiffRangeNotSupport = -9
#ErrorLastChannelNotZero = -10
#ErrorChannelNotDescending = -11
#ErrorChannelNotAscending = -12
#ErrorOpenDriverFailed = -13
#ErrorOpenEventFailed = -14
#ErrorTransferCountTooLarge = -15
#ErrorNotDoubleBufferMode = -16
#ErrorInvalidSampleRate = -17
#ErrorInvalidCounterMode = -18
#ErrorInvalidCounter = -19
#ErrorInvalidCounterState = -20
#ErrorInvalidBinBcdParam = -21
#ErrorBadCardType = -22
#ErrorInvalidDaRefVoltage = -23
#ErrorAdTimeOut = -24
#ErrorNoAsyncAI = -25
#ErrorNoAsyncAO = -26
#ErrorNoAsyncDI = -27
#ErrorNoAsyncDO = -28
#ErrorNotInputPort = -29
#ErrorNotOutputPort = -30
#ErrorInvalidDioPort = -31
#ErrorInvalidDioLine = -32
#ErrorContIoActive = -33
#ErrorDblBufModeNotAllowed = -34
#ErrorConfigFailed = -35
#ErrorInvalidPortDirection = -36
#ErrorBeginThreadError = -37
#ErrorInvalidPortWidth = -38
#ErrorInvalidCtrSource = -39
#ErrorOpenFile = -40
#ErrorAllocateMemory = -41
#ErrorDaVoltageOutOfRange = -42
#ErrorInvalidSyncMode = -43
#ErrorInvalidBufferID = -44
#ErrorInvalidCNTInterval  = -45
#ErrorReTrigModeNotAllowed = -46
#ErrorResetBufferNotAllowed = -47
#ErrorAnaTriggerLevel = -48
#ErrorDAQEvent = -49
#ErrorInvalidCounterValue = -50 
#ErrorOffsetCalibration = -51
#ErrorGainCalibration = -52
#ErrorCountOutofSDRAMSize = -53
#ErrorNotStartTriggerModule = -54
#ErrorInvalidRouteLine = -55
#ErrorInvalidSignalCode = -56
#ErrorInvalidSignalDirection = -57
#ErrorTRGOSCalibration = -58
#ErrorNoSDRAM = -59
#ErrorIntegrationGain = -60
#ErrorAcquisitionTiming = -61
#ErrorIntegrationTiming = -62
#ErrorInvalidTimeBase = -70
#ErrorUndefinedParameter = -71
#
## Error number for calibration API
#ErrorCalAddress = -110
#ErrorInvalidCalBank = -111
#
## Error number for driver API
#ErrorConfigIoctl = -201
#ErrorAsyncSetIoctl = -202
#ErrorDBSetIoctl = -203
#ErrorDBHalfReadyIoctl = -204
#ErrorContOPIoctl = -205
#ErrorContStatusIoctl = -206
#ErrorPIOIoctl = -207
#ErrorDIntSetIoctl = -208
#ErrorWaitEvtIoctl = -209
#ErrorOpenEvtIoctl = -210
#ErrorCOSIntSetIoctl = -211
#ErrorMemMapIoctl = -212
#ErrorMemUMapSetIoctl = -213
#ErrorCTRIoctl = -214
#ErrorGetResIoctl = -215
#ErrorCalIoctl = -216
#ErrorPMIntSetIoctl = -217
#ErrorNotSuportOldDriver = -301

TRUE = 1
FALSE = 0

# Synchronous Mode
SYNCH_OP = 1
ASYNCH_OP = 2

# AD Range
AD_B_10_V = 1
AD_B_5_V = 2
AD_B_2_5_V = 3
AD_B_1_25_V = 4
AD_B_0_625_V = 5
AD_B_0_3125_V = 6
AD_B_0_5_V = 7
AD_B_0_05_V = 8
AD_B_0_005_V = 9
AD_B_1_V = 10
AD_B_0_1_V = 11
AD_B_0_01_V = 12
AD_B_0_001_V = 13
AD_U_20_V = 14
AD_U_10_V = 15
AD_U_5_V = 16
AD_U_2_5_V = 17
AD_U_1_25_V = 18
AD_U_1_V = 19
AD_U_0_1_V = 20
AD_U_0_01_V = 21
AD_U_0_001_V = 22
AD_B_2_V  = 23
AD_B_0_25_V = 24
AD_B_0_2_V = 25
AD_U_4_V = 26
AD_U_2_V = 27
AD_U_0_5_V = 28
AD_U_0_4_V = 29

# DIO Port Direction
INPUT_PORT = 1
OUTPUT_PORT = 2

# DIO Line Direction
INPUT_LINE = 1
OUTPUT_LINE = 2

# Channel & Port
Channel_P1A = 0
Channel_P1B = 1
Channel_P1C = 2
Channel_P1CL = 3
Channel_P1CH = 4
Channel_P1AE = 10
Channel_P1BE = 11
Channel_P1CE = 12
Channel_P2A = 5
Channel_P2B = 6
Channel_P2C = 7
Channel_P2CL = 8
Channel_P2CH = 9
Channel_P2AE = 15
Channel_P2BE = 16
Channel_P2CE = 17
Channel_P3A = 10
Channel_P3B = 11
Channel_P3C = 12
Channel_P3CL = 13
Channel_P3CH = 14
Channel_P4A = 15
Channel_P4B = 16
Channel_P4C = 17
Channel_P4CL = 18
Channel_P4CH = 19
Channel_P5A = 20
Channel_P5B = 21
Channel_P5C = 22
Channel_P5CL = 23
Channel_P5CH = 24
Channel_P6A = 25
Channel_P6B = 26
Channel_P6C = 27
Channel_P6CL = 28
Channel_P6CH = 29

# -------- Constants for DAQ2000 --------------------
All_Channels = -1
BufferNotUsed = -1

# Constants for Analog trigger
# define analog trigger condition constants
Below_Low_level = 0x0000
Above_High_Level = 0x0100
Inside_Region = 0x0200
High_Hysteresis = 0x0300
Low_Hysteresis = 0x0400

# define analog trigger Dedicated Channel */
CH0ATRIG = 0x00
CH1ATRIG = 0x02
CH2ATRIG = 0x04
CH3ATRIG = 0x06
EXTATRIG = 0x01
ADCATRIG = 0x00 # used for DAQ-2205/2206

# Time Base
DAQ2K_IntTimeBase = 0x00
DAQ2K_ExtTimeBase = 0x01
DAQ2K_SSITimeBase = 0x02
DAQ2K_ExtTimeBase_AFI0 = 0x3
DAQ2K_ExtTimeBase_AFI1 = 0x4
DAQ2K_ExtTimeBase_AFI2 = 0x5
DAQ2K_ExtTimeBase_AFI3 = 0x6
DAQ2K_ExtTimeBase_AFI4 = 0x7
DAQ2K_ExtTimeBase_AFI5 = 0x8
DAQ2K_ExtTimeBase_AFI6 = 0x9
DAQ2K_ExtTimeBase_AFI7 = 0xa
DAQ2K_PXI_CLK = 0xc
DAQ2K_StarTimeBase = 0xd
DAQ2K_SMBTimeBase = 0xe

# Constants for AD
DAQ2K_AI_ADSTARTSRC_Int = 0x00
DAQ2K_AI_ADSTARTSRC_AFI0 = 0x10
DAQ2K_AI_ADSTARTSRC_SSI = 0x20
DAQ2K_AI_ADCONVSRC_Int = 0x00
DAQ2K_AI_ADCONVSRC_AFI0 = 0x04
DAQ2K_AI_ADCONVSRC_SSI = 0x08
DAQ2K_AI_ADCONVSRC_AFI1 = 0x0C
DAQ2K_AI_ADCONVSRC_AFI2 = 0x100
DAQ2K_AI_ADCONVSRC_AFI3 = DAQ2K_AI_ADCONVSRC_AFI2 + 0x100
DAQ2K_AI_ADCONVSRC_AFI4 = DAQ2K_AI_ADCONVSRC_AFI2 + 0x200
DAQ2K_AI_ADCONVSRC_AFI5 = DAQ2K_AI_ADCONVSRC_AFI2 + 0x300
DAQ2K_AI_ADCONVSRC_AFI6 = DAQ2K_AI_ADCONVSRC_AFI2 + 0x400
DAQ2K_AI_ADCONVSRC_AFI7 = DAQ2K_AI_ADCONVSRC_AFI2 + 0x500
DAQ2K_AI_ADCONVSRC_PFI0 = DAQ2K_AI_ADCONVSRC_AFI0

# AI Delay Counter SRC: only available for DAQ-250X
DAQ2K_AI_DTSRC_Int = 0x00
DAQ2K_AI_DTSRC_AFI1 = 0x10
DAQ2K_AI_DTSRC_GPTC0 = 0x20
DAQ2K_AI_DTSRC_GPTC1 = 0x30
DAQ2K_AI_TRGSRC_SOFT = 0x00
DAQ2K_AI_TRGSRC_ANA = 0x01
DAQ2K_AI_TRGSRC_ExtD = 0x02
DAQ2K_AI_TRSRC_SSI = 0x03
DAQ2K_AI_TRGMOD_POST = 0x00 # Post Trigger Mode
DAQ2K_AI_TRGMOD_DELAY = 0x08 # Delay Trigger Mode
DAQ2K_AI_TRGMOD_PRE = 0x10 # Pre-Trigger Mode
DAQ2K_AI_TRGMOD_MIDL = 0x18 # Middle Trigger Mode
DAQ2K_AI_ReTrigEn = 0x80
DAQ2K_AI_Dly1InSamples = 0x100
DAQ2K_AI_Dly1InTimebase = 0x000
DAQ2K_AI_MCounterEn = 0x400
DAQ2K_AI_TrgPositive = 0x0000
DAQ2K_AI_TrgNegative = 0x1000
DAQ2K_AI_TRGSRC_AFI0 = 0x10000
DAQ2K_AI_TRGSRC_AFI1 = DAQ2K_AI_TRGSRC_AFI0 + 0x10000
DAQ2K_AI_TRGSRC_AFI2 = DAQ2K_AI_TRGSRC_AFI0 + 0x20000
DAQ2K_AI_TRGSRC_AFI3 = DAQ2K_AI_TRGSRC_AFI0 + 0x30000
DAQ2K_AI_TRGSRC_AFI4 = DAQ2K_AI_TRGSRC_AFI0 + 0x40000
DAQ2K_AI_TRGSRC_AFI5 = DAQ2K_AI_TRGSRC_AFI0 + 0x50000
DAQ2K_AI_TRGSRC_AFI6 = DAQ2K_AI_TRGSRC_AFI0 + 0x60000
DAQ2K_AI_TRGSRC_AFI7 = DAQ2K_AI_TRGSRC_AFI0 + 0x70000
DAQ2K_AI_TRGSRC_PXIStar = DAQ2K_AI_TRGSRC_AFI0 + 0x90000
DAQ2K_AI_TRGSRC_SMB = DAQ2K_AI_TRGSRC_AFI0 + 0xa0000

# AI Reference ground
AI_RSE = 0x0000
AI_DIFF = 0x0100
AI_NRSE = 0x0200

# Constants for DA
# DA CH config constant
DAQ2K_DA_BiPolar = 0x1
DAQ2K_DA_UniPolar = 0x0
DAQ2K_DA_Int_REF = 0x0
DAQ2K_DA_Ext_REF = 0x1

# DA control constant
DAQ2K_DA_WRSRC_Int = 0x00
DAQ2K_DA_WRSRC_AFI1 = 0x01
DAQ2K_DA_WRSRC_SSI = 0x02
DAQ2K_DA_WRSRC_AFI0 = DAQ2K_DA_WRSRC_AFI1
DAQ2K_DA_WRSRC_PFI0 = DAQ2K_DA_WRSRC_AFI0

# DA group 
DA_Group_A = 0x00
DA_Group_B = 0x04
DA_Group_AB = 0x08

# DA TD Counter SRC: only available for DAQ-250X
DAQ2K_DA_TDSRC_Int = 0x00
DAQ2K_DA_TDSRC_AFI0 = 0x10
DAQ2K_DA_TDSRC_GPTC0 = 0x20
DAQ2K_DA_TDSRC_GPTC1 = 0x30

# DA BD Counter SRC: only available for DAQ-250X
DAQ2K_DA_BDSRC_Int = 0x00
DAQ2K_DA_BDSRC_AFI0 = 0x40
DAQ2K_DA_BDSRC_GPTC0 = 0x80
DAQ2K_DA_BDSRC_GPTC1 = 0xC0

# DA trigger constant
DAQ2K_DA_TRGSRC_SOFT = 0x00
DAQ2K_DA_TRGSRC_ANA = 0x01
DAQ2K_DA_TRGSRC_ExtD = 0x02
DAQ2K_DA_TRSRC_SSI = 0x03
DAQ2K_DA_TRGMOD_POST = 0x00
DAQ2K_DA_TRGMOD_DELAY = 0x04
DAQ2K_DA_ReTrigEn = 0x20
DAQ2K_DA_Dly1InUI = 0x40
DAQ2K_DA_Dly1InTimebase = 0x00
DAQ2K_DA_Dly2InUI = 0x80
DAQ2K_DA_Dly2InTimebase = 0x00
DAQ2K_DA_DLY2En = 0x100
DAQ2K_DA_TrgPositive = 0x000
DAQ2K_DA_TrgNegative = 0x200

# DA stop mode
DAQ2K_DA_TerminateImmediate = 0
DAQ2K_DA_TerminateUC = 1
DAQ2K_DA_TerminateIC = 2
DAQ2K_DA_TerminateFIFORC = DAQ2K_DA_TerminateIC

# DA stop source : only available for DAQ-250X
DAQ2K_DA_STOPSRC_SOFT = 0
DAQ2K_DA_STOPSRC_AFI0 = 1
DAQ2K_DA_STOPSRC_ATrig = 2
DAQ2K_DA_STOPSRC_AFI1 = 3

# -------- Timer/Counter -----------------------------
# Counter Mode (8254)
TOGGLE_OUTPUT = 0 # Toggle output from low to high on terminal count
PROG_ONE_SHOT = 1 # Programmable one-shot
RATE_GENERATOR = 2 # Rate generator
SQ_WAVE_RATE_GENERATOR = 3 # Square wave rate generator
SOFT_TRIG = 4 # Software-triggered strobe
HARD_TRIG = 5 # Hardware-triggered strobe

# 16-bit binary or 4-decade BCD counter
BIN = 0
BCD = 1

# General Purpose Timer/Counter
# Counter Mode
SimpleGatedEventCNT  = 0x01
SinglePeriodMSR = 0x02
SinglePulseWidthMSR = 0x03
SingleGatedPulseGen = 0x04
SingleTrigPulseGen = 0x05
RetrigSinglePulseGen = 0x06
SingleTrigContPulseGen = 0x07
ContGatedPulseGen = 0x08

# GPTC clock source
GPTC_GATESRC_EXT = 0x04
GPTC_GATESRC_INT = 0x00
GPTC_CLKSRC_EXT = 0x08
GPTC_CLKSRC_INT = 0x00
GPTC_UPDOWN_SEL_EXT = 0x10
GPTC_UPDOWN_SEL_INT = 0x00

# GPTC clock polarity
GPTC_CLKEN_LACTIVE = 0x01
GPTC_CLKEN_HACTIVE = 0x00
GPTC_GATE_LACTIVE = 0x02
GPTC_GATE_HACTIVE = 0x00
GPTC_UPDOWN_LACTIVE = 0x04
GPTC_UPDOWN_HACTIVE = 0x00
GPTC_OUTPUT_LACTIVE = 0x08
GPTC_OUTPUT_HACTIVE = 0x00
GPTC_INT_LACTIVE = 0x10
GPTC_INT_HACTIVE = 0x00

# GPTC paramID
GPTC_IntGATE = 0x00
GPTC_IntUpDnCTR = 0x01
GPTC_IntENABLE  = 0x02

# SSI signal code
SSI_TIME = 1
SSI_CONV = 2
SSI_WR = 4
SSI_ADSTART = 8
SSI_ADTRIG = 0x20 
SSI_DATRIG = 0x40

# signal code for GPTC
GPTC_CLK_0 = 0x100
GPTC_GATE_0 = 0x200 
GPTC_OUT_0 = 0x300
GPTC_CLK_1 = 0x400
GPTC_GATE_1 = 0x500
GPTC_OUT_1 = 0x600

# signal code for clockoutToSMB source
PXI_CLK_10_M = 0x1000
CLK_20_M  = 0x2000

# signal code for external SMB clk 
SMB_CLK_IN = 0x3000

# signal route lines
PXI_TRIG_0 = 0
PXI_TRIG_1 = 1
PXI_TRIG_2 = 2
PXI_TRIG_3 = 3
PXI_TRIG_4 = 4
PXI_TRIG_5 = 5
PXI_TRIG_6 = 6
PXI_TRIG_7 = 7
PXI_STAR_TRIG = 8
TRG_IO = 9
SMB_CLK_OUT  = 10
AFI0 = 0x10
AFI1  = 0x11
AFI2  = 0x12
AFI3 = 0x13
AFI4 = 0x14
AFI5 = 0x15
AFI6 = 0x16
AFI7 = 0x17
PXI_CLK = 0x18

# export signal plarity
Signal_ActiveHigh = 0x0
Signal_ActiveLow = 0x1

# DAQ Event type for the event message
DAQEnd = 0
DBEvent = 1
TrigEvent = 2
DAQEnd_A = 0
DAQEnd_B = 2
DAQEnd_AB = 3
DATrigEvent = 4
DATrigEvent_A = 4
DATrigEvent_B = 5
DATrigEvent_AB = 6

# Not_Reset_Code 
DIONotRest = 0x01

#
# PCIS-DASK Function prototype
#
dll.D2K_Register_Card.restype = I16
dll.D2K_Register_Card.argtypes = (U16,U16,)
dll.D2K_Release_Card.restype = I16
dll.D2K_Release_Card.argtypes = (U16,)
dll.D2K_AIO_Config.restype = I16
dll.D2K_AIO_Config.argtypes = (U16,U16,U16,U16,U16,)
dll.D2K_Register_Card_By_PXISlot_GA.restype = I16
dll.D2K_Register_Card_By_PXISlot_GA.argtypes = (U16,U16,)
dll.D2K_GetPXISlotGeographAddr.restype = I16
dll.D2K_GetPXISlotGeographAddr.argtypes = (U16,POINTER(U8),)
dll.D2K_SoftTrigGen.restype = I16
dll.D2K_SoftTrigGen.argtypes = (U16,U8,)
dll.D2K_GetFPGAVersion.restype = I16
dll.D2K_GetFPGAVersion.argtypes = (U16,POINTER(U32),)
dll.D2K_GetSerialNumber.restype = I16
dll.D2K_GetSerialNumber.argtypes = (U16,POINTER(U8),U8,POINTER(U8),)
dll.D2K_AI_Config.restype = I16
dll.D2K_AI_Config.argtypes = (U16,U16,U32,U32,U16,U16,BOOLEAN,)
dll.D2K_AI_ConfigEx.restype = I16
dll.D2K_AI_ConfigEx.argtypes = (U16,U16,U32,U32,U32,U32,BOOLEAN,)
dll.D2K_AI_PostTrig_Config.restype = I16
dll.D2K_AI_PostTrig_Config.argtypes = (U16,U16,U32,U16,U16,BOOLEAN,)
dll.D2K_AI_PostTrig_ConfigEx.restype = I16
dll.D2K_AI_PostTrig_ConfigEx.argtypes = (U16,U16,U32,U16,U32,BOOLEAN,)
dll.D2K_AI_DelayTrig_Config.restype = I16
dll.D2K_AI_DelayTrig_Config.argtypes = (U16,U16,U32,U32,U16,U16,BOOLEAN,)
dll.D2K_AI_DelayTrig_ConfigEx.restype = I16
dll.D2K_AI_DelayTrig_ConfigEx.argtypes = (U16,U16,U32,U32,U16,U32,BOOLEAN,)
dll.D2K_AI_PreTrig_Config.restype = I16
dll.D2K_AI_PreTrig_Config.argtypes = (U16,U16,U32,U16,U16,BOOLEAN,)
dll.D2K_AI_PreTrig_ConfigEx.restype = I16
dll.D2K_AI_PreTrig_ConfigEx.argtypes = (U16,U16,U32,U16,U32,BOOLEAN,)
dll.D2K_AI_MiddleTrig_Config.restype = I16
dll.D2K_AI_MiddleTrig_Config.argtypes = (U16,U16,U32,U32,U16,U16,BOOLEAN,)
dll.D2K_AI_MiddleTrig_ConfigEx.restype = I16
dll.D2K_AI_MiddleTrig_ConfigEx.argtypes = (U16,U16,U32,U32,U16,U32,BOOLEAN,)
dll.D2K_AI_CH_Config.restype = I16
dll.D2K_AI_CH_Config.argtypes = (U16,U16,U16,)
dll.D2K_AI_InitialMemoryAllocated.restype = I16
dll.D2K_AI_InitialMemoryAllocated.argtypes = (U16,POINTER(U32),)
dll.D2K_AI_ReadChannel.restype = I16
dll.D2K_AI_ReadChannel.argtypes = (U16,U16,POINTER(U16),)
dll.D2K_AI_VReadChannel.restype = I16
dll.D2K_AI_VReadChannel.argtypes = (U16,U16,POINTER(F64),)
dll.D2K_AI_SimuReadChannel.restype = I16
dll.D2K_AI_SimuReadChannel.argtypes = (U16,U16,POINTER(U16),POINTER(U16),)
dll.D2K_AI_ScanReadChannels.restype = I16
#dll.D2K_AI_ScanReadChannels.argtypes = (U16,U16,POINTER(U16),POINTER(U16),)
dll.D2K_AI_ScanReadChannels.argtypes = (U16,U16,POINTER(U16),POINTER(I16),)
dll.D2K_AI_VoltScale.restype = I16
dll.D2K_AI_VoltScale.argtypes = (U16,U16,I16,POINTER(F64),)
dll.D2K_AI_ContReadChannel.restype = I16
dll.D2K_AI_ContReadChannel.argtypes = (U16,U16,U16,U32,U32,U32,U16,)
dll.D2K_AI_ContReadMultiChannels.restype = I16
dll.D2K_AI_ContReadMultiChannels.argtypes = (U16,U16,POINTER(U16),U16,U32,U32,U32,U16,)
dll.D2K_AI_ContScanChannels.restype = I16
dll.D2K_AI_ContScanChannels.argtypes = (U16,U16,U16,U32,U32,U32,U16,)
dll.D2K_AI_ContReadChannelToFile.restype = I16
dll.D2K_AI_ContReadChannelToFile.argtypes = (U16,U16,U16,POINTER(U8),U32,U32,U32,U16,)
dll.D2K_AI_ContReadMultiChannelsToFile.restype = I16
dll.D2K_AI_ContReadMultiChannelsToFile.argtypes = (U16,U16,POINTER(U16),U16,POINTER(U8),U32,U32,U32,U16,)
dll.D2K_AI_ContScanChannelsToFile.restype = I16
dll.D2K_AI_ContScanChannelsToFile.argtypes = (U16,U16,U16,POINTER(U8),U32,U32,U32,U16,)
dll.D2K_AI_ContStatus.restype = I16
dll.D2K_AI_ContStatus.argtypes = (U16,POINTER(U16),)
dll.D2K_AI_ContVScale.restype = I16
dll.D2K_AI_ContVScale.argtypes = (U16,U16,c_void_p,POINTER(F64),I32,)
dll.D2K_AI_AsyncCheck.restype = I16
dll.D2K_AI_AsyncCheck.argtypes = (U16,POINTER(BOOLEAN),POINTER(U32),)
dll.D2K_AI_AsyncClear.restype = I16
dll.D2K_AI_AsyncClear.argtypes = (U16,POINTER(U32),POINTER(U32),)
dll.D2K_AI_AsyncClearEx.restype = I16
dll.D2K_AI_AsyncClearEx.argtypes = (U16,POINTER(U32),POINTER(U32),U32,)
dll.D2K_AI_AsyncDblBufferHalfReady.restype = I16
dll.D2K_AI_AsyncDblBufferHalfReady.argtypes = (U16,POINTER(BOOLEAN),POINTER(BOOLEAN),)
dll.D2K_AI_AsyncDblBufferMode.restype = I16
dll.D2K_AI_AsyncDblBufferMode.argtypes = (U16,BOOLEAN,)
dll.D2K_AI_AsyncDblBufferToFile.restype = I16
dll.D2K_AI_AsyncDblBufferToFile.argtypes = (U16,)
dll.D2K_AI_ContBufferSetup.restype = I16
dll.D2K_AI_ContBufferSetup.argtypes = (U16,c_void_p,U32,POINTER(U16),)
dll.D2K_AI_ContBufferReset.restype = I16
dll.D2K_AI_ContBufferReset.argtypes = (U16,)
dll.D2K_AI_MuxScanSetup.restype = I16
dll.D2K_AI_MuxScanSetup.argtypes = (U16,U16,POINTER(U16),POINTER(U16),)
dll.D2K_AI_ReadMuxScan.restype = I16
dll.D2K_AI_ReadMuxScan.argtypes = (U16,POINTER(U16),)
dll.D2K_AI_ContMuxScan.restype = I16
dll.D2K_AI_ContMuxScan.argtypes = (U16,U16,U32,U32,U32,U16,)
dll.D2K_AI_ContMuxScanToFile.restype = I16
dll.D2K_AI_ContMuxScanToFile.argtypes = (U16,U16,POINTER(U8),U32,U32,U32,U16,)
dll.D2K_AI_EventCallBack_x64.restype = I16
dll.D2K_AI_EventCallBack_x64.argtypes = (U16,I16,I16,ULONG_PTR,)
dll.D2K_AI_AsyncReTrigNextReady.restype = I16
dll.D2K_AI_AsyncReTrigNextReady.argtypes = (U16,POINTER(BOOLEAN),POINTER(BOOLEAN),POINTER(U16),)
dll.D2K_AI_AsyncReTrigNextReadyEx.restype = I16
dll.D2K_AI_AsyncReTrigNextReadyEx.argtypes = (U16,POINTER(BOOLEAN),POINTER(BOOLEAN),POINTER(U32),)
dll.D2K_AI_AsyncDblBufferHandled.restype = I16
dll.D2K_AI_AsyncDblBufferHandled.argtypes = (U16,)
dll.D2K_AI_AsyncDblBufferOverrun.restype = I16
dll.D2K_AI_AsyncDblBufferOverrun.argtypes = (U16,U16,POINTER(U16),)
dll.D2K_AI_SetTimeout.restype = I16
dll.D2K_AI_SetTimeout.argtypes = (U16,U32,)
dll.D2K_AO_CH_Config.restype = I16
dll.D2K_AO_CH_Config.argtypes = (U16,U16,U16,U16,F64,)
dll.D2K_AO_Config.restype = I16
dll.D2K_AO_Config.argtypes = (U16,U16,U16,U16,U16,U16,BOOLEAN,)
dll.D2K_AO_PostTrig_Config.restype = I16
dll.D2K_AO_PostTrig_Config.argtypes = (U16,U16,U16,U16,U16,U16,U16,BOOLEAN,)
dll.D2K_AO_DelayTrig_Config.restype = I16
dll.D2K_AO_DelayTrig_Config.argtypes = (U16,U16,U16,U16,U16,U16,U16,U16,BOOLEAN,)
dll.D2K_AO_InitialMemoryAllocated.restype = I16
dll.D2K_AO_InitialMemoryAllocated.argtypes = (U16,POINTER(U32),)
dll.D2K_AO_WriteChannel.restype = I16
dll.D2K_AO_WriteChannel.argtypes = (U16,U16,I16,)
dll.D2K_AO_VWriteChannel.restype = I16
dll.D2K_AO_VWriteChannel.argtypes = (U16,U16,F64,)
dll.D2K_AO_VoltScale.restype = I16
dll.D2K_AO_VoltScale.argtypes = (U16,U16,F64,POINTER(I16),)
dll.D2K_AO_ContWriteChannel.restype = I16
dll.D2K_AO_ContWriteChannel.argtypes = (U16,U16,U16,U32,U32,U32,U16,U16,)
dll.D2K_AO_ContWriteMultiChannels.restype = I16
dll.D2K_AO_ContWriteMultiChannels.argtypes = (U16,U16,POINTER(U16),U16,U32,U32,U32,U16,U16,)
dll.D2K_AO_AsyncCheck.restype = I16
dll.D2K_AO_AsyncCheck.argtypes = (U16,POINTER(BOOLEAN),POINTER(U32),)
dll.D2K_AO_AsyncClear.restype = I16
dll.D2K_AO_AsyncClear.argtypes = (U16,POINTER(U32),U16,)
dll.D2K_AO_AsyncClearEx.restype = I16
dll.D2K_AO_AsyncClearEx.argtypes = (U16,POINTER(U32),U16,U32,)
dll.D2K_AO_AsyncDblBufferHalfReady.restype = I16
dll.D2K_AO_AsyncDblBufferHalfReady.argtypes = (U16,POINTER(BOOLEAN),)
dll.D2K_AO_AsyncDblBufferMode.restype = I16
dll.D2K_AO_AsyncDblBufferMode.argtypes = (U16,BOOLEAN,)
dll.D2K_AO_SimuWriteChannel.restype = I16
dll.D2K_AO_SimuWriteChannel.argtypes = (U16,U16,POINTER(U16),)
dll.D2K_AO_ContBufferSetup.restype = I16
dll.D2K_AO_ContBufferSetup.argtypes = (U16,c_void_p,U32,POINTER(U16),)
dll.D2K_AO_ContBufferReset.restype = I16
dll.D2K_AO_ContBufferReset.argtypes = (U16,)
dll.D2K_AO_ContStatus.restype = I16
dll.D2K_AO_ContStatus.argtypes = (U16,POINTER(U16),)
dll.D2K_AO_ContBufferComposeAll.restype = I16
dll.D2K_AO_ContBufferComposeAll.argtypes = (U16,U16,U32,c_void_p,c_void_p,BOOLEAN,)
dll.D2K_AO_ContBufferCompose.restype = I16
dll.D2K_AO_ContBufferCompose.argtypes = (U16,U16,U16,U32,c_void_p,c_void_p,BOOLEAN,)
dll.D2K_AO_EventCallBack_x64.restype = I16
dll.D2K_AO_EventCallBack_x64.argtypes = (U16,I16,I16,ULONG_PTR,)
dll.D2K_AO_SetTimeout.restype = I16
dll.D2K_AO_SetTimeout.argtypes = (U16,U32,)
dll.D2K_AO_Group_Setup.restype = I16
dll.D2K_AO_Group_Setup.argtypes = (U16,U16,U16,POINTER(U16),)
dll.D2K_AO_Group_Update.restype = I16
dll.D2K_AO_Group_Update.argtypes = (U16,U16,POINTER(I16),)
dll.D2K_AO_Group_VUpdate.restype = I16
dll.D2K_AO_Group_VUpdate.argtypes = (U16,U16,POINTER(F64),)
dll.D2K_AO_Group_FIFOLoad.restype = I16
dll.D2K_AO_Group_FIFOLoad.argtypes = (U16,U16,U16,U32,)
dll.D2K_AO_Group_FIFOLoad_2.restype = I16
dll.D2K_AO_Group_FIFOLoad_2.argtypes = (U16,U16,U16,U32,)
dll.D2K_AO_Group_WFM_StopConfig.restype = I16
dll.D2K_AO_Group_WFM_StopConfig.argtypes = (U16,U16,U16,U16,)
dll.D2K_AO_Group_WFM_Start.restype = I16
dll.D2K_AO_Group_WFM_Start.argtypes = (U16,U16,U16,U16,U32,U32,U32,U16,)
dll.D2K_AO_Group_WFM_AsyncCheck.restype = I16
dll.D2K_AO_Group_WFM_AsyncCheck.argtypes = (U16,U16,POINTER(U8),POINTER(U32),)
dll.D2K_AO_Group_WFM_AsyncClear.restype = I16
dll.D2K_AO_Group_WFM_AsyncClear.argtypes = (U16,U16,POINTER(U32),U16,)
dll.D2K_DI_ReadLine.restype = I16
dll.D2K_DI_ReadLine.argtypes = (U16,U16,U16,POINTER(U16),)
dll.D2K_DI_ReadPort.restype = I16
dll.D2K_DI_ReadPort.argtypes = (U16,U16,POINTER(U32),)
dll.D2K_DO_WriteLine.restype = I16
dll.D2K_DO_WriteLine.argtypes = (U16,U16,U16,U16,)
dll.D2K_DO_WritePort.restype = I16
dll.D2K_DO_WritePort.argtypes = (U16,U16,U32,)
dll.D2K_DO_ReadLine.restype = I16
dll.D2K_DO_ReadLine.argtypes = (U16,U16,U16,POINTER(U16),)
dll.D2K_DO_ReadPort.restype = I16
dll.D2K_DO_ReadPort.argtypes = (U16,U16,POINTER(U32),)
dll.D2K_DIO_PortConfig.restype = I16
dll.D2K_DIO_PortConfig.argtypes = (U16,U16,U16,)
dll.D2K_DIO_LineConfig.restype = I16
dll.D2K_DIO_LineConfig.argtypes = (U16,U16,U32,U16,)
dll.D2K_DIO_LinesConfig.restype = I16
dll.D2K_DIO_LinesConfig.argtypes = (U16,U16,U32,)
dll.D2K_GCTR_Setup.restype = I16
dll.D2K_GCTR_Setup.argtypes = (U16,U16,U16,U8,U8,U16,U16,)
dll.D2K_GCTR_Control.restype = I16
dll.D2K_GCTR_Control.argtypes = (U16,U16,U16,U16,)
dll.D2K_GCTR_Reset.restype = I16
dll.D2K_GCTR_Reset.argtypes = (U16,U16,)
dll.D2K_GCTR_Read.restype = I16
dll.D2K_GCTR_Read.argtypes = (U16,U16,POINTER(U32),)
dll.D2K_GCTR_Status.restype = I16
dll.D2K_GCTR_Status.argtypes = (U16,U16,POINTER(U16),)
dll.D2K_GCTR_SetupEx.restype = I16
dll.D2K_GCTR_SetupEx.argtypes = (U16,U16,U16,U8,U8,U32,U32,)
dll.D2K_SSI_SourceConn.restype = I16
dll.D2K_SSI_SourceConn.argtypes = (U16,U16,)
dll.D2K_SSI_SourceDisConn.restype = I16
dll.D2K_SSI_SourceDisConn.argtypes = (U16,U16,)
dll.D2K_SSI_SourceClear.restype = I16
dll.D2K_SSI_SourceClear.argtypes = (U16,)
dll.D2K_Route_Signal.restype = I16
dll.D2K_Route_Signal.argtypes = (U16,U16,U16,U16,U16,)
dll.D2K_Signal_DisConn.restype = I16
dll.D2K_Signal_DisConn.argtypes = (U16,U16,U16,U16,)
dll.DAQ2205_Acquire_DA_Error.restype = I16
dll.DAQ2205_Acquire_DA_Error.argtypes = (U16,U16,U16,POINTER(F32),POINTER(F32),)
dll.DAQ2205_Acquire_AD_Error.restype = I16
dll.DAQ2205_Acquire_AD_Error.argtypes = (U16,POINTER(F32),POINTER(F32),POINTER(F32),POINTER(F32),)
dll.DAQ2206_Acquire_DA_Error.restype = I16
dll.DAQ2206_Acquire_DA_Error.argtypes = (U16,U16,U16,POINTER(F32),POINTER(F32),)
dll.DAQ2206_Acquire_AD_Error.restype = I16
dll.DAQ2206_Acquire_AD_Error.argtypes = (U16,POINTER(F32),POINTER(F32),POINTER(F32),POINTER(F32),)
dll.DAQ2213_Acquire_AD_Error.restype = I16
dll.DAQ2213_Acquire_AD_Error.argtypes = (U16,POINTER(F32),POINTER(F32),POINTER(F32),POINTER(F32),)
dll.DAQ2214_Acquire_DA_Error.restype = I16
dll.DAQ2214_Acquire_DA_Error.argtypes = (U16,U16,U16,POINTER(F32),POINTER(F32),)
dll.DAQ2214_Acquire_AD_Error.restype = I16
dll.DAQ2214_Acquire_AD_Error.argtypes = (U16,POINTER(F32),POINTER(F32),POINTER(F32),POINTER(F32),)
dll.DAQ2010_Acquire_AD_Error.restype = I16
dll.DAQ2010_Acquire_AD_Error.argtypes = (U16,U16,U16,POINTER(F32),POINTER(F32),)
dll.DAQ2010_Acquire_DA_Error.restype = I16
dll.DAQ2010_Acquire_DA_Error.argtypes = (U16,U16,U16,POINTER(F32),POINTER(F32),)
dll.DAQ2005_Acquire_AD_Error.restype = I16
dll.DAQ2005_Acquire_AD_Error.argtypes = (U16,U16,U16,POINTER(F32),POINTER(F32),)
dll.DAQ2005_Acquire_DA_Error.restype = I16
dll.DAQ2005_Acquire_DA_Error.argtypes = (U16,U16,U16,POINTER(F32),POINTER(F32),)
dll.DAQ2006_Acquire_AD_Error.restype = I16
dll.DAQ2006_Acquire_AD_Error.argtypes = (U16,U16,U16,POINTER(F32),POINTER(F32),)
dll.DAQ2006_Acquire_DA_Error.restype = I16
dll.DAQ2006_Acquire_DA_Error.argtypes = (U16,U16,U16,POINTER(F32),POINTER(F32),)
dll.DAQ2016_Acquire_AD_Error.restype = I16
dll.DAQ2016_Acquire_AD_Error.argtypes = (U16,U16,U16,POINTER(F32),POINTER(F32),)
dll.DAQ2016_Acquire_DA_Error.restype = I16
dll.DAQ2016_Acquire_DA_Error.argtypes = (U16,U16,U16,POINTER(F32),POINTER(F32),)
dll.DAQ2204_Acquire_DA_Error.restype = I16
dll.DAQ2204_Acquire_DA_Error.argtypes = (U16,U16,U16,POINTER(F32),POINTER(F32),)
dll.DAQ2204_Acquire_AD_Error.restype = I16
dll.DAQ2204_Acquire_AD_Error.argtypes = (U16,POINTER(F32),POINTER(F32),POINTER(F32),POINTER(F32),)
dll.DAQ2208_Acquire_AD_Error.restype = I16
dll.DAQ2208_Acquire_AD_Error.argtypes = (U16,POINTER(F32),POINTER(F32),POINTER(F32),POINTER(F32),)
dll.DAQ250X_Acquire_DA_Error.restype = I16
dll.DAQ250X_Acquire_DA_Error.argtypes = (I16,U16,U16,POINTER(c_float),POINTER(c_float),)
dll.DAQ250X_Acquire_AD_Error.restype = I16
dll.DAQ250X_Acquire_AD_Error.argtypes = (I16,U16,POINTER(c_float),POINTER(c_float),)
dll.D2K_DB_Auto_Calibration_ALL.restype = I16
dll.D2K_DB_Auto_Calibration_ALL.argtypes = (U16,)
dll.D2K_EEPROM_CAL_Constant_Update.restype = I16
dll.D2K_EEPROM_CAL_Constant_Update.argtypes = (U16,U16,)
dll.D2K_Load_CAL_Data.restype = I16
dll.D2K_Load_CAL_Data.argtypes = (U16,U16,)
dll.D2K_Set_Default_Load_Area.restype = I16
dll.D2K_Set_Default_Load_Area.argtypes = (U16,U16,)
dll.D2K_Get_Default_Load_Area.restype = I16
dll.D2K_Get_Default_Load_Area.argtypes = (U16,)
dll.D2K_AI_GetEvent.restype = I16
dll.D2K_AI_GetEvent.argtypes = (U16,POINTER(HANDLE),)
dll.D2K_AO_GetEvent.restype = I16
dll.D2K_AO_GetEvent.argtypes = (U16,POINTER(HANDLE),)
dll.D2K_DI_GetEvent.restype = I16
dll.D2K_DI_GetEvent.argtypes = (U16,POINTER(HANDLE),)
dll.D2K_DO_GetEvent.restype = I16
dll.D2K_DO_GetEvent.argtypes = (U16,POINTER(HANDLE),)

class DAQ2502:
    # Creation
    def __init__(self, card_number):
        da_ch = (U16*8)(0, 1, 2, 3, 4, 5, 6, 7)
        self.card = dll.D2K_Register_Card(DAQ_2502, card_number)
        if self.card < 0: raise Exception(error_code[self.card])
        else: print 'Registered card', card_number, 'as card number', self.card
        
        self.slave = None
        self.n_samples = {}
        
        #D2K_AO_CH_Config   (card, All_Channels, DAQ2K_DA_BiPolar, DAQ2K_DA_Int_REF, 10.0) # default
        dll.D2K_AO_Group_Setup(self.card, DA_Group_AB, 8, da_ch)
        dll.D2K_AO_Config(self.card, DAQ2K_DA_WRSRC_Int, DAQ2K_DA_TRGSRC_SOFT | DAQ2K_DA_TRGMOD_POST, 0, 0, 0, 0)
        #D2K_DIO_PortConfig (card, Channel_P1A, OUTPUT_PORT)
        #D2K_AI_CH_Config (card, All_Channels, AD_B_10_V | )
        #D2K_AI_Config (card, DAQ2K_AI_ADCONVSRC_Int, DAQ2K_AI_TRGSRC_SOFT | DAQ2K_AI_TRGMOD_POST, 0, 0, 1, 0)
        
    def enslave(self, slave):
        self.slave = slave    
        dll.D2K_AO_Config(slave.card, DAQ2K_DA_WRSRC_SSI, DAQ2K_DA_TRSRC_SSI | DAQ2K_DA_TRGMOD_POST, 0, 0, 0, 0)
        dll.D2K_SSI_SourceConn(self.card, SSI_WR | SSI_DATRIG)
        
    def emancipate(self):
        dll.D2K_AO_Config(self.slave.card, DAQ2K_DA_WRSRC_Int, DAQ2K_DA_TRGSRC_SOFT | DAQ2K_DA_TRGMOD_POST, 0, 0, 0, 0)
        dll.D2K_SSI_SourceClear(self.card)
        self.slave = None
    
    def release(self):
        dll.D2K_Release_Card(self.card)
        print 'Released card', self.card
    
    # Analog Output
    def write(self, digital_values):
        # AO channels are in order [0, 1, 2, 3, 4, 5, 6, 7]
        # Speed test: 512 samples in 13 ms = 40 ksps
        dll.D2K_AO_Group_Update(self.card, DA_Group_AB, digital_values.ctypes.data_as(POINTER(I16)))
    
    def write_channel(self, i, channel=0):
        dll.D2K_AO_WriteChannel(self.card, channel, i)
    
    def load(self, digital_values):
        buffer_id = U16()
        
        n_samples, n_channels = digital_values.shape
        dll.D2K_AO_ContBufferSetup(self.card, digital_values.ctypes.data_as(c_void_p), n_samples*n_channels, buffer_id)
        
        self.n_samples[buffer_id.value] = n_samples
        self.last_buffer = buffer_id.value
        return self.last_buffer
        
    def play(self, update_interval=40, buffer_id=None):
        if not buffer_id: buffer_id = self.last_buffer 
        #if self.slave: self.slave.play(update_interval)
        dll.D2K_AO_Group_WFM_Start(self.card, DA_Group_AB, buffer_id, 0, self.n_samples[buffer_id], 1, update_interval, 1)

    def wait(self):
        write_finished = BOOLEAN(0)
        write_count = U32(0)
        while write_finished.value == 0:
            dll.D2K_AO_Group_WFM_AsyncCheck(self.card, DA_Group_AB, write_finished, write_count)
            
    def stop(self):
        write_count = U32(0)
        dll.D2K_AO_Group_WFM_AsyncClear(self.card, DA_Group_AB, write_count, DAQ2K_DA_TerminateImmediate)
        print write_count.value, "samples written in total on card", self.card
            
    def clear(self):
        dll.D2K_AO_ContBufferReset(self.card)
        self.n_samples = {}
    
    def digital_write(self, bit_values, port):
        dll.D2K_DO_WritePort(self.card, port, bit_values)
    
    # Analog Input
		
    def read(self):
        # I16 D2K_AI_ScanReadChannels (U16 CardNumber, U16 NumChans, U16 *Chans, U16 *Buffer)
        ad_ch = (U16*4)(0, 1, 2, 3)
        digital_values = zeros([4], I16)
        dll.D2K_AI_ScanReadChannels (self.card, 4, ad_ch, digital_values.ctypes.data_as(POINTER(I16)))
        return digital_values