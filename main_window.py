import tkinter as tk


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CalculatorPro")
        self.geometry("800x600")

        self.img = tk.PhotoImage(file="images/icon.png")
        self.iconphoto(False, self.img)

        self.label_1 = tk.Label(self, image=self.img)
        self.label_1.pack()


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
