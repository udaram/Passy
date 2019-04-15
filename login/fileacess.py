from tkinter import *
from tkinter import filedialog
from shutil import copyfile

from gesturefileaccess import choosegesturefile

def choosefile(username):
    screen2 =Tk()
    screen2.geometry("600x200")
    screen2.title("Choose file")
    def chosegesture():
        choosegesturefile(username)
    def chfile():
        global dest
        fileaddress=filedialog.askopenfilename(initialdir = "/home/udaram/PythonGUI/login/img",title = "Select file",filetypes = (("jpeg files","*.jpeg"),("all files","*.*")))
        dest="/home/udaram/PythonGUI/login/imagesegImg/"+str(username)+".jpeg"
        copyfile(fileaddress,dest)
        Button(screen2,text="Next",command=chosegesture).pack()
       

    Label(screen2,text="Choose image file for Image Segmentation verification",fg="green",font="calibri 13 bold").pack()
    Button(screen2,text="Choose file",command=chfile,width=30,height=3).pack()
    
    
    screen2.mainloop()
    return 
    
#choosefile("udram")