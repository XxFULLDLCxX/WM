"""Structures for Win32API"""
from . import ct, wt, WNDPROC


class POINT(ct.Structure):
    _fields_ = [
        ('x', wt.LONG),
        ('y', wt.LONG),
    ]


class RECT(ct.Structure):
    _fields_ = [
        ('left', wt.LONG),
        ('top', wt.LONG),
        ('right', wt.LONG),
        ('bottom', wt.LONG),
    ]


class MARGINS(ct.Structure):
    _fields_ = [
        ('cxLeftWidth', wt.INT),
        ('cxRightWidth', wt.INT),
        ('cyTopHeight', wt.INT),
        ('cyBottomHeight', wt.INT),
    ]


class MSG(ct.Structure):
    _fields_ = [("hwnd", wt.HWND),
                ("message", wt.UINT),
                ("wParam", wt.WPARAM),
                ("lParam", wt.LPARAM),
                ("time", wt.DWORD),
                ("pt", POINT)]


class WNDCLASSEXW(ct.Structure):
    _fields_ = [
        ('cbSize', wt.UINT),
        ('style', wt.UINT),
        ('lpfnWndProc', WNDPROC),
        ('cbClsExtra', wt.INT),
        ('cbWndExtra', wt.INT),
        ('hInstance', wt.HINSTANCE),
        ('hIcon', wt.HICON),
        ('hCursor', wt.HICON),
        ('hbrBackground', wt.HBRUSH),
        ('lpszMenuName', wt.LPCWSTR),
        ('lpszClassName', wt.LPCWSTR),
        ('hIconSm', wt.HICON),
    ]


class PAINTSTRUCT(ct.Structure):
    _fields_ = [
        ('hdc', wt.HDC),
        ('fErase', wt.BOOL),
        ('rcPaint', wt.RECT),
        ('fRestore', wt.BOOL),
        ('fIncUpdate', wt.BOOL),
        ('rgbReserved', wt.BYTE * 32),
    ]


class NCCALCSIZE_PARAMS(ct.Structure):
    _fields_ = [
        ('rgrc', RECT * 3),
        ('lppos', POINT),
    ]


class MINMAXINFO(ct.Structure):
    _fields_ = [
        ('ptReserved', POINT),
        ('ptMaxSize', POINT),
        ('ptMaxPosition', POINT),
        ('ptMinTrackSize', POINT),
        ('ptMaxTrackSize', POINT),
    ]


class BITMAP(ct.Structure):
    _fields_ = [
        ('bmType', wt.DWORD),
        ('bmWidth', wt.LONG),
        ('bmHeight', wt.LONG),
        ('bmWidthBytes', wt.DWORD),
        ('bmPlanes', wt.WORD),
        ('bmBitsPixel', wt.WORD),
        ('bmBits', wt.LPVOID),
    ]


class BITMAPFILEHEADER(ct.Structure):
    _fields_ = [
        ('bfType', wt.WORD),
        ('bfSize', wt.DWORD),
        ('bfReserved1', wt.WORD),
        ('bfReserved2', wt.WORD),
        ('bfOffBits', wt.DWORD),
    ]


class BITMAPINFOHEADER(ct.Structure):
    _fields_ = [
        ('biSize', wt.DWORD),
        ('biWidth', wt.LONG),
        ('biHeight', wt.LONG),
        ('biPlanes', wt.WORD),
        ('biBitCount', wt.WORD),
        ('biCompression', wt.DWORD),
        ('biSizeImage', wt.DWORD),
        ('biXPelsPerMeter', wt.LONG),
        ('biYPelsPerMeter', wt.LONG),
        ('biClrUsed', wt.DWORD),
        ('biClrImportant', wt.DWORD),
    ]