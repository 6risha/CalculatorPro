import tkinter as tk
from frames.start_frame import StartFrame
from frames.calculation import CalculationFrame
from frames.equations import EquationsFrame
from frames.matrices import MatricesFrame
from frames.grapher import GrapherFrame
from frames.sequences import SequencesFrame
from frames.settings import SettingsFrame


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CalculatorPro")
        self.geometry("1000x600")

        self.bg_color = 'gray18'
        self.fg_color = 'white'
        self.accent_color = 'maroon1'
        self.configure(background=self.bg_color)

        self.menus = {'Calculation': CalculationFrame(self, self.bg_color, self.fg_color, self.accent_color),
                      'Equations': EquationsFrame(self, self.bg_color, self.fg_color, self.accent_color),
                      'Matrices': MatricesFrame(self, self.bg_color, self.fg_color, self.accent_color),
                      'Grapher': GrapherFrame(self, self.bg_color, self.fg_color, self.accent_color),
                      'Sequences': SequencesFrame(self, self.bg_color, self.fg_color, self.accent_color),
                      '...': SettingsFrame(self, self.bg_color, self.fg_color, self.accent_color)}

        self.icon = tk.PhotoImage(file="images/icon.png")
        self.iconphoto(False, self.icon)

        self.start_frame = StartFrame(self, self.bg_color, self.fg_color, self.accent_color)
        self.start_frame.pack()

    def open_next(self, next_frame):
        for menu in self.menus:
            if next_frame == menu:
                self.menus[next_frame].pack()


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
