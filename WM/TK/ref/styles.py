from .. import tk
from . import System, Call


P = [tk.PhotoImage, ]


class Style(System, Call.Style):
    def __init__(self, ):
        super().__init__('ST')
        self.S = {
            'TFrame': {
                'configure': {
                    'background': self.COLORS['bar'][0]
                },
                'layout': [('Frame.padding', {'sticky': 'nswe'})],
            },
            'TLabel': {
                'configure': {
                    'background': self.COLORS['bar'][0],
                    'padding': (10, 0, 10, 5),
                    'font': ('Yu Gothic UI', 10),
                    'foreground': '#ffffff',
                },
                'map': {
                    'foreground': [('!background', '#858585')]
                }
            },
            'TButton': {
                'configure': {
                    'background': self.COLORS['bar'][0],
                    'padding': (17, 9, 17, 11),
                    'anchor': 'nw'
                },
                'layout': [('Button.padding', {'children': [('Button.label', {'sticky': 'nswe'})], 'sticky': 'nswe'})],
            }
        }
        self.theme_create('WM', parent='default', settings=self.S)
        self.theme_use('WM')
        self.set_styles()
        self.set_images()

    def set_styles(self):
        self.W['L'][1]['style'] = 'title.TLabel'
        self.W['F'][1]['style'] = 'bar.TFrame'
        for i, s in enumerate(('min', 'max', 'exit'), 1):
            self.W['B'][i]['style'] = f'{s}.TButton'

    def set_images(self):
        image = P[0](file='img\\0-00-000.png')
        for i in (1, 2, 3):
            self.image((i - 1) * 12, 0, i * 12, 12, image)
            self.configure(self.W['B'][i]['style'], image=P[-1])
            self.image((i - 1) * 12, 12, i * 12, 24, image)
            self.map(self.W['B'][i]['style'], background=[
                ('active', self.COLORS['bar'][1] if i != 3 else self.COLORS['bar'][2])])
            if i != 2:
                self.map(self.W['B'][i]['style'], image=[
                    ('!alternate', 'active', P[-2]), ('!alternate', '!background', P[-1])])
            else:
                self.map(self.W['B'][i]['style'], image=[
                    ('!alternate', 'active', P[-2]), ('!alternate', '!background', P[-1]),
                    ('alternate', 'background', self.image(36, 0, 48, 12, image)),
                    ('alternate', 'active', P[-1]),
                    ('alternate', '!background', self.image(36, 12, 48, 24, image))])

    def image(self, x1, y1, x2, y2, image):
        P.append(P[0]())
        P[-1].tk.call(P[-1], 'copy', image, '-from', x1, y1, x2, y2, '-to', 0, 0)
        return P[-1]
