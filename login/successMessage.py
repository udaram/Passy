from tkinter import *
from PIL import Image, ImageTk
#import Login 

def quit_prog():
    quit()
    
#global fileaddress
def Message(username):
    global screen3
    screen3 =Tk()
    screen3.geometry("700x400")
    screen3.title("Account Created Succesfully") 
    screen3.configure(background='pink')
    immg=Image.open("correct.jpeg")
    photo=ImageTk.PhotoImage(immg)
    Label(screen3,image=photo).pack()
    Label(screen3,text="Thanks",fg="brown",font="calibri 16 bold").pack()
    mess="**Dear "+str(username)+"**\n"+"You have successfuly created your Acount"
    Label(screen3,text=mess,fg="green",font="calibri 16 bold").pack(pady=3)
    Button(screen3,text="Quit",command=quit_prog,font="calibri 15 bold",bg="red",height=2,width=10).pack(pady=6)
    screen3.mainloop() 
