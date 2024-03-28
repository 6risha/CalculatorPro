import tkinter as tk


class StartFrame(tk.Frame):
    def __init__(self, window, bg_color, fg_color, accent_color):
        super().__init__(window, background=bg_color)

        self.window = window
        self.labels = {}

        self.shift = 30
        self.font = ('Courier', 24, 'bold')
        self.accent_font = ('Courier', 24, 'bold', 'underline')

        for name in window.menus:
            label = tk.Label(self, text=name, font=self.font, foreground=fg_color, background=bg_color)
            label.pack(pady=self.shift)
            label.bind('<Enter>', lambda event, lbl=label, color=accent_color: self.on_enter(event, lbl, color))
            label.bind('<Leave>', lambda event, lbl=label, color=fg_color: self.on_leave(event, lbl, color))
            label.bind('<Button-1>', lambda event, menu=name: self.open_menu(menu))
            self.labels[name] = label

    def on_enter(self, event, label, color):
        label.config(font=self.accent_font, foreground=color)

    def on_leave(self, event, label, color):
        label.config(font=self.font, foreground=color)

    def open_menu(self, menu_name):
        self.pack_forget()
        self.window.open_next(menu_name)
