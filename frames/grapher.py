import tkinter as tk


class GrapherFrame(tk.Frame):
    def __init__(self, window, bg_color, fg_color, accent_color):
        super().__init__(window, background=bg_color)

        self.window = window

        self.font = ('Courier', 24, 'bold')

        self.label1 = tk.Label(self, text="Here will be the grapher...",
                               background=bg_color, foreground=fg_color, font=self.font)
        self.label1.pack()
