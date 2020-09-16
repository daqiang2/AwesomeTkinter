#!/usr/bin/env python
"""
    AwesomeTkinter, a new tkinter widgets design using custom styles and images

    :copyright: (c) 2020 by Mahmoud Elshahat.

"""

import tkinter as tk

from .button import Button3d
from .frame import Frame3d, ScrollableFrame
from .menu import RightClickMenu
from .progressbar import RadialProgressbar, RadialProgressbar3d
from .scrollbar import SimpleScrollbar
from .text import ScrolledText
from .utils import *
from .config import *


def main():
    
    root = tk.Tk()
    root.config(background=DEFAULT_COLOR)

    f1 = Frame3d(root)
    f1.pack(side='left', expand=True, fill='both', padx=3, pady=3)

    bar = RadialProgressbar3d(f1, fg='cyan', size=120)
    bar.pack(padx=20, pady=20)
    bar.start()

    Button3d(f1, text='3D Button').pack(pady=10)

    f2 = Frame3d(root)
    f2.pack(side='left', expand=True, fill='both', padx=3, pady=3)

    bar = RadialProgressbar(f2, fg='green')
    bar.pack(padx=30, pady=30)
    bar.start()

    btn = Button3d(f2, text='Pressed Button')
    btn.pack(pady=10)

    root.mainloop()















 