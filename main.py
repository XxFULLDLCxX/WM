from Win32 import ct, wt
from Win32._sc import c, s
from TK.ref import System, Call
from TK.ref.views import Generate
from TK.ref.styles import Style
import Win32 as W
import sys


@W.WNDPROC
def WndProc(hWnd, uMsg, wParam, lParam):
    if uMsg == c.WM_CREATE:
        print("WM_CREATE")
    if uMsg == c.WM_SIZE and Call.TK:
        rc = s.RECT()
        W.user32.GetClientRect(hWnd, ct.byref(rc))
        state = {
            c.SIZE_MINIMIZED: "iconic",
            c.SIZE_MAXIMIZED: "zoomed",
            c.SIZE_RESTORED: "normal"
        }
        if wParam in state:
            Call.TK[1].state(state[wParam])
        Call.TK[1].geometry(f"{rc.right - 16}x{rc.bottom}+0+0")
        Call.TK[1].update()
    if uMsg == c.WM_NCCALCSIZE and wParam:
        pncc = s.NCCALCSIZE_PARAMS.from_address(lParam)
        pncc.rgrc[0].left += 7
        pncc.rgrc[0].top += 0
        pncc.rgrc[0].right -= 7
        pncc.rgrc[0].bottom -= 7
        return 0
    if uMsg == c.WM_GETMINMAXINFO and Call.TK:
        pmmi = s.MINMAXINFO.from_address(lParam)
        pmmi.ptMinTrackSize.x = Call.TK[0].minsize()[0]  # 334
        pmmi.ptMinTrackSize.y = Call.TK[0].minsize()[1]  # 508
        pmmi.ptMaxTrackSize.x = Call.TK[0].maxsize()[0] + 7
        pmmi.ptMaxTrackSize.y = Call.TK[0].maxsize()[1]
        return 0
    if uMsg == c.WM_ACTIVATE and Call.TK:
        margins = s.MARGINS()
        if wParam:
            margins.cyTopHeight = 1
            Call.TK[1].event_generate('<<Activate>>')
        else:
            Call.TK[1].event_generate('<<Inactivate>>')
        W.dwmapi.DwmExtendFrameIntoClientArea(hWnd, ct.byref(margins))
    if uMsg == c.WM_DESTROY:
        print("WM_DESTROY")
        W.user32.PostQuitMessage(0)
        if Call.TK:
            Call.TK[0].destroy()
        return 0

    return W.user32.DefWindowProcW(hWnd, uMsg, wParam, lParam)


class Win32(System, Call):
    def __init__(self, ):
        W.user32.LoadStringW(W.hInst, c.IDS_APP_TITLE, self.szTitle, c.MAX_LOADSTRING)
        W.user32.LoadStringW(W.hInst, 109, self.szWindowClass, c.MAX_LOADSTRING)
        self.resister_class()

    def __call__(self):
        return W.user32.CreateWindowExW(dwExStyle, self.atom, self.szTitle, dwStyle, 0, 0, 305, 510, 0, 0, W.hInst, 0)

    def view(self):
        W.user32.SetLayeredWindowAttributes(self.hWnd, 255, 255, c.LWA_ALPHA)
        uFlags = c.SWP_NOMOVE | c.SWP_NOSIZE | c.SWP_NOZORDER | c.SWP_FRAMECHANGED | c.SWP_SHOWWINDOW
        W.user32.SetWindowPos(self.hWnd, 0, 0, 0, 0, 0, uFlags)
        W.user32.ShowWindow(self.hWnd, c.SW_SHOW)
        W.user32.UpdateWindow(self.hWnd)

    def loop(self):
        msg = wt.MSG()
        hAccelTable = W.user32.LoadAcceleratorsW(W.hInst, 109)
        # Main message loop:
        while W.user32.GetMessageW(ct.byref(msg), None, 0, 0):
            if not W.user32.TranslateAcceleratorW(msg.hWnd, hAccelTable, ct.byref(msg)):
                W.user32.TranslateMessage(ct.byref(msg))
                W.user32.DispatchMessageW(ct.byref(msg))

    def resister_class(self):
        wcex = s.WNDCLASSEXW()
        wcex.cbSize = ct.sizeof(s.WNDCLASSEXW)
        wcex.style = c.CS_HREDRAW | c.CS_VREDRAW
        wcex.lpfnWndProc = WndProc
        wcex.lpszClassName = self.szWindowClass
        wcex.hInstance = W.hInst
        wcex.hIcon = W.user32.LoadImageW(W.hInst, self.Icon, c.IMAGE_ICON, 0, 0, c.LR_DEFAULTSIZE | c.LR_LOADFROMFILE)
        wcex.hCursor = W.user32.LoadCursorW(0, c.IDC_ARROW)
        # wcex.hbrBackground = W.gdi32.CreateSolidBrush(0x1F1F1F)
        self.atom = W.user32.RegisterClassExW(ct.byref(wcex))


class WM(System, Call.Toplevel):
    def __init__(self, ):
        super().__init__('TL')
        self['bg'] = "#000001"
        self.withdraw()
        self.update_idletasks()
        self.hWnd = int(self.frame(), 16)
        self.columnconfigure(0, weight=1)
        self.attributes('-transparentcolor', '#000001')

    def __call__(self, window):
        self.TK[:] = [window, self]
        self.TK[0].update_idletasks()
        self.TK[0].hWnd = int(self.TK[0].frame(), 16)
        Call.szWindowClass = Call.szTitle = self.TK[0].title()
        Call.HWND = Win32()()
        Generate()
        Style()
        Win = Control()
        Win.set_styles()
        Win.set_events()
        W.user32.SetLayeredWindowAttributes(self.HWND, 255, 255, c.LWA_ALPHA)
        return self

    def wm_size(self, event):
        size_caption = 33
        if len(B) > 1:
            if self.state() == 'zoomed':
                F[1].grid(padx=1, pady=7, ipady=1, sticky='nsew')
                self.tk.call(B[2], 'state', 'alternate')
                size_caption += 7
            if self.state() == 'normal':
                F[1].grid(padx=0, pady=0, ipady=1, sticky='nsew')
                self.tk.call(B[2], 'state', '!alternate')
        self.TK[0].geometry(f'{self.winfo_width()-16}x{self.winfo_height()-size_caption}+0+{size_caption}')

    def wm_focus(self, event):
        W.user32.SendMessageW(self.HWND, c.WM_ACTIVATE, c.WA_ACTIVE, 0)
        W.user32.SetFocus(self.TK[0].hWnd)

    def wm_resize(self, event):
        W.user32.ReleaseCapture()
        W.user32.PostMessageW(self.HWND, c.WM_NCLBUTTONDOWN, self.wm_hittest(event), 0)

    def wm_hittest(self, event):
        ptMouse = s.POINT(event.x_root, event.y_root)
        rcWindow = s.RECT()
        W.user32.GetWindowRect(self.HWND, ct.byref(rcWindow))

        uCol, uRow = 1, 1

        BORDER = 5

        if ptMouse.x - rcWindow.left < BORDER:
            uCol = 0
        elif ptMouse.x - rcWindow.left > rcWindow.right - rcWindow.left - BORDER:
            uCol = 2

        if ptMouse.y - rcWindow.top < BORDER:
            uRow = 0
        elif ptMouse.y - rcWindow.top > rcWindow.bottom - rcWindow.top - BORDER:
            uRow = 2

        cursors = [
            ['size_nw_se', 'size_ns', 'size_ne_sw'],
            ['size_we', 'arrow', 'size_we'],
            ['size_ne_sw', 'size_ns', 'size_nw-se'],
        ]
        event.widget['cursor'] = cursors[uRow][uCol]
        hittests = [
            [c.HTTOPLEFT, c.HTTOP, c.HTTOPRIGHT],
            [c.HTLEFT, c.HTCAPTION, c.HTRIGHT],
            [c.HTBOTTOMLEFT, c.HTBOTTOM, c.HTBOTTOMRIGHT],
        ]
        return hittests[uRow][uCol]

    def wm_maxsize(self, event=None):
        self.tk.call(B[2], 'state', ('!' if 'alternate' in B[2].state() else '') + 'alternate')
        if self.state() == 'zoomed':
            self.wm_restore()
        else:
            W.user32.ShowWindow(self.HWND, c.SW_MAXIMIZE)

    def wm_minsize(self, event=None):
        W.user32.ShowWindow(self.HWND, c.SW_MINIMIZE)

    def wm_restore(self, event=None):
        W.user32.ShowWindow(self.HWND, c.SW_RESTORE)

    def wm_destroy(self, event=None):
        W.user32.PostMessageW(self.HWND, c.WM_CLOSE, 0, 0)

    def wm_activate(self, event):
        """Called when the window is activated."""
        # change the state of the buttons in the bar.
        for i in range(1, len(B)):  # for each button in the bar
            self.tk.call(B[i], 'state', 'background')
        for i in range(1, len(L)):  # for each label in the bar
            self.tk.call(L[i], 'state', 'background')
        self.update_idletasks()  # necessary so that there is no delay in the update when clicking on the edges.
        #: self.update() this produces a bug when the window was inactive and was activated by pressing the bottom edge.

    def wm_inactivate(self, event):
        """Called when the window is inactivated."""
        # change the state of the buttons in the bar.
        for i in range(1, len(B)):
            self.tk.call(B[i], 'state', '!background')
        for i in range(1, len(L)):
            self.tk.call(L[i], 'state', '!background')


B = System.Call.W['B']
F = System.Call.W['F']
L = System.Call.W['L']


class TK(System, Call.Tk):
    def __init__(self, ):
        super().__init__('TK')
        self['bg'] = "LightGreen"
        self.withdraw()
        self.update_idletasks()
        self.hWnd = int(self.frame(), 16)

    def attributes(self, *args, **kw):
        for a in args[0]:
            print(a)


dwStyle = c.WS_OVERLAPPEDWINDOW | c.WS_CLIPCHILDREN | c.WS_CLIPSIBLINGS | c.WS_VISIBLE
dwExStyle = c.WS_EX_LAYERED | c.WS_EX_APPWINDOW | c.WS_EX_ACCEPTFILES | c.WS_EX_TOPMOST


class Control(System, Call):
    def __init__(self):
        super().__init__()

    def set_styles(self):
        W.user32.SetWindowLongPtrW(self.TK[1].hWnd, c.GWL_STYLE, c.WS_CHILD | c.WS_VISIBLE)
        W.user32.SetWindowLongPtrW(self.TK[0].hWnd, c.GWL_STYLE, c.WS_CHILD | c.WS_VISIBLE)
        W.user32.SetWindowLongPtrW(self.TK[1].hWnd, c.GWL_EXSTYLE, c.WS_EX_NOREDIRECTIONBITMAP)

        # One for All and All for One
        W.user32.SetParent(self.TK[1].hWnd, self.HWND)
        W.user32.SetParent(self.TK[0].hWnd, self.TK[1].hWnd)

    def set_events(self):
        # WM_SIZE
        self.TK[1].bind('<Configure>', self.TK[1].wm_size)
        self.TK[1].bind('<Motion>', self.TK[1].wm_hittest)
        self.TK[0].bind('<Button-1>', self.TK[1].wm_focus)
        L[1].bind('<Button-1>', self.TK[1].wm_resize)

        # WM_GETMINMAXINFO
        L[1].bind('<Double-Button-1>', self.TK[1].wm_maxsize)

        # WM_ACTIVATE
        self.TK[1].bind('<<Activate>>', self.TK[1].wm_activate)
        self.TK[1].bind('<<Inactivate>>', self.TK[1].wm_inactivate)


"""
if __name__ == '__main__':
    Call.TK = TK(), WM()
    Call.HWND = Win32()()
    Generate()
    Style()
    Win = Control()
    Win.set_styles()
    Win.set_events()
    Win.mainloop()
 """
if __name__ == '__main__':
    M = TK()
    C = [{}, -1]

    for argv in sys.argv[1:]:
        if '#' in argv:  # CHECK ARGV AS VALID COLORS
            C[1] += 1
            if len([i for i in argv[1:] if i <= 'f']) in (3, 6, 9):
                C[0][C[1]] = argv
            else:
                print(f'The Hex Color {C[1]} is Not Valid!')
        else:  # UPDATE TITLE BAR
            M.title(argv)
    for i, new_color in C[0].items():
        Call.COLORS['bar'][i] = new_color  # UPDATE BAR COLOR

    WM()(M)
    M.mainloop()
