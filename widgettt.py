'''This program is developed by awanish kumar 
This program contains the different function for different widget and doc string to 
get the proper overview of the each function'''

''' importing the tkinter '''
from tkinter import *
import tkinter as tk


''' creating the sefty function for under construction box if anything goes wrong'''


def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="This part is still in under construction")
   button.pack()

''' All the widget functions at one place '''


def canvass():
    '''canvas widget window '''
    can = tk.Tk()
    can.title('canvas window')
    canvas = tk.Canvas(can, height = 500 , width = 500)
    canvas.create_oval(10,10,100,100,fill = 'gray90')
    canvas.create_line(105,10,200,105)
    canvas.create_rectangle(205,10,300,105, outline = 'black',fill = 'gray50')
    # img = tk.PhotoImage(file ="1.png")
    # canvas.create_image(145,285,image=img)
    canvas.pack()
    can.mainloop()


def checkk():
    '''check box widget window '''
    che = tk.Tk()
    che.geometry("300x300")
    che.title('check button widget')
    tk.Checkbutton(che, text = 'english').pack()
    tk.Checkbutton(che, text = 'hindi').pack()
    tk.Checkbutton(che, text = 'maths').pack()
    tk.Checkbutton(che, text = 'physics').pack()
    tk.Checkbutton(che, text = 'python').pack()
    tk.Checkbutton(che, text = 'tkinter is cool').pack()
    che.mainloop()


def lab():
    ''' lable eidget '''
    lab = tk.Tk()
    lab.title('lable window')
    tk.Label(lab,text='In this series you will see th tkinter function ').pack()
    tk.Label(lab,text='graphic user interface is more fun ').pack()
    tk.Label(lab,text='lets try some more widget').pack()
    tk.Label(lab,text='close this window and try new widget').pack()
    lab.mainloop()


def msg():
    '''messsage widget'''
    msg =tk.Tk()
    msg.title('Message widget')
    tk.Message(msg,text = '''Introduction to Tkinter
    Graphical User Interface(GUI) is a form of user interface which allows users to
 interact with computers through visual indicators using items such as icons, menus, windows, etc.
 It has advantages over the Command Line Interface(CLI)
 where users interact with computers by writing commands using keyboard only and
  whose usage is more difficult than GUI.''').pack()
    msg.mainloop()


def rad():
    '''radio widget window'''
    rb = tk.Tk()
    rb.title('redio button widget')
    rb.geometry("250x250")
    for text , value in [('python',1),
    ('tkinter',2),
    ('GUI',3),
    ('cool',4)]:
        tk.Radiobutton(rb,text=text,value=value).pack()
    rb.mainloop()


def ent():
    en = tk.Tk()
    en.title('entry widget')
    tk.Label(en, text = 'User name').pack(side = LEFT)
    tk.Entry(en, bd = 5).pack(side = RIGHT)
    en.mainloop()


def lb():
    '''list box widget'''
    lisbx = tk.Tk()
    lisbx.title('List box widget')
    a = tk.Listbox(lisbx)
    a.insert(1 , "python")
    a.insert(2 , "rubby")
    a.insert(3 , "AWS")
    a.insert(4 , "Azure")
    a.insert(5 , "django")
    a.insert(6 , "Node js")
    a.pack()
    lisbx.mainloop()


<<<<<<< HEAD
def tol():
    '''this function tell us about the tool used in the program '''
    tl = Tk()
    tl.title('Tools i used')
    tol = Label(text = '''Tools that are use is python programing \n
    module which i used is TKinter\n
    and some basic function of Tkinter''', bg = 'black',fg = "red",
    padx = 113,pady = 98,font = "comicsansms 20 bold", borderwidth = 10, relief = RAISED)
    tol.pack(fill = X,padx = 34,pady = 34)
    tl.mainloop()


'''this function contains the source code'''
def src_code():
    sc = Tk()
    sc.title('Source code')
    scrollbar = Scrollbar(sc)
    scrollbar.pack(side = RIGHT , fill = Y)
    sorce = Message(msg,text = '''#This program is developed by awanish kumar 
#This program contains the different function for different widget and doc string to 
#get the proper overview of the each function
#importing the tkinter
from tkinter import *
import tkinter as tk
def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="This part is still in under construction")
   button.pack()
def canvass():
    can = tk.Tk()
    can.title('canvas window')
    canvas = tk.Canvas(can, height = 500 , width = 500)
    canvas.create_oval(10,10,100,100,fill = 'gray90')
    canvas.create_line(105,10,200,105)
    canvas.create_rectangle(205,10,300,105, outline = 'black',fill = 'gray50')
    # img = tk.PhotoImage(file ="1.png")
    # canvas.create_image(145,285,image=img)
    canvas.pack()
    can.mainloop()
def checkk():
    che = tk.Tk()
    che.geometry("300x300")
    che.title('check button widget')
    tk.Checkbutton(che, text = 'english').pack()
    tk.Checkbutton(che, text = 'hindi').pack()
    tk.Checkbutton(che, text = 'maths').pack()
    tk.Checkbutton(che, text = 'physics').pack()
    tk.Checkbutton(che, text = 'python').pack()
    tk.Checkbutton(che, text = 'tkinter is cool').pack()
    che.mainloop()
def lab():
    lab = tk.Tk()
    lab.title('lable window')
    tk.Label(lab,text='In this series you will see th tkinter function ').pack()
    tk.Label(lab,text='graphic user interface is more fun ').pack()
    tk.Label(lab,text='lets try some more widget').pack()
    tk.Label(lab,text='close this window and try new widget').pack()
    lab.mainloop()
def msg():
    msg =tk.Tk()
    msg.title('Message widget')
    tk.Message(msg,text = "Introduction to Tkinter
    Graphical User Interface(GUI) is a form of user interface which allows users to
 interact with computers through visual indicators using items such as icons, menus, windows, etc.
 It has advantages over the Command Line Interface(CLI)
 where users interact with computers by writing commands using keyboard only and
  whose usage is more difficult than GUI.").pack()
    msg.mainloop()
def rad():
    rb = tk.Tk()
    rb.title('redio button widget')
    rb.geometry("250x250")
    for text , value in [('python',1),
    ('tkinter',2),
    ('GUI',3),
    ('cool',4)]:
        tk.Radiobutton(rb,text=text,value=value).pack()
    rb.mainloop()
def ent():
    en = tk.Tk()
    en.title('entry widget')
    tk.Label(en, text = 'User name').pack(side = LEFT)
    tk.Entry(en, bd = 5).pack(side = RIGHT)
    en.mainloop()
def lb():
    lisbx = tk.Tk()
    lisbx.title('List box widget')
    a = tk.Listbox(lisbx)
    a.insert(1 , "python")
    a.insert(2 , "rubby")
    a.insert(3 , "AWS")
    a.insert(4 , "Azure")
    a.insert(5 , "django")
    a.insert(6 , "Node js")
    a.pack()
    lisbx.mainloop()
def tol():
    tl = Tk()
    tl.title('Tools i used')
    tol = Label(text = "Tools that are use is python programing \n
    module which i used is TKinter\n
    and some basic function of Tkinter", bg = 'black',fg = "red",
    padx = 113,pady = 98,font = "comicsansms 20 bold", borderwidth = 10, relief = RAISED)
    tol.pack(fill = X,padx = 34,pady = 34)
    tl.mainloop()
root = Tk()
root.geometry("400x400")
bdy = Label(text = "This is The main window. \n to see all the
 widget try find in Menu bar \n \n Though menu is also comes under 
the widget of tkinter \n To see the credit please do check the about
 section under the help menu", bg = 'black',fg = "yellow",
 padx = 113,pady = 98,font = "comicsansms 20 bold", borderwidth = 5, relief = SUNKEN)
bdy.pack(fill = X,padx = 34,pady = 34)
menubar = Menu(root)
widgetmenu = Menu(menubar, tearoff=0)
widgetmenu.add_command(label="Canvas widget", command=canvass)
widgetmenu.add_command(label="check box widget", command=checkk)
widgetmenu.add_command(label="label widget", command=lab)
widgetmenu.add_command(label="Message widget", command=msg)
widgetmenu.add_command(label="Radio widget", command=rad)
widgetmenu.add_command(label="Entry widget", command=ent)
widgetmenu.add_command(label="List box widget", command=lb)
widgetmenu.add_separator()
widgetmenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Widgets", menu=widgetmenu)
sourcemenu = Menu(menubar, tearoff=0)
sourcemenu.add_command(label="Source code", command=donothing)
menubar.add_cascade(label="Source", menu=sourcemenu)
infomenu = Menu(menubar, tearoff=0)
infomenu.add_command(label="tools used", command=donothing)
infomenu.add_command(label="About developer", command=donothing)
menubar.add_cascade(label="Info desk", menu=infomenu)
root.config(menu=menubar)
root.mainloop()''', font = "comicsansms 12 bold")
    sorce.pack(side = LEFT , fill = BOTH)
    sc.mainloop()


def about_dev():
    ab = Tk()
    dev = Label(text = '''This program is developed by Awanish kumar \n
    Under the guidence of Sb Dandin sir \n
    hope you all liked my work''', bg = 'black',fg = "yellow",
padx = 113,pady = 98,font = "comicsansms 20 bold", borderwidth = 5, relief = SUNKEN)
    dev.pack(fill = X,padx = 34,pady = 34)
    ab.mainloop()
    

=======
>>>>>>> 590608b9f032b45a4cb475487e51d00d66943d35
''' this part of the code contains the menu operations '''
root = Tk()
root.geometry("400x400")
bdy = Label(text = '''This is The main window. \n to see all the
 widget try find in Menu bar \n \n Though menu is also comes under 
the widget of tkinter \n To see the credit please do check the about
 section under the help menu''', bg = 'black',fg = "yellow",
padx = 113,pady = 98,font = "comicsansms 20 bold", borderwidth = 5, relief = SUNKEN)
bdy.pack(fill = X,padx = 34,pady = 34)
menubar = Menu(root)
widgetmenu = Menu(menubar, tearoff=0)
widgetmenu.add_command(label="Canvas widget", command=canvass)
widgetmenu.add_command(label="check box widget", command=checkk)
widgetmenu.add_command(label="label widget", command=lab)
widgetmenu.add_command(label="Message widget", command=msg)
widgetmenu.add_command(label="Radio widget", command=rad)
widgetmenu.add_command(label="Entry widget", command=ent)
widgetmenu.add_command(label="List box widget", command=lb)

widgetmenu.add_separator()

widgetmenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Widgets", menu=widgetmenu)


sourcemenu = Menu(menubar, tearoff=0)
<<<<<<< HEAD
sourcemenu.add_command(label="Source code", command=src_code)
=======
sourcemenu.add_command(label="Source code", command=donothing)
>>>>>>> 590608b9f032b45a4cb475487e51d00d66943d35
menubar.add_cascade(label="Source", menu=sourcemenu)


infomenu = Menu(menubar, tearoff=0)
<<<<<<< HEAD
infomenu.add_command(label="tools used", command=tol)
infomenu.add_command(label="About developer", command=about_dev)
=======
infomenu.add_command(label="tools used", command=donothing)
infomenu.add_command(label="About developer", command=donothing)
>>>>>>> 590608b9f032b45a4cb475487e51d00d66943d35
menubar.add_cascade(label="Info desk", menu=infomenu)

root.config(menu=menubar)
root.mainloop()