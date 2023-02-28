from tkinter import *
import datetime
from mypeople import MyPeople
from addpeople import AddPeople
from aboutus import About

date = datetime.datetime.now().date()
date = str(date)

class Application(object):
    def __init__(self, master):
        self.master = master

        #frames

        self.top = Frame(master, height=150, bg='white')
        self.top.pack(fill=X)

        self.bottom = Frame(master, height=500, bg='pink')
        self.bottom.pack(fill=X)

        #top frame design
        self.top_image = PhotoImage(file='icons/contactbook.png')
        self.top_image_label = Label(self.top, image=self.top_image, bg='white')
        self.top_image_label.place(x=100, y=10)

        self.heading = Label(self.top, text='My Contact Book App',font='arial 20 bold', bg='white', fg='black')
        self.heading.place(x=230, y=50)

        self.date_lbl = Label(self.top, text="Today's date: "+date, font='arial 11 bold', fg='black', bg='white')
        self.date_lbl.place(x=460, y=120)

        #button1 - view people
        self.viewButton = Button(self.bottom, text="View People",width=12, fg='black',bg='lightgrey', font='arial 12 bold',command=self.my_people)
        self.viewButton.place(x=250, y=70)

        #button2 - add people
        self.addButton = Button(self.bottom, text="Add People",width=12, fg='black', bg='lightgrey',
                                font='arial 12 bold', command = self.addpeoplefunction)
        self.addButton.place(x=250, y=130)

        #button3 - about us
        self.aboutButton = Button(self.bottom, text="About Us",width=12, fg='black', bg='lightgrey',
                                  font='arial 12 bold', command = self.about_us)
        self.aboutButton.place(x=250, y=190)

    def my_people(self):
        people = MyPeople()

    def  about_us(self):
        aboutpage = About()

    def addpeoplefunction(self):
        addpeoplewindow = AddPeople()


def main():
    root = Tk()
    app = Application(root)
    root.title("Contact Book App")
    root.geometry("650x550+200+100")
    root.resizable(False, False)
    root.mainloop()


if __name__ == '__main__':
    main()