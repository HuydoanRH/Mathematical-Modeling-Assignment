from tkinter import *
import tkinter.messagebox
import tkinter.messagebox
from Quession1_1 import qs1a
from Quession1_2 import qs1b
from Quession2 import qs2
from Quession34 import qs34

class  petrinet_Laucher:
    def __init__(self,master):
        self.master = master
        self.master.protocol("WM_DELETE_WINDOW", self.handler)
        self.app = ""
        self.windows = ""
        self.creatUI()
    def creatUI(self):
        self.bnt_qs1a = Button(self.master,width=20, padx=3, pady=3)
        self.bnt_qs1a['text'] = "Quession 1.a"
        self.bnt_qs1a['command'] = self.load_qs1a
        self.bnt_qs1a.grid(row=0, column=0, padx=2, pady=2)

        self.bnt_qs1b = Button(self.master, width=20, padx=3, pady=3)
        self.bnt_qs1b['text'] = "Quession 1.b"
        self.bnt_qs1b['command'] = self.load_qs1b
        self.bnt_qs1b.grid(row=0, column=1, padx=2, pady=2)

        self.bnt_qs2 = Button(self.master, width=20, padx=3, pady=3)
        self.bnt_qs2['text'] = "Quession 2"
        self.bnt_qs2['command'] = self.load_qs2
        self.bnt_qs2.grid(row=1, column=0, padx=2, pady=2)

        self.bnt_qs34 = Button(self.master, width=20, padx=3, pady=3)
        self.bnt_qs34['text'] = "Quession 3 and 4"
        self.bnt_qs34['command'] = self.load_qs34
        self.bnt_qs34.grid(row=1, column=1, padx=2, pady=2)

    def load_qs1a(self):
        if(self.windows ==""):
            self.windows = Tk()
        elif (self.app.isClosed == 1):
            self.windows = Tk()
        else:
            self.windows.destroy()
            self.windows = Tk()
        self.app = qs1a(self.windows)
        self.app.master.title("Quession 1.a Assignment Pertri Net")
        self.windows.mainloop()

    def load_qs1b(self):
        if(self.windows ==""):
            self.windows = Tk()
        elif (self.app.isClosed == 1):
            self.windows = Tk()
        else:
            self.windows.destroy()
            self.windows = Tk()
        self.app = qs1b(self.windows)
        self.app.master.title("Quession 1.b Assignment Pertri Net")
        self.windows.mainloop()
    def load_qs2(self):
        if(self.windows ==""):
            self.windows = Tk()
        elif (self.app.isClosed == 1):
            self.windows = Tk()
        else:
            self.windows.destroy()
            self.windows = Tk()
        self.app = qs2(self.windows)
        self.app.master.title("Quession 2 Assignment Pertri Net")
        self.windows.mainloop()

    def load_qs34(self):
        if(self.windows ==""):
            self.windows = Tk()
        elif (self.app.isClosed == 1):
            self.windows = Tk()
        else:
            self.windows.destroy()
            self.windows = Tk()
        self.app = qs34(self.windows)
        self.app.master.title("Quession 34 Assignment Pertri Net")
        self.windows.mainloop()
    def handler(self):
        if(tkinter.messagebox.askokcancel("Quit app?","Are you want to quit app?")):
            if(self.app ==""):
                if (self.app.isClosed == -1):
                    self.windows.destroy()
            self.master.destroy()

if  __name__ == '__main__':
    tk =Tk()
    app = petrinet_Laucher(tk)
    app.master.title("Pertri Net")
    tk.mainloop()