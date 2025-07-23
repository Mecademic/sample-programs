"""
This library is used to get values from the joystick in Python on a Windows machine.
It uses windmm.dll to get the values.
"""

# Imports
import ctypes
from ctypes.wintypes import WORD, UINT, DWORD
from ctypes.wintypes import WCHAR as TCHAR

# Get functions
joyGetNumDevs = ctypes.windll.winmm.joyGetNumDevs
joyGetPos = ctypes.windll.winmm.joyGetPos
joyGetPosEx = ctypes.windll.winmm.joyGetPosEx
joyGetDevCaps = ctypes.windll.winmm.joyGetDevCapsW

# Define constants
MAXPNAMELEN = 32
MAX_JOYSTICKOEMVXDNAME = 260

JOY_RETURNX = 0x1
JOY_RETURNY = 0x2
JOY_RETURNZ = 0x4
JOY_RETURNR = 0x8
JOY_RETURNU = 0x10
JOY_RETURNV = 0x20
JOY_RETURNPOV = 0x40
JOY_RETURNBUTTONS = 0x80
JOY_RETURNRAWDATA = 0x100
JOY_RETURNPOVCTS = 0x200
JOY_RETURNCENTERED = 0x400
JOY_USEDEADZONE = 0x800
JOY_RETURNALL = JOY_RETURNX | JOY_RETURNY | JOY_RETURNZ | JOY_RETURNR | JOY_RETURNU | JOY_RETURNV | JOY_RETURNPOV | JOY_RETURNBUTTONS

# Button mapping
buttons = ['Button1', 'Button2']

# Structures for WinMM
class JOYCAPS(ctypes.Structure):
    _fields_ = [
        ('wMid', WORD),
        ('wPid', WORD),
        ('szPname', TCHAR * MAXPNAMELEN),
        ('wXmin', UINT),
        ('wXmax', UINT),
        ('wYmin', UINT),
        ('wYmax', UINT),
        ('wZmin', UINT),
        ('wZmax', UINT),
        ('wNumButtons', UINT),
        ('wPeriodMin', UINT),
        ('wPeriodMax', UINT),
        ('wRmin', UINT),
        ('wRmax', UINT),
        ('wUmin', UINT),
        ('wUmax', UINT),
        ('wVmin', UINT),
        ('wVmax', UINT),
        ('wCaps', UINT),
        ('wMaxAxes', UINT),
        ('wNumAxes', UINT),
        ('wMaxButtons', UINT),
        ('szRegKey', TCHAR * MAXPNAMELEN),
        ('szOEMVxD', TCHAR * MAX_JOYSTICKOEMVXDNAME),
    ]

class JOYINFO(ctypes.Structure):
    _fields_ = [
        ('wXpos', UINT),
        ('wYpos', UINT),
        ('wZpos', UINT),
        ('wButtons', UINT),
    ]

class JOYINFOEX(ctypes.Structure):
    _fields_ = [
        ('dwSize', DWORD),
        ('dwFlags', DWORD),
        ('dwXpos', DWORD),
        ('dwYpos', DWORD),
        ('dwZpos', DWORD),
        ('dwRpos', DWORD),
        ('dwUpos', DWORD),
        ('dwVpos', DWORD),
        ('dwButtons', DWORD),
        ('dwButtonNumber', DWORD),
        ('dwPOV', DWORD),
        ('dwReserved1', DWORD),
        ('dwReserved2', DWORD),
    ]

class MecaJoy():
    def __init__(self):
        # Define structures
        self._joyid = 0
        self._info = JOYINFO()
        self._pinfo = ctypes.pointer(self._info)
        self._caps = JOYCAPS()
        self._pcaps = ctypes.pointer(self._caps)
        self._info = JOYINFO()
        self._infoex = JOYINFOEX()
        self._pinfoex = ctypes.pointer(self._infoex)
        self._infoex.dwSize = ctypes.sizeof(JOYINFOEX)
        self._infoex.dwFlags = JOY_RETURNX | JOY_RETURNY | JOY_RETURNZ | JOY_RETURNBUTTONS

    def checkdriver(self):
        num_devs = joyGetNumDevs()
        if num_devs == 0:
            print("Driver not loaded")
            return False
        return True

    def checkplugged(self):
        if joyGetPos(self._joyid, self._pinfo) != 0:
            print("Joystick not plugged in")
            return False
        return True

    def getcaps(self):
        test = joyGetDevCaps(self._joyid, self._pcaps, ctypes.sizeof(JOYCAPS))
        if test != 0:
            print("Failed to load capability")
            return False
        return True

    def getinfo(self):
        joyGetPosEx(self._joyid, self._pinfoex)
        data = [round((self._infoex.dwXpos-32767.5)/32767.5, 2), round((self._infoex.dwYpos-32767.5)/32767.5, 2), round((self._infoex.dwZpos-32767.5)/32767.5, 2), None, None]
        for b in range(self._caps.wNumButtons):
            data[b+3] = 0 != (1 << b) & self._infoex.dwButtons
        return data





















