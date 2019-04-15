from tkinter import *
from tkinter import filedialog
from shutil import copyfile
from gesture import create_new_gesture

def quit_prog():
    quit()

#global fileaddress
def choosegesturefile(username):
    print(username)
    screen2 =Tk()
    screen2.geometry("700x200")
    screen2.title("Choose file")
    def creategesture():
        create_new_gesture(username)
        return
    def chfile():
        fileaddress=filedialog.askopenfilename(initialdir = "/home/udaram/PythonGUI/login/img",title = "Select file",filetypes = (("jpeg files","*.jpeg"),("all files","*.*")))
        dest="/home/udaram/PythonGUI/login/gestureImg/"+str(username)+".jpeg"
        copyfile(fileaddress,dest)
        Button(screen2,text="Create Gesture Password",command=creategesture,fg="Blue",font="calibri 10 bold").pack()
       
    Label(screen2,text="Choose image file for Gesture verification",fg="green",font="calibri 16 bold").pack()
    Button(screen2,text="Choose file",command=chfile,width=30,height=3).pack()
    screen2.mainloop()
