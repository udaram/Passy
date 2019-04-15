from tkinter import *
from PIL import Image, ImageTk

def quit_prog():
    quit()

#global fileaddress
def Message(username):
    #print(username)
    screen3 =Tk()
    screen3.geometry("700x500")
    screen3.title("Account Created Succesfully") 
    immg=Image.open("correct.jpeg")
    photo=ImageTk.PhotoImage(immg)
    Label(screen3,image=photo).pack()
    Label(screen3,text="Thanks",fg="brown",font="calibri 16 bold").pack()
    mess="**Dear "+str(username)+"**\n"+"You have successfuly created your Acount"
    Label(screen3,text=mess,fg="green",font="calibri 16 bold").pack()
    Button(screen3,text="Go back",command=quit_prog,font="calibri 15 bold",fg="red").pack()
    screen3.mainloop()
#Message("Udaram")