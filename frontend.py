from tkinter import *
from backend import Database

database = Database("books.db")

def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple = list1.get(index)
    return(selected_tuple)

def view_command():             #connecting b1
    list1.delete(0,END)
    for row in database.view():
        list1.insert(END,row)

def search_command():             #search commands
    list1.delete(0,END)
    for row in database.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,row)

def insert_command():               #insert command
    database.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))

def delete_command():
    database.delete(selected_tuple[0])  

def update_command():
    database.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())    
    

window =Tk()

window.wm_title('bookstore')

l1=Label(window,text="title")
l1.grid(row='0',column='0')

l2=Label(window,text="author")
l2.grid(row='0',column='2')

l3=Label(window,text="year")
l3.grid(row='1',column='0')
 
l4=Label(window,text="ISBN")
l4.grid(row='1',column='2')

title_text=StringVar()              #title entry
e1=Entry(window,textvariable=title_text)
e1.grid(row='0',column='1')

author_text=StringVar()               #author entry
e2=Entry(window,textvariable=author_text)
e2.grid(row='0',column='3')

year_text=StringVar()               #year entry
e3=Entry(window,textvariable=year_text)
e3.grid(row='1',column='1')

isbn_text=StringVar()              #isbn entry
e4=Entry(window,textvariable=isbn_text)
e4.grid(row='1',column='3')

list1 = Listbox(window , height='6',width='35')       #listbox 
list1.grid(row='2',column='0',columnspan='2')

sb1=Scrollbar(window)                              #scrollbox
sb1.grid(row='2',column='2',rowspan='3')
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview) 

list1.bind('<<ListboxSelect>>',get_selected_row)

#button area

b1=Button(window,text='view all',width='12',command=view_command)   #view all
b1.grid(row='2',column='3')

b1=Button(window,text='search entry',width='12',command=search_command)  #search
b1.grid(row='3',column='3')

b1=Button(window,text='add entry',width='12',command=insert_command)   #add entry
b1.grid(row='4',column='3')

b1=Button(window,text='update',width='12',command=update_command)  #update
b1.grid(row='5',column='3')

b1=Button(window,text='delete',width='12',command=delete_command)   #delete
b1.grid(row='6',column='3')

b1=Button(window,text='close',width='12',command=window.destroy)    #close
b1.grid(row='7',column='3')


window.mainloop()