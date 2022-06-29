from .. import tk, ttk
from . import System, Call


class Element(System, Call):
    def __init__(self, N: str = '', *args, generic=False, **kw):
        # print('Element Called! ', self.__class__.__name__)
        if not generic:
            super(System, self).__init__(N, *args, **kw)
        if N != 'PI':
            self.W = System.W[N][-1]
        else:
            self.P = self.SYS['PI'][0](*args, **kw)

    def grid(self, row=0, column=0, sticky=tk.NSEW, *args, **kw):
        self.W.grid(row=row, column=column, sticky=sticky, *args, **kw)

        def configure(weight: dict = {0: (1, 1)}):
            for i in weight:
                self.W.rowconfigure(i, weight=weight[i][0])
                self.W.columnconfigure(i, weight=weight[i][1])
            return self.W
        return configure

    def pack(self, fill=tk.BOTH, expand=1, *args, **kw):
        self.W.pack(*args, fill=fill, expand=expand, **kw)

        def configure(weight: dict = {0: (1, 1)}):
            for i in weight:
                self.W.rowconfigure(i, weight=weight[i][0])
                self.W.columnconfigure(i, weight=weight[i][1])
            return self.W
        return configure

    def image(self, x1, y1, x2, y2) -> tk.PhotoImage:
        """
        3-0 --> x = 16, y = 16        in  64x96
        0-1 --> x = 62, y = 23 or 20  in 248x23
        """
        super(System, self).__init__('PI')
        Call.SYS['PI'][-1].tk.call(Call.SYS['PI'][-1], 'copy', self.P, '-from', x1, y1, x2, y2, '-to', 0, 0)
        return Call.SYS['PI'][-1]


class Generate(System, Call):
    def __init__(self, ):
        super().__init__()
        Element('F', self.TK[1]).grid(ipady=1)()
        Element('L', F[-1], text=self.szTitle).grid(pady=1)
        Element('B', F[-1], command=self.TK[1].wm_minsize).grid(0, 3, pady=1)
        Element('B', F[-1], command=self.TK[1].wm_maxsize).grid(0, 4, pady=1)
        Element('B', F[-1], command=self.TK[1].wm_destroy).grid(0, 5, pady=1)
        self.TK[1].after(2, lambda: self.TK[1].event_generate('<<Activate>>'))


F = System.Call.W['F']
