from tkinter import *
import random

root=Tk()
root.title("To Do List")
root.iconbitmap("to-do-list.ico")
root.configure(bg="white")
root.geometry("300x400")

#For testing purposes
tasks=[]

def update_listbox():
    #clear the current listbox
    clear_listbox()
        #display things in listbox
    for task in tasks:
        all_display.insert("end",task)

def clear_listbox():
    all_display.delete(0,"end")

def add_task():
    task=entry_widget.get()
    if task!="":
        tasks.append(task)
        update_listbox()
    else:
        lbl_display["text"]="Please enter a task first"    
    entry_widget.delete(0,"end")

def del_all():
    #Since we are deleting the list it needs to be global
    global tasks
    #Clear the tasks
    tasks=[]
    update_listbox()

def del_one():
    #Get the text of currently selected task
    #To get whatever we clicked on we use active method
    task=all_display.get("active")
    #remove the selected item
    if task in tasks:
        tasks.remove(task)
    update_listbox()

def sort_asc():
    tasks.sort()
    update_listbox()

def sort_desc():
    tasks.sort()
    tasks.reverse()
    update_listbox()    

def choose_random():
    task=random.choice(tasks)
    lbl_display["text"]=task

def total_tasks():
    total=len(tasks)
    msg="Total Tasks: %s"%total
    lbl_display["text"]=msg

#Creation of  all things to be displayed  on to do list
l1=Label(root,text="To do List",font=30 ,bg="light green",fg="black")
lbl_display=Label(root,text="",font=("Helvetica",15 ,"bold") )
entry_widget=Entry(root, text="Enter your list",borderwidth=5,border=5,width=25)
add_btn=Button(root,text="Add Task",width=15,bg="light blue",fg="black",borderwidth=10,command=add_task)
del_btn=Button(root,text="Delete All Tasks",width=15,bg="light blue",fg="black",borderwidth=10,command=del_all)
delete_btn=Button(root,text="Delete Task",width=15,bg="light blue",fg="black",borderwidth=10,command=del_one)
sortasc_btn=Button(root,text="Sort (Ascending)",width=15,bg="light blue",fg="black",borderwidth=10,command=sort_asc)
sortdesc_btn=Button(root,text="Sort (Descending)",width=15,bg="light blue",fg="black",borderwidth=10,command=sort_desc)
random_btn=Button(root,text="Choose Random",width=15,bg="light blue",fg="black",borderwidth=10,command=choose_random)
number_of_task=Button(root,text="Number of Tasks",width=15,bg="light blue",fg="black",borderwidth=10,command=total_tasks)
exit_btn=Button(root,text="Exit",bg="light blue",fg="black",borderwidth=10)
all_display=Listbox(root,height=20)

#Packing all the items
l1.grid(row=0,column=0)
lbl_display.grid(row=0,column=1)
entry_widget.grid(row=1,column=1)
add_btn.grid(row=1,column=0)
del_btn.grid(row=2,column=0)
delete_btn.grid(row=3,column=0)
sortasc_btn.grid(row=4,column=0)
sortdesc_btn.grid(row=5,column=0)
random_btn.grid(row=6,column=0)
number_of_task.grid(row=7,column=0)
exit_btn.grid(row=8,column=0)
all_display.grid(row=2,column=1,rowspan=7)

root.mainloop()