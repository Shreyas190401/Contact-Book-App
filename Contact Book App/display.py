from tkinter import *
from tkinter import *
import sqlite3
from tkinter import messagebox

con = sqlite3.connect('database.db')
cur = con.cursor()

class Display(Toplevel):
    def __init__(self,person_id):
        Toplevel.__init__(self)

        self.geometry("500x700+200+100")
        self.title("Display Person")
        self.resizable(False, False)


        query = "select * from contactbook where person_id = '{}'".format(person_id)
        result = cur.execute(query).fetchone()
        print(result)
        self.person_id = person_id
        person_name = result[1]
        person_surname = result[2]
        person_mobile = result[3]
        person_dateofbirth = result[4]
        person_email = result[5]
        person_address = result[6]


        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=500, bg='#f7ff66')
        self.bottom.pack(fill=X)

        # top frame design
        self.top_image = PhotoImage(file='icons/addpeople.png')
        self.top_image_label = Label(self.top, image=self.top_image, bg='white')
        self.top_image_label.place(x=50, y=10)

        self.heading = Label(self.top, text=' Person Details', font='arial 25 bold', bg='white', fg='black')
        self.heading.place(x=210, y=50)

        # first name
        self.label_name = Label(self.bottom, text="First Name", font='arial 12 bold', fg='black', bg='#f7ff66')
        self.label_name.place(x=50, y=40)

        self.entry_name = Entry(self.bottom, width=30, bd=3)
        self.entry_name.insert(0, person_name)
        self.entry_name.config(state='disabled')
        self.entry_name.place(x=170, y=40)

        # surname
        self.label_surname = Label(self.bottom, text="Surname", font='arial 12 bold', fg='black', bg='#f7ff66')
        self.label_surname.place(x=50, y=80)

        self.entry_surname = Entry(self.bottom, width=30, bd=3)
        self.entry_surname.insert(0, person_surname)
        self.entry_surname.config(state='disabled')
        self.entry_surname.place(x=170, y=80)

        # mobile number
        self.label_mobile = Label(self.bottom, text="Mobile No.", font='arial 12 bold', fg='black', bg='#f7ff66')
        self.label_mobile.place(x=50, y=120)

        self.entry_mobile = Entry(self.bottom, width=30, bd=3)
        self.entry_mobile.insert(0, person_mobile)
        self.entry_mobile.config(state='disabled')
        self.entry_mobile.place(x=170, y=120)

        # date of birth
        self.label_dateofbirth = Label(self.bottom, text="Date of Birth", font='arial 12 bold', fg='black',
                                       bg='#f7ff66')
        self.label_dateofbirth.place(x=50, y=160)

        self.entry_dateofbirth = Entry(self.bottom, width=30, bd=3)
        self.entry_dateofbirth.insert(0, person_dateofbirth)
        self.entry_dateofbirth.config(state='disabled')
        self.entry_dateofbirth.place(x=170, y=160)

        # email
        self.label_email = Label(self.bottom, text="Email ID", font='arial 12 bold', fg='black',
                                 bg='#f7ff66')
        self.label_email.place(x=50, y=200)

        self.entry_email = Entry(self.bottom, width=30, bd=3)
        self.entry_email.insert(0, person_email)
        self.entry_email.config(state='disabled')
        self.entry_email.place(x=170, y=200)

        # address
        self.label_address = Label(self.bottom, text="Address", font='arial 12 bold', fg='black',
                                   bg='#f7ff66')
        self.label_address.place(x=50, y=240)

        self.entry_address = Text(self.bottom, width=21, height=12, bd=3)
        self.entry_address.insert(1.0, person_address)
        self.entry_address.config(state='disabled')
        self.entry_address.place(x=170, y=240)



