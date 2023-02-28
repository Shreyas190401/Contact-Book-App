from tkinter import *
import sqlite3
from addpeople import AddPeople
from updateperson import Update
from display import Display
from tkinter import messagebox

con = sqlite3.connect('database.db')
cur = con.cursor()


class MyPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("650x600+200+100")
        self.title("View People")
        self.resizable(False, False)

        # frames

        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=500, bg='#32e3b7')
        self.bottom.pack(fill=X)

        # top frame design
        self.top_image = PhotoImage(file='icons/viewpeople.png')
        self.top_image_label = Label(self.top, image=self.top_image, bg='white')
        self.top_image_label.place(x=150, y=10)

        self.heading = Label(self.top, text='View People',
                             font='arial 25 bold', bg='white', fg='black')
        self.heading.place(x=310, y=50)

        self.scroll = Scrollbar(self.bottom, orient=VERTICAL)

        self.listbox = Listbox(self.bottom, width=50, height=27)
        self.listbox.grid(row=0, column=0, padx=(40, 0))
        self.scroll.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scroll.set)

        persons = cur.execute("select * from 'contactbook'").fetchall()
        print(persons)
        count = 0
        for person in persons:
            self.listbox.insert(count, str(person[0])+ ". " +person[1] +" "+person[2])
            count += 1

        self.scroll.grid(row=0, column=1, sticky=N+S)

        #buttons

        btnadd = Button(self.bottom, text="Add", width=12, font='arial 12 bold', bg='lightgrey', fg='black', command=self.add_people)
        btnadd.grid(row=0, column=2, padx=70, pady=50, sticky=N)

        btnupdate = Button(self.bottom, text="Update", width=12, font='arial 12 bold', bg='lightgrey', fg='black',
                           command=self.update_function)
        btnupdate.grid(row=0, column=2, padx=70, pady=100, sticky=N)

        btndisplay = Button(self.bottom, text="Display", width=12, font='arial 12 bold', bg='lightgrey', fg='black',
                            command=self.display_person)
        btndisplay.grid(row=0, column=2, padx=70, pady=150, sticky=N)

        btndelete = Button(self.bottom, text="Delete", width=12, font='arial 12 bold', bg='lightgrey', fg='black',
                           command=self.delete_person)
        btndelete.grid(row=0, column=2, padx=70, pady=200, sticky=N)

    def delete_person(self):
        selected_item = self.listbox.curselection()
        person = self.listbox.get(selected_item)
        person_id = person.split(".")[0]

        query = "delete from contactbook where person_id = {}".format(person_id)
        answer = messagebox.askquestion("Warning", "Are you sure you want to delete?")
        if answer == 'yes':
            try:
                cur.execute(query)
                con.commit()
                messagebox.showinfo("Success","Deleted")
                self.destroy()
            except EXCEPTION as e:
                messagebox.showinfo("Info", str(e))

    def add_people(self):
        add_page = AddPeople()
        self.destroy()

    def update_function(self):
        selected_item = self.listbox.curselection()
        person = self.listbox.get(selected_item)
        person_id = person.split(".")[0]

        updatepage = Update(person_id)

    def display_person(self):
        selected_item = self.listbox.curselection()
        person = self.listbox.get(selected_item)
        person_id = person.split(".")[0]

        displaypage = Display(person_id)
