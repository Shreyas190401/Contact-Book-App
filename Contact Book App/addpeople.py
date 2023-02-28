from tkinter import *
import sqlite3
from tkinter import messagebox

con = sqlite3.connect('database.db')
cur = con.cursor()

class AddPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("500x650+200+100")
        self.title("Add People")
        self.resizable(False, False)

        # frames

        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=500, bg='#34baeb')
        self.bottom.pack(fill=X)

        # top frame design
        self.top_image = PhotoImage(file='icons/addpeople.png')
        self.top_image_label = Label(self.top, image=self.top_image, bg='white')
        self.top_image_label.place(x=50, y=10)

        self.heading = Label(self.top, text='Add People',font='arial 25 bold', bg='white', fg='black')
        self.heading.place(x=210, y=50)

        #first name
        self.label_name = Label(self.bottom, text="First Name", font='arial 12 bold', fg='black', bg='#34baeb')
        self.label_name.place(x=50, y=40)

        self.entry_name = Entry(self.bottom, width=30, bd=3)
        self.entry_name.insert(0, "Enter First Name")
        self.entry_name.place(x=170, y=40)


        #surname
        self.label_surname = Label(self.bottom, text="Surname", font='arial 12 bold', fg='black', bg='#34baeb')
        self.label_surname.place(x=50, y=80)

        self.entry_surname = Entry(self.bottom, width=30, bd=3)
        self.entry_surname.insert(0, "Enter Surname")
        self.entry_surname.place(x=170, y=80)

        # mobile number
        self.label_mobile = Label(self.bottom, text="Mobile No.", font='arial 12 bold', fg='black', bg='#34baeb')
        self.label_mobile.place(x=50, y=120)

        self.entry_mobile = Entry(self.bottom, width=30, bd=3)
        self.entry_mobile.insert(0, "Enter Mobile Number")
        self.entry_mobile.place(x=170, y=120)

        #date of birth
        self.label_dateofbirth = Label(self.bottom, text="Date of Birth", font='arial 12 bold', fg='black', bg='#34baeb')
        self.label_dateofbirth.place(x=50, y=160)

        self.entry_dateofbirth = Entry(self.bottom, width=30, bd=3)
        self.entry_dateofbirth.insert(0, "Enter Date of Birth")
        self.entry_dateofbirth.place(x=170, y=160)

        # email
        self.label_email = Label(self.bottom, text="Email ID", font='arial 12 bold', fg='black',
                                 bg='#34baeb')
        self.label_email.place(x=50, y=200)

        self.entry_email = Entry(self.bottom, width=30, bd=3)
        self.entry_email.insert(0, "Enter Email ID")
        self.entry_email.place(x=170, y=200)

        #address
        self.label_address = Label(self.bottom, text="Address", font='arial 12 bold', fg='black',
                                 bg='#34baeb')
        self.label_address.place(x=50, y=240)

        self.entry_address = Text(self.bottom, width=21, height=12, bd=3)
        self.entry_address.place(x=170, y=240)

        #button
        addbutton = Button(self.bottom, text="Save", width=12, font='arial 12 bold', bg='lightgrey', fg='black', command=self.add_people)
        addbutton.place(x=200, y=450)


    def add_people(self):
        name = self.entry_name.get()
        surname = self.entry_surname.get()
        mobile = self.entry_mobile.get()
        dateofbirth = self.entry_dateofbirth.get()
        email = self.entry_email.get()
        address = self.entry_address.get(1.0, 'end-1c')

        if name and surname and mobile and dateofbirth and email and address !="":
            try:
                #add to the database
                # insert into 'contactbook' (person_id, person_name, person_surname, person_mobile, person_dateofbirth,  person_email,  person_address) values()
                query ="insert into 'contactbook' (person_name, person_surname, person_mobile, person_dateofbirth, person_email, person_address) values(?,?,?,?,?,?)"
                cur.execute(query, (name, surname, mobile, dateofbirth, email, address))
                con.commit()
                messagebox.showinfo("Success","contact saved")
            except EXCEPTION as e:
                messagebox.showerror("Error",str(e))
        else:
            messagebox.showerror("Error","fill all the the fields", icon='warning')