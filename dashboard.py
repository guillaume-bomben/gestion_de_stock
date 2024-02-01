import tkinter
from product import product
from category import category

class dashboard:
    def __init__(self):
        self.windows = tkinter.Tk()
        self.windows.minsize(1200,800)
        self.windows.mainloop()