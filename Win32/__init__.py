"""Win32API for Python with ctypes"""
from ctypes import wintypes as wt
import ctypes as ct
import _ctypes


gdi32 = ct.WinDLL('gdi32', use_last_error=True)
user32 = ct.WinDLL('user32', use_last_error=True)
dwmapi = ct.WinDLL('dwmapi', use_last_error=True)
uxtheme = ct.WinDLL('uxtheme', use_last_error=True)
kernel32 = ct.WinDLL('kernel32', use_last_error=True)

hInst = kernel32.GetModuleHandleW(None)


class LRESULT(_ctypes._SimpleCData):
    _type_ = 'q'


user32.DefWindowProcW.argtypes = [wt.HWND, wt.UINT, wt.WPARAM, wt.LPARAM]
dwmapi.DwmDefWindowProc.argtypes = [wt.HWND, wt.UINT, wt.WPARAM, wt.LPARAM, ct.POINTER(LRESULT)]

WNDPROC = ct.WINFUNCTYPE(LRESULT, wt.HWND, wt.UINT, wt.WPARAM, wt.LPARAM)


def LOWORD(dw):
    return dw & 0xffff


def HIWORD(dw):
    return dw >> 16


def GET_X_LPARAM(lp):
    return LOWORD(lp)


def GET_Y_LPARAM(lp):
    return HIWORD(lp)


def SUCCEEDED(hr):
    return hr >= 0
