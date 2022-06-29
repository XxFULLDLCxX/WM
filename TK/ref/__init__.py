from .. import tk, ttk


class Call:
    """
    S = System List
    W = Widget List
    """

    Tk = tk.Tk
    Toplevel = tk.Toplevel
    Style = ttk.Style

    TK = []
    HWND = 0

    szTitle = 'WM'
    szWindowClass = 'WM'
    Icon = 'img/resize.ico'

    S = {'TK': [tk.Tk], 'SV': [tk.StringVar], 'PI': [tk.PhotoImage], 'ST': [ttk.Style], 'TL': [tk.Toplevel]}
    W = {'F': [ttk.Frame], 'L': [ttk.Label], 'B': [ttk.Button]}

    COLORS = {'bar': ['#1f1f1f', '#353535', '#e81123'], }
    KEYS = ('', 'alt & h', 'alt+Up', 'alt & i', 'ctrl+l', 'ctrl+r', 'ctrl+p', 'ctrl+q', 'ctrl+m', 'alt & m', '%',
            'Delete', 'Escape', 'BackSpace', 'r', 'q', '@', '/', '7', '8', '9', '*', '4', '5', '6', '-', '1', '2',
            '3', '+', 'F9', '0', ',', '=')

    def __init__(self, N: str = '', *args, **kw):
        """
        N = Name Key of the SYS dictionary
        """
        super().__init__()
        # print(self.__class__.__name__, 'Call', N)

        if N in ('TK', 'ST', 'TL'):
            Call.S[N].append(self)
            if N == 'ST':
                Call.Style = Call.S['ST'][-1]

        if N in ('SV', 'PI'):
            Call.S[N].append(Call.S[N][0](*args, **kw))

        if N in ('F', 'L', 'B'):
            Call.W[N].append(Call.W[N][0](*args, **kw))

        """ if N in ('Tk', 'St', 'SV'):
            print(self.S[N]) """


class System(Call):
    """SYSTEM --> CALL! Generate References__Elements DISCHARGE!"""
    Call = Call

    def __init__(self, N: str = '', *args, **kw):
        """S = System_List"""
        super().__init__(N, *args, **kw)
        print('System Called!', self.__class__.__name__)
