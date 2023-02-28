from tkinter import *

class About(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("550x550+200+100")
        self.title("About Us")
        self.resizable(False, False)

        self.top = Frame(self, height=550, width=550, bg='#9b85ff')
        self.top.pack(fill=BOTH)

        self.text = Label(self.top, text='Hey This is about us page'
                          '\n\n With the help of this application you can'
                          '\n add ,update ,display various details of your '
                         '\n contact number and you can also delete them',
                          font = 'arial 14 bold', bg="#9b85ff", fg = "white"
                          )

        self.text.place(x=50, y=50)