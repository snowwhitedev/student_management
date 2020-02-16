from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image
import DATABASE
from PIL import Image, ImageTk
import os

errror = ""

'''Event when clicking Add New Button --- for Inserting new record into DataBase''' 
def addNew():
    id = stuID_field.get()
    fname = stufName_field.get()
    lname = stulName_field.get()
    mark = stuMark_field.get()
    active = stuActive_field.get()
    imageloc = stuimageLoc_field.get()
    
    if not fname:
        msg["text"] = "First Name must be Entered!"
        return 0
    if not lname:
        msg["text"] = "Last Name must be Entered!"
        return 0
    if active is None:
        active = 1
    DATABASE.Add(fname,lname,mark,active,imageloc)
 
'''Event when clicking Clear all button --- for Clearing Student's panel''' 
def clearStu(event):
    stuID_field.delete(0,END)
    stufName_field.delete(0,END)
    stulName_field.delete(0,END)
    stuMark_field.delete(0,END)
    stuActive_field.delete(0,END)
    stuimageLoc_field.delete(0,END)
    stuFrame.bind('<Double-Button-1>', clearStu)

'''Event when cliking View All Button --- for viewing all records '''
def viewALL():
    records = DATABASE.View()
    clearTree()
    for row in records:
        tv.insert("", 0, values=row)

'''Event when clicking Delete Button ---for Deleting  selected record '''
def delete():
    ID = stuID_field.get()
    DATABASE.Delete(ID)
    msg["text"] = ""
    msg["text"] = "deleted!"
    stuID_field.delete(0,END)
    stufName_field.delete(0,END)
    stulName_field.delete(0,END)
    stuMark_field.delete(0,END)
    stuActive_field.delete(0,END)
    stuimageLoc_field.delete(0,END)
   
'''Event when clicking Update Button --- for Updating Selected Record '''
def update():
    id = stuID_field.get()
    fname = stufName_field.get()
    lname = stulName_field.get()
    mark = stuMark_field.get()
    active = stuActive_field.get()
    imageloc = stuimageLoc_field.get()
    if active is None:
        active = 1
    if not fname or not lname:
        print("hello")
    DATABASE.Update(id, fname,lname,mark,active,imageloc)
    msg["text"] = "updated!"
   
'''Event when clicking Search Button --- for Searching Records ---key : id or First_Name'''
def search():
    msg["text"] = ""
    id = stuID_field.get()
    fname = stufName_field.get()
    records = DATABASE.Search(id, fname)
    
    clearTree()
    for row in records:
        tv.insert("", 0, values=row)
    
    msg["text"] = "Search activated!"
 
'''Function for Inserting records to the Tree'''
def insertTree():
    for row in list:
        tv.insert("", 0, values=row)
        #tv.insert('',END,values=row)

'''For Clearing Tree'''
def clearTree():
    x = tv.get_children()
    print("Tree :", x) #debug code
    for item in x:
        tv.delete(item)
 
'''Event when Selecting Tree Item...''' 
def select_item(event):
    row = tv.item(tv.selection())
    print("row",type(row),row)
    item = tv.selection()[0]
    print ('item clicked ', item)
    stuID_field.delete(0,END)
    stufName_field.delete(0,END)
    stulName_field.delete(0,END)
    stuMark_field.delete(0,END)
    stuActive_field.delete(0,END)
    stuimageLoc_field.delete(0,END)
    
    stuID_field.insert(0, tv.item(item)['values'][0])
    stufName_field.insert(0,tv.item(item)['values'][1])
    stulName_field.insert(0, tv.item(item)['values'][2])
    stuMark_field.insert(0, tv.item(item)['values'][3])
    stuActive_field.insert(0, tv.item(item)['values'][4])
    stuimageLoc_field.insert(0, tv.item(item)['values'][5])
    image_load(tv.item(item)['values'][5])

'''Fucntion for Loading image'''
def image_load(loc):
        if not os.path.isfile(loc):
                loc = "img/Avatar.jpg" 
        img_load = Image.open(loc)
        render = ImageTk.PhotoImage(img_load)
        img = Label(win, image = render)
        img.image = render
        img.place(x = 235, y = 20, width = 180, height = 195)  
 
win = Tk()
win.title("Student Record")
win.geometry("800x500")
win.configure(background='Orange1')
 
#Student frame
stuFrame = LabelFrame(win, text='Student panel')
stuFrame.configure(background='LightBlue2')
stuFrame.grid(row=0, column=0, sticky=NSEW, padx=8, pady=8)
 
#Student ID
stuID = Label(stuFrame, text='StuID: ')
stuID.grid(row=0, column=0)
stuID_text = StringVar()
stuID_field = Entry(stuFrame, textvariable=stuID_text)
stuID_field.grid(row=0, column=1)
 
#Student first Name
stufName = Label(stuFrame, text='Stu First Name:').grid(row=1, column=0, pady=2)
stufName_text = StringVar()
stufName_field = Entry(stuFrame, textvariable=stufName)
stufName_field.grid(row=1, column=1,  padx=8, pady=8)


 
#student last Name
stulName = Label(stuFrame, text='Stu Last Name:').grid(row=2, column=0, pady=2)
stulName_text = StringVar()
stulName_field = Entry(stuFrame, textvariable=stulName)
stulName_field.grid(row=2, column=1,  padx=8, pady=8)
 
#Student Mark
stuMark = Label(stuFrame, text='Stu Mark:').grid(row=3, column=0,  pady=2)
stuMark_num = IntVar()
stuMark_field = Entry(stuFrame, textvariable=stuMark_num)
stuMark_num.set('')
stuMark_field.grid(row=3, column=1, padx=5, pady=2)
 
#Student Active
stuActive = Label(stuFrame, text='Stu Active').grid(row=4, column=0, pady=2)
stuActive_num = IntVar()
stuActive_field = Entry(stuFrame, textvariable=stuActive_num)
stuActive_num.set('')
stuActive_field.grid(row=4, column=1, padx=5, pady=2)
 
# Student's image location field
stuimageLoc = Label(stuFrame, text='Stu Image Loc:').grid(row=5, column=0, pady=2)
stuimageLoc_text = StringVar()
stuimageLoc_field = Entry(stuFrame, textvariable=stuimageLoc_text)
stuimageLoc_field.grid(row=5, column=1, padx=5, pady=2 )
 
# Student's photo placeholder
photoLabel = Label(stuFrame, text='Stu Photo')
photoLabel.grid(row=0, column=3)
 
label = Label(stuFrame, text='Place holder\n for a photo\n of student')
label.grid(row=3, column=3,columnspan=3,sticky=N)

image_load("img/Avatar.jpg")


dispFrame = LabelFrame(win, text='Display panel:')
dispFrame.configure(background='Green')
dispFrame.grid(row=1, column=0, sticky=N, padx=8, pady=8)
 
tv = ttk.Treeview(dispFrame, height=10, columns=5)
tv.grid(row=1, column=1, columnspan=6)
tv["columns"] = ["Stu ID", "Stu First Name", "Stu Last Name", "Mark", "Active", "Image Loc"]
tv["show"] = "headings"
tv.heading("Stu ID", text="Stu ID")
tv.column("Stu ID", anchor='center', width=70)
 
tv.heading("Stu First Name", text="Stu First Name")
tv.column("Stu First Name", anchor='center', width=100)
 
tv.heading("Stu Last Name", text="Stu Last Name")
tv.column("Stu Last Name", anchor='center', width=100)
 
tv.heading("Mark", text="Mark")
tv.column("Mark", anchor='center', width=100)
 
tv.heading("Active", text="Active")
tv.column("Active", anchor='center', width=70)
 
tv.heading("Image Loc", text="Image Loc")
tv.column("Image Loc", anchor='center', width=100)
 
tv.bind('<ButtonRelease-1>', select_item)
tv.bind('<Double-Button-1>', select_item)
sb1 = Scrollbar(dispFrame, command=tv.yview, orient=VERTICAL)
sb1.grid(row=0, column=7, rowspan=2, sticky='ns')
tv.configure(yscrollcommand=sb1.set)
 
 
tv.bind('<ButtonRelease-1>', select_item)
tv.bind('<Return>', select_item)
 
btnFrame = LabelFrame(win,text= 'Action panel:')
btnFrame.configure(background='Red')
btnFrame.grid(row=0, column=3, sticky=E,padx=8,pady=8)
 
b1=Button(btnFrame,text="View all ",width=12, command=viewALL)
b1.grid(row=0, column=0,padx=8,pady=8)
 
b2=Button(btnFrame,text="Add new ",width=12, command=addNew)
b2.grid(row=2, column=0)
 
b3=Button(btnFrame,text="Delete ",width=12, command=delete)
b3.grid(row=3, column=0)
 
b4=Button(btnFrame,text="Update ",width=12, command=update)
b4.grid(row=4, column=0)
 
b5=Button(btnFrame,text="Search ",width=12, command=search)
b5.grid(row=5, column=0)
 
b6=Button(btnFrame,text="Clear All ",width=12, command=clearTree)
b6.grid(row=0, column=2)
 
b7=Button(btnFrame,text="Exit ",width=12, command=win.destroy)
b7.grid(row=2, column=2)
 
addBtns = Label(btnFrame, text='Space reserved\nfor new buttons\nto be added later: ')
addBtns.grid(row=3,rowspan=3, column=2)
 
msgFrame = LabelFrame(win, text='Message panel:')
msgFrame.configure(background='Pink')
msgFrame.grid(row=1, column=3, sticky=NSEW, padx=8, pady=8)
msg = Label(msgFrame, text='Msg Display to alert \nwhat button is activated\nand any other info', fg='red')
msg.grid(row=0, column=0, padx=8, pady=8)
 
win.mainloop()