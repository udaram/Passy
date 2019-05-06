from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
from shutil import copyfile

from gesturefileaccess import choosegesturefile

def chosegesture():
        screen3.destroy()
        choosegesturefile(username)
def chfile():
    global dest
    fileaddress=filedialog.askopenfilename(initialdir = "img",title = "Select file",filetypes = (("jpeg files","*.jpeg"),("all files","*.*")))
    dest="imagesegImg/"+str(username)+".jpeg"
    copyfile(fileaddress,dest)
    Label(screen3,text="file has been selected Successfuly",bg="orange",fg="Blue",font="calibri 16 bold").pack()
    Button(screen3,text="Next",command=chosegesture,bg="violet",height=2,width=20).pack(pady=5)
 

def choosefile(user):
    global username
    username=user
    global screen3
    screen3 =Tk() 
    screen3.geometry("600x400")
    screen3.title("Choose File")
    ima=Image.open("choose.jpeg")
    im=ImageTk.PhotoImage(ima)
    Label(screen3,image=im).pack()

          
    Label(screen3,text="Choose image file for Image Segmentation verification",fg="green",bg="yellow",font="calibri 13 bold").pack(pady=2)
    Button(screen3,text="Choose File",command=chfile,width=30,height=3,bg="violet").pack(pady=5)
    screen3.mainloop()
  

#choosefile("uda")