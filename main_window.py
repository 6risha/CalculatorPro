import tkinter as tk


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CalculatorPro")
        self.geometry("1000x600")
        self.bg_color = 'gray21'
        self.configure(background=self.bg_color)

        self.icon = tk.PhotoImage(file="images/icon.png")
        self.iconphoto(False, self.icon)

        self.labels = []

        # Creating and placing labels and adding them into the list
        for i, name in enumerate(['Calculation', 'Equations', 'Matrices', 'Grapher', 'Sequences', '...']):
            label = tk.Label(self, text=name, font=('Courier', 24, 'bold'))
            label.pack(pady=30)
            label.config(background=self.bg_color)
            label.bind('<Enter>', lambda event, lbl=label: self.on_enter(event, lbl))
            label.bind('<Leave>', lambda event, lbl=label: self.on_leave(event, lbl))
            label.bind('<Button-1>', lambda event, menu: self.open_menu(menu))
            self.labels.append(label)

    def on_enter(self, event, label):
        label.config(font=('Courier', 24, 'bold', 'underline'), foreground='maroon1')

    def on_leave(self, event, label):
        label.config(font=('Courier', 24, 'bold'), foreground='white')

    def open_menu(self, menu_name):
        print(f"Opening menu for {menu_name}")


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
