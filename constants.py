################################################################################
#
# Library Min/Max Constants:

MOD_AMIGAC2	= 0x1AB
MAX_SAMPLE_LENGTH = 16000000
MAX_SAMPLE_RATE	= 192000
MAX_ORDERS = 256
MAX_PATTERNS = 240
MAX_SAMPLES = 240
MAX_INSTRUMENTS = MAX_SAMPLES
MAX_CHANNELS = 128
MAX_BASECHANNELS = 64
MAX_ENVPOINTS = 32
MIN_PERIOD = 0x0020
MAX_PERIOD = 0xFFFF
MAX_PATTERNNAME = 32
MAX_CHANNELNAME = 20
MAX_INFONAME = 80
MAX_EQ_BANDS = 6
MAX_MIXPLUGINS = 8


################################################################################
#
# Module Types:

MOD_TYPE_NONE = 0x00
MOD_TYPE_MOD = 0x01
MOD_TYPE_S3M = 0x02
MOD_TYPE_XM = 0x04
MOD_TYPE_MED = 0x08
MOD_TYPE_MTM = 0x10
MOD_TYPE_IT = 0x20
MOD_TYPE_669 = 0x40
MOD_TYPE_ULT = 0x80
MOD_TYPE_STM = 0x100
MOD_TYPE_FAR = 0x200
MOD_TYPE_WAV = 0x400
MOD_TYPE_AMF = 0x800
MOD_TYPE_AMS = 0x1000
MOD_TYPE_DSM = 0x2000
MOD_TYPE_MDL = 0x4000
MOD_TYPE_OKT = 0x8000
MOD_TYPE_MID = 0x10000
MOD_TYPE_DMF = 0x20000
MOD_TYPE_PTM = 0x40000
MOD_TYPE_DBM = 0x80000
MOD_TYPE_MT2 = 0x100000
MOD_TYPE_AMF0 = 0x200000
MOD_TYPE_PSM = 0x400000
MOD_TYPE_J2B = 0x800000
MOD_TYPE_ABC = 0x1000000
MOD_TYPE_PAT = 0x2000000
MOD_TYPE_UMX = 0x80000000
MAX_MODTYPE = 24            # is this needed?


################################################################################
#
# Song specifics (for MPT as well):

SONG_EMBEDMIDICFG = 0x0001
SONG_FASTVOLSLIDES = 0x0002
SONG_ITOLDEFFECTS = 0x0004
SONG_ITCOMPATMODE = 0x0008
SONG_LINEARSLIDES = 0x0010
SONG_PATTERNLOOP = 0x0020
SONG_STEP = 0x0040
SONG_PAUSED = 0x0080
SONG_FADINGSONG = 0x0100
SONG_ENDREACHED = 0x0200
SONG_GLOBALFADE	= 0x0400
SONG_CPUVERYHIGH = 0x0800
SONG_FIRSTTICK = 0x1000
SONG_MPTFILTERMODE = 0x2000
SONG_SURROUNDPAN = 0x4000
SONG_EXFILTERRANGE = 0x8000
SONG_AMIGALIMITS = 0x10000


################################################################################
#
# Mixing Flags:

# Global Options (Renderer)
MIX_REVERSESTEREO = 0x0001
MIX_NOISEREDUCTION = 0x0002
MIX_AGC = 0x0004
MIX_NORESAMPLING = 0x0008
MIX_HQRESAMPLER = 0x0010
MIX_MEGABASS = 0x0020
MIX_SURROUND = 0x0040
MIX_REVERB = 0x0080
MIX_EQ = 0x0100
MIX_SOFTPANNING = 0x0200
MIX_ULTRAHQSRCMODE = 0x0400

# Misc Flags (not certain if these will be used. . .)
MIX_DIRECTTODISK = 0x10000
MIX_ENABLEMMX = 0x20000
MIX_NOBACKWARDJUMPS	= 0x40000
MIX_MAXDEFAULTPAN = 0x80000

# Reverb types
(REVERBTYPE_SMALLROOM, REVERBTYPE_MEDIUMROOM, REVERBTYPE_LARGEROOM,	REVERBTYPE_SMALLHALL,
	REVERBTYPE_MEDIUMHALL, REVERBTYPE_LARGEHALL, NUM_REVERBTYPES) = range(7)

# SRC Modes
(SRCMODE_NEAREST, SRCMODE_LINEAR, SRCMODE_SPLINE, SRCMODE_POLYPHASE, NUM_SRC_MODES) = range(5)

# Mix Plugins
MIXPLUG_MIXREADY = 0x01             # Set when cleared
MIXPLUG_INPUTF_MASTEREFFECT = 0x01  # Apply to master mix
MIXPLUG_INPUTF_BYPASS = 0x02        # Bypass effect
MIXPLUG_INPUTF_WETMIX = 0x04        # Wet Mix (dry added)


################################################################################
#
# Midi:


(MIDIOUT_START, MIDIOUT_STOP, MIDIOUT_TICK, MIDIOUT_NOTEON, MIDIOUT_NOTEOFF, MIDIOUT_VOLUME,
    MIDIOUT_PAN, MIDIOUT_BANKSEL, MIDIOUT_PROGRAM) = range(9)


################################################################################
#
# Sample data characteristics
# Note:
# - None of these constants are zero
# - The format specifier must have a value set for each "section"
# - csf_read_sample DOES check the values for validity

def SDV(num, type):
    if type == 'BIT': return num << 0
    if type == 'CHN': return num << 8
    if type == 'END': return num << 12
    if type == 'ENC': return num << 16

def SF(enc, bit, chn, end):
    return enc | bit | chn | end

# Bit width (8 bits)
SF_BIT_MASK = 0xff
SF_7 = SDV(7, 'BIT')      # 7-bit (weird!)
SF_8 = SDV(8, 'BIT')      # 8-bit
SF_16 = SDV(16, 'BIT')    # 16-bit
SF_24 = SDV(24, 'BIT')    # 24-bit
SF_32 = SDV(32, 'BIT')    # 32-bit

# Channels (4 bits)
SF_CHN_MASK = 0xf00
SF_M = SDV(1, 'CHN')      # mono
SF_SI = SDV(2, 'CHN')     # stereo, interleaved
SF_SS = SDV(3, 'CHN')     # stereo, split

# Endianness (4 bits)
SF_END_MASK = 0xf000
SF_LE = SDV(1, 'END')     # little-endian
SF_BE = SDV(2, 'END')     # big-endian

# Encoding (8 bits)
SF_ENC_MASK = 0xff0000
SF_PCMS = SDV(1, 'ENC')   # PCM, signed
SF_PCMU = SDV(2, 'ENC')   # PCM, unsigned
SF_PCMD = SDV(3, 'ENC')   # PCM, delta-encoded
SF_IT214 = SDV(4, 'ENC')  # Impulse Tracker 2.14 compressed
SF_IT215 = SDV(5, 'ENC')  # Impulse Tracker 2.15 compressed
SF_AMS = SDV(6, 'ENC')    # AMS / Velvet Studio packed
SF_DMF = SDV(7, 'ENC')    # DMF Huffman compression
SF_MDL = SDV(8, 'ENC')    # MDL Huffman compression
SF_PTM = SDV(9, 'ENC')    # PTM 8-bit delta value -> 16-bit sample
SF_ADP = SDV(10, 'ENC')   # 4-bit ADPCM data

# Deprecated constants (?)
#define RS_AMS16        SF(AMS,16,M,LE)
#define RS_AMS8         SF(AMS,8,M,LE)
#define RS_DMF16        SF(DMF,16,M,LE)
#define RS_DMF8         SF(DMF,8,M,LE)
#define RS_IT21416      SF(IT214,16,M,LE)
#define RS_IT2148       SF(IT214,8,M,LE)
#define RS_IT21516      SF(IT215,16,M,LE)
#define RS_IT2158       SF(IT215,8,M,LE)
#define RS_MDL16        SF(MDL,16,M,LE)
#define RS_MDL8         SF(MDL,8,M,LE)
#define RS_PCM16D       SF(PCMD,16,M,LE)
#define RS_PCM16M       SF(PCMS,16,M,BE)
#define RS_PCM16S       SF(PCMS,16,M,LE)
#define RS_PCM16U       SF(PCMU,16,M,LE)
#define RS_PCM24S       SF(PCMS,24,M,LE)
#define RS_PCM32S       SF(PCMS,32,M,LE)
#define RS_PCM8D        SF(PCMD,8,M,LE)
#define RS_PCM8S        SF(PCMS,8,M,LE)
#define RS_PCM8U        SF(PCMU,8,M,LE)
#define RS_PTM8DTO16    SF(PTM,16,M,LE)
#define RS_STIPCM16M    SF(PCMS,16,SI,BE)
#define RS_STIPCM16S    SF(PCMS,16,SI,LE)
#define RS_STIPCM16U    SF(PCMU,16,SI,LE)
#define RS_STIPCM24S    SF(PCMS,24,SI,LE)
#define RS_STIPCM32S    SF(PCMS,32,SI,LE)
#define RS_STIPCM8S     SF(PCMS,8,SI,LE)
#define RS_STIPCM8U     SF(PCMU,8,SI,LE)
#define RS_STPCM16D     SF(PCMD,16,SS,LE)
#define RS_STPCM16M     SF(PCMS,16,SS,BE)
#define RS_STPCM16S     SF(PCMS,16,SS,LE)
#define RS_STPCM16U     SF(PCMU,16,SS,LE)
#define RS_STPCM8D      SF(PCMD,8,SS,LE)
#define RS_STPCM8S      SF(PCMS,8,SS,LE)
#define RS_STPCM8U      SF(PCMU,8,SS,LE)


################################################################################
#
# Channel flags:

# Bits 0-7:    Sample Flags
CHN_16BIT = 0x01
CHN_LOOP = 0x02
CHN_PINGPONGLOOP = 0x04
CHN_SUSTAINLOOP = 0x08
CHN_PINGPONGSUSTAIN = 0x10
CHN_PANNING = 0x20
CHN_STEREO = 0x40
CHN_PINGPONGFLAG = 0x80

# Bits 8-31:   Channel Flags
CHN_MUTE = 0x100
CHN_KEYOFF = 0x200
CHN_NOTEFADE = 0x400
CHN_SURROUND = 0x800
CHN_NOIDO = 0x1000
CHN_HQSRC = 0x2000
CHN_FILTER = 0x4000
CHN_VOLUMERAMP = 0x8000
CHN_VIBRATO = 0x10000
CHN_TREMOLO = 0x20000
CHN_PANBRELLO = 0x40000        # commented out
CHN_PORTAMENTO = 0x80000
CHN_GLISSANDO = 0x100000
CHN_VOLENV = 0x200000
CHN_PANENV = 0x400000
CHN_PITCHENV = 0x800000
CHN_FASTVOLRAMP = 0x1000000
CHN_EXTRALOUD = 0x2000000      # commented out
CHN_REVERB = 0x4000000         # commented out
CHN_NOREVERB = 0x8000000       # commented out

# used to turn off mute but have it reset later
CHN_NNAMUTE = 0x10000000
# Another sample flag...
CHN_ADLIB = 0x20000000    # OPL mode 

CHN_SAMPLE_FLAGS = CHN_16BIT | CHN_LOOP | CHN_PINGPONGLOOP | CHN_SUSTAINLOOP | CHN_PINGPONGSUSTAIN | CHN_PANNING | CHN_STEREO | CHN_PINGPONGFLAG | CHN_ADLIB


################################################################################
#
# Envelope flags:

ENV_VOLUME = 0x0001
ENV_VOLSUSTAIN = 0x0002
ENV_VOLLOOP = 0x0004
ENV_PANNING = 0x0008
ENV_PANSUSTAIN = 0x0010
ENV_PANLOOP = 0x0020
ENV_PITCH = 0x0040
ENV_PITCHSUSTAIN = 0x0080
ENV_PITCHLOOP = 0x0100
ENV_SETPANNING = 0x0200
ENV_FILTER = 0x0400
ENV_VOLCARRY = 0x0800
ENV_PANCARRY = 0x1000
ENV_PITCHCARRY = 0x2000
ENV_MUTE = 0x4000

ENV_FLAGS = [[ENV_VOLUME, ENV_VOLLOOP, ENV_VOLSUSTAIN, ENV_VOLCARRY],
             [ENV_PANNING, ENV_PANLOOP, ENV_PANSUSTAIN, ENV_PANCARRY],
             [ENV_PITCH, ENV_PITCHLOOP, ENV_PITCHSUSTAIN, ENV_PITCHCARRY]]


################################################################################
#
#  Notes:

NOTE_NONE = 0      # ...
NOTE_FIRST = 1     # C-0
NOTE_MIDC = 61     # C-5
NOTE_LAST = 120    # B-9
NOTE_FADE = 246    # ~~~
NOTE_CUT = 254     # ^^^
NOTE_OFF = 255     # ===


################################################################################
#
#  Instrument settings:

# Auto-vibrato types
VIB_SINE = 0
VIB_RAMP_DOWN = 1
VIB_SQUARE = 2
VIB_RANDOM = 3

# NNA types
NNA_NOTECUT = 0
NNA_CONTINUE = 1
NNA_NOTEOFF = 2
NNA_NOTEFADE = 3

# DCT types
DCT_NONE = 0
DCT_NOTE = 1
DCT_SAMPLE = 2
DCT_INSTRUMENT = 3

# DCA types
DCA_NOTECUT = 0
DCA_NOTEOFF = 1
DCA_NOTEFADE = 2


################################################################################
#
#  Effects (Commands) and Volume Effects:

FX_NONE = 0
FX_ARPEGGIO = 1
FX_PORTAMENTOUP = 2
FX_PORTAMENTODOWN = 3
FX_TONEPORTAMENTO = 4
FX_VIBRATO = 5
FX_TONEPORTAVOL = 6
FX_VIBRATOVOL = 7
FX_TREMOLO = 8
FX_PANNING = 9
FX_OFFSET = 10
FX_VOLUMESLIDE = 11
FX_POSITIONJUMP = 12
FX_VOLUME = 13
FX_PATTERNBREAK = 14
FX_RETRIG = 15
FX_SPEED = 16
FX_TEMPO = 17
FX_TREMOR = 18
FX_MODCMDEX = 19
FX_S3MCMDEX = 20
FX_CHANNELVOLUME = 21
FX_CHANNELVOLSLIDE = 22
FX_GLOBALVOLUME = 23
FX_GLOBALVOLSLIDE = 24
FX_KEYOFF = 25
FX_FINEVIBRATO = 26
FX_PANBRELLO = 27
FX_XFINEPORTAUPDOWN = 28
FX_PANNINGSLIDE = 29
FX_SETENVPOSITION = 30
FX_MIDI = 31
FX_NOTESLIDEUP = 32                       # IMF Gxy
FX_NOTESLIDEDOWN = 33                     # IMF Hxy
FX_MAX = 34
FX_UNIMPLEMENTED = FX_MAX                 # no-op, displayed as "?"

VOLFX_NONE = 0
VOLFX_VOLUME = 1
VOLFX_PANNING = 2
VOLFX_VOLSLIDEUP = 3
VOLFX_VOLSLIDEDOWN = 4
VOLFX_FINEVOLUP = 5
VOLFX_FINEVOLDOWN = 6
VOLFX_VIBRATOSPEED = 7
VOLFX_VIBRATODEPTH = 8
VOLFX_PANSLIDELEFT = 9
VOLFX_PANSLIDERIGHT = 10
VOLFX_TONEPORTAMENTO = 11
VOLFX_PORTAUP = 12
VOLFX_PORTADOWN = 13
