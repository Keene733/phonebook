import tkinter as tk
from tkinter import *




class PhoneBookGUI(tk.Frame):
    address_book = []


    def __init__(self):
        tk.Frame.__init__(self)


        self.list = tk.Listbox()
        self.list.grid(row=5, column=7)



        self.lb = Listbox(selectmode=SINGLE)

        # elf.scoll = Scrollbar()
        # self.scoll.grid(row = 5, column = 6)

        self.add = tk.Button(text="Add Contact", command=self.add)
        self.add.grid(row=4, column=5)

        self.delete = tk.Button(text="Delete Contact", command=self.delete)
        self.delete.grid(row=4, column=6),

        self.edit = tk.Button(text="Edit Contact",command = self.change)
        self.edit.grid(row=4, column=7)

        self.load = tk.Button(text="Load Contact", command=self.upload)
        self.load.grid(row=4, column=8)

        self.nam = tk.Label(text="Name:")
        self.nam.grid(row=6, column=4)

        self.text_name = tk.Entry()
        self.text_name.grid(row=6, column=5)

        self.numbs = tk.Label(text="Number:")
        self.numbs.grid(row=7, column=4)

        self.text_number = tk.Entry()
        self.text_number.grid(row=7, column=5)

        self.heme_lab = tk.Label(text="Email: ")
        self.heme_lab.grid(row=8, column=4)

        self.text_email = tk.Entry()
        self.text_email.grid(row=8, column=5)

        self.master.title("Address Book")


    def add(self):
        # get contact info, insert to list and append to address book
        name = self.text_name.get()
        phone = self.text_number.get()
        email = self.text_email.get()



        self.list.insert(END, name)
        self.address_book.append([name, phone, email])
        #self.address_book.sort()
        #print(self.address_book)

    def delete(self):
        # delete selection and delete from list
        U_select = self.list.curselection()

        self.list.delete(U_select)
        self.address_book.__delitem__(0)

    def select(self):
        #list selection
        print(self.list.curselection())
        return int(self.list.curselection()[0])

    def change(self):
        self.address_book[self.select()] = self.text_name.get(),self.text_number.get,self.text_email.get



    def upload(self):
        #prints out selection from address book
        U_select = self.address_book[self.select()]

        for x in range(len(U_select)):
            print(U_select[x])
















app = PhoneBookGUI()
app.mainloop()
