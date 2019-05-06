from tkinter import *
from PIL import Image, ImageTk
from Movieplay import play
from photoshow import photosh
import webbrowser as wb
def course_materail():
    wb.open_new_tab('https://drive.google.com/open?id=1KUIwkdij047G9Sjuq2mWyD1h2WotizzH')
def timetable():
    wb.open_new(r'timetable.pdf')

def photos():
    photosh()
    pass
def playmovie():
    play()
    pass
def Quit():
    quit()

def account(user):
    root=Tk()
    root.geometry("800x700")
    root.title("Your Account")
    img=Image.open("welcome.jpeg")
    photo=ImageTk.PhotoImage(img)
    Label(root,image=photo).pack() 
    mess="Hello "+str(user)+"\n"+"You have Logged in into IITJammu Account"
    Label(root,text=mess,bg="pink",font="calibri 15 bold").pack(pady=5)
    Label(root,text="Choose your functions",bg="yellow",fg="green",font="calibri 15 bold").pack(pady=5)
    Button(root,text="Click to play the Movie",bg="Blue",command=playmovie,height="3",width="30").pack(pady=10)
    Button(root,text="Click to See Photo of IITJammu",command=photos,height="3",width="30").pack(pady=5)
    Button(root,text="Your Time-table",bg="Blue",command=timetable,height="3",width="30").pack(pady=10)
    Button(root,text="Your Course Material",command=course_materail,height="3",width="30").pack(pady=5)
    Button(root,text="Log Out",command=Quit,bg="red").pack(pady=5) 
    root.mainloop()
