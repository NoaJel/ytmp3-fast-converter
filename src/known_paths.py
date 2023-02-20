import ctypes
from ctypes import windll, wintypes


class GUID(ctypes.Structure):
    _fields_ = [
        ("Data1", wintypes.DWORD),
        ("Data2", wintypes.WORD),
        ("Data3", wintypes.WORD),
        ("Data4", wintypes.BYTE * 8)
    ]

    def __init__(self, uuid_):
        ctypes.Structure.__init__(self)
        self.Data1, self.Data2, self.Data3, self.Data4[0], self.Data4[1], rest = uuid_.fields
        for i in range(2, 8):
            self.Data4[i] = rest >> (8 - i - 1) * 8 & 0xff


class UserHandle:
    current = wintypes.HANDLE(0)
    common = wintypes.HANDLE(-1)


_CoTaskMemFree = windll.ole32.CoTaskMemFree
_CoTaskMemFree.restype = None
_CoTaskMemFree.argtypes = [ctypes.c_void_p]

_SHGetKnownFolderPath = windll.shell32.SHGetKnownFolderPath
_SHGetKnownFolderPath.argtypes = [
    ctypes.POINTER(GUID), wintypes.DWORD, wintypes.HANDLE, ctypes.POINTER(
        ctypes.c_wchar_p)
]


class PathNotFoundException(Exception):
    pass


def getPathFromFolder(folder_uuid, user_handle=UserHandle.current):
    fid = GUID(folder_uuid)
    pPath = ctypes.c_wchar_p()
    S_OK = 0

    if _SHGetKnownFolderPath(ctypes.byref(fid), 0, user_handle, ctypes.byref(pPath)) != S_OK:
        raise PathNotFoundException()

    path = pPath.value
    _CoTaskMemFree(pPath)

    return path
