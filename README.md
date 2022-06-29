# WM
A Window Manager for Tkinter On Windows 10

https://user-images.githubusercontent.com/73524758/175761318-5dea6c64-f1c1-410e-8abf-7adaa1b886a8.mp4

from WM import WM, TK
## How to use
>~~~python
>if __name__ == '__main__':
>    TK = TK()
>    TK.title('Default')
>    WM()(TK, loop=True)
>    # TK.mainloop()  # if loop is False
>~~~

I developed a code pattern based on the Sword Art Online (SAO) for Tkinter

###  For Example:

**`System Call Generate`** `Button` **`Element`** `<Object-ID>` _`Discharge`_ !

_Discharge_ is only a SAO reference.

[`./TK/ref/__init__.py`](./TK/ref/__init__.py)
> ~~~python
> class Call:  # Object-IDs are here.
>    Tk, ... = tk.Tk, ...
>    W = {'B': [ttk.Button, ], ...}  # W['B'][-1] for the last Button
>    def __init__(self, N: str = '', *args, *kw):
>        self.W[N].append(self.W[N][0](*args, **kw))  # N in 'F', 'L', 'B'
>
> class System(Call):  # class TK(System, Call.Tk): 
>    Call = Call  # System.Call
> ~~~

 [`./TK/ref/views.py`](./TK/ref/views.py)
> ~~~python
> class Element(System, Call):
>    def __init__(self, N: str = '', *args, generic=0, **kw):
>        super(System, self).__init__(N, *args, **kw)  # if generic == 0
>    ...
>    # Accelerators for Grid, Pack and Cut to Image
>
> class Generate(System, Call):
>    def __init__(self):
>        super(System, self).__init__()  # info when called
>        ...
>        #  Draw APP
> ~~~




