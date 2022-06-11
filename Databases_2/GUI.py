from database_connector import Session, Person, pull_from_database, add_to_database, delete_from_database, update_information
from tkinter import *

main_window = Tk()

main_window.title("Employee database")

scrollbar = Scrollbar(main_window)
box = Listbox(main_window, width=100, yscrollcommand=scrollbar.set)
scrollbar.config(command=box.yview)

box.insert(END, *pull_from_database())


label_top = Label(main_window, text='Employee list')
label_name = Label(main_window, text='Name', width=20)
entry_name = Entry(main_window, width=20)
label_surname = Label(main_window, text='Surname ', width=20)
entry_surname = Entry(main_window, width=20)
label_dob = Label(main_window, text='Date of birth', width=20)
entry_dob = Entry(main_window, width=20)
label_position = Label(main_window, text='Position', width=20)
entry_position = Entry(main_window, width=20)
label_salary = Label(main_window, text='Salary', width=20)
entry_salary = Entry(main_window, width=20)

def addition():
    add_to_database(entry_name.get(), entry_surname.get(), entry_dob.get(),entry_position.get(),entry_salary.get())
    box.delete(0, 'end')
    box.insert(END, *pull_from_database())

def deletion():
    item_in_database = pull_from_database()[box.curselection()[0]]
    delete_from_database(item_in_database)
    box.delete(0, 'end')
    box.insert(END, *pull_from_database())

def change_data():
    new_window = Tk()
    new_window.title('Update information')

    item_in_database = pull_from_database()[box.curselection()[0]]

    def update():
        update_information(item_in_database, entry_name.get(), entry_surname.get(), entry_dob.get(), entry_position.get(), entry_salary.get())
        box.delete(0, 'end')
        box.insert(END, *pull_from_database())
        new_window.destroy()

    label_name = Label(new_window, text='Name', width=20)
    entry_name = Entry(new_window, width=20)
    label_surname = Label(new_window, text='Surname ', width=20)
    entry_surname = Entry(new_window, width=20)
    label_dob = Label(new_window, text='Date of birth', width=20)
    entry_dob = Entry(new_window, width=20)
    label_position = Label(new_window, text='Position', width=20)
    entry_position = Entry(new_window, width=20)
    label_salary = Label(new_window, text='Salary', width=20)
    entry_salary = Entry(new_window, width=20)
    button = Button(new_window, text="Update", command=update)

    item_in_database = pull_from_database()[box.curselection()[0]]

    entry_name.insert(0, item_in_database.first_name)
    entry_surname.insert(0, item_in_database.last_name)
    entry_dob.insert(0, item_in_database.date_of_birth)
    entry_position.insert(0, item_in_database.position)
    entry_salary.insert(0, item_in_database.salary)

    label_name.grid(row=0, column=0)
    entry_name.grid(row=0, column=1)
    label_surname.grid(row=1, column=0)
    entry_surname.grid(row=1, column=1)
    label_dob.grid(row=2, column=0)
    entry_dob.grid(row=2, column=1)
    label_position.grid(row=3, column=0)
    entry_position.grid(row=3, column=1)
    label_salary.grid(row=4, column=0)
    entry_salary.grid(row=4, column=1)
    button.grid(row=5, columnspan=2)

    new_window.mainloop()

button0 = Button(main_window, text="Add to database", command=addition)
button1 = Button(main_window, text="Delete from database", command=deletion)
button2 = Button(main_window, text="Modify data", command=change_data)

''' Visual '''
label_top.grid(row=0, column=1, columnspan=4,  sticky=W + E)

label_name.grid(row=1, column=0)
entry_name.grid(row=1, column=1)
label_surname.grid(row=2, column=0)
entry_surname.grid(row=2, column=1)
label_dob.grid(row=3, column=0)
entry_dob.grid(row=3, column=1)
label_position.grid(row=4, column=0)
entry_position.grid(row=4, column=1)
label_salary.grid(row=5, column=0)
entry_salary.grid(row=5, column=1)

button0.grid(row=6, column=0, columnspan=2)
button1.grid(row=7, column=0, columnspan=2)
button2.grid(row=8, column=0, columnspan=2)

box.grid(row=1, rowspan=8, column=3)

scrollbar.grid(row=1, rowspan=8,column=4, sticky=N+S)

main_window.mainloop()