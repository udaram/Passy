from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
from shutil import copyfile
from gesture import create_new_gesture

def quit_prog():
    quit()

#global fileaddress
def choosegesturefile(username):
    #print(username)
    screen2 =Tk()
    screen2.geometry("700x400")
    screen2.title("Choose File")
    image=Image.open("choose2.jpeg")
    photo=ImageTk.PhotoImage(image)
    Label(screen2,image=photo).pack()
    def creategesture():
        screen2.destroy()
        create_new_gesture(username)
        return
    def chfile():
        fileaddress=filedialog.askopenfilename(initialdir = "img",title = "Select file",filetypes = (("jpeg files","*.jpeg"),("all files","*.*")))
        dest="gestureImg/"+str(username)+".jpeg"
        copyfile(fileaddress,dest)
        Label(screen2,text="Image for Gusture varification selected Successfuly!!\nClick on Below button to create Gesture",bg="magenta",fg="green",font="calibri 16 bold").pack(pady=4)
        Button(screen2,text="Create Gesture Password",command=creategesture,bg="orange",fg="Blue",font="calibri 10 bold",width=40,height=3).pack(pady=3)
       
    Label(screen2,text="Choose image file for Gesture verification",bg="yellow",fg="green",font="calibri 16 bold").pack(pady=4)
    Button(screen2,text="Choose file",command=chfile,width=30,height=3,bg="pink").pack(pady=4)
    screen2.mainloop()
