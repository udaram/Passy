from tkinter import*
from PIL import Image, ImageTk
from password_hasher import hashing_method
#from gesture import create_new_gesture
from gesture import login_gesture
from  fileacess import choosefile
from image_br import image_seg
from successMessage import Message

username_store="uda"
'''
def thankingGUI():
    thank=Tk()
    thank.geometry("500x400")
    thank.title("Thanks")
    image=Image.open("login.jpeg")
    photo=ImageTk.PhotoImage(image)
    #photo.resize()
    #Label(thank,text="hi").pack()  
    Label(thank,image=photo).pack()
    #thank.mainloop()    
'''
def Authentication_failed():
    #auth_screen=Tk()
    auth_screen=Toplevel(screen)
    auth_screen.geometry("400x400")
    oops=Image.open("oops.jpeg")
    photo=ImageTk.PhotoImage(oops)
    #photo.resize()
    auth_screen.title("Authentication Failed")
    Label(auth_screen,image=photo).pack()
    Label(auth_screen,text="Authentication Failed!!!",fg="red",font="calibri 14 bold").pack()
    Button(auth_screen,text="Quit",command=quit_from,height=3,width=20,bg="brown",font="calibri 15 bold",pady=10).pack()
    auth_screen.mainloop()

def quit_from():
    quit()
def playmovie():
    pass

def Gesture_verification():
    #print(username_store)
    #print(username_store,"hihhh")
    auth=login_gesture(username_store)
    if auth is False:
        Authentication_failed()
        #Label(g_screen,text="Oops!!Authentication Failed!!",fg="red",font="Calibri 8 bold").pack()
        #Button(g_screen,text="Quit",command=quit_from).pack()
    else:
        Label(g_screen,text="Authentication completed succesfully",fg="Green",font="Calibri 12 bold").pack()
        Button(g_screen,text="Click to play the movie",bg="Blue",command=playmovie).pack()
        Button(g_screen,text="Quit",command=quit_from,fg="Black",bg="red",font="calibri 12 bold").pack()
    pass
def Gesture_verification_gui():
    global g_screen
    g_screen=Toplevel(screen)
    g_screen.geometry("800x400")
    Label(g_screen,text="Congratulation!! You have completed two steps of verification",fg="Green",font="Calibri 16 bold").pack()
    Button(g_screen,text="Click for Gesture Verification",command=Gesture_verification).pack()
    

def imagesegmentation():
    #print("hi")
    image="/home/udaram/PythonGUI/login/imagesegImg/"+username_store+".jpeg"
    print(image)
    ff=image_seg(image)
    if(ff is False):
        Authentication_failed()
        print("Sorry your authentication failed")
        print("bi",ff)
    else:
        Gesture_verification_gui()
        print("hi",ff) 
    pass    

def validation():
    global username_store
    username_store=username.get()
    check=check_database(username_store)
    if check is not None:
        check=check[:-1]
    
    if check==None:
        Label(login_screen,text="Oops!!It seems username doesn't exist",fg="red").pack()
    elif hashing_method(password.get()) == check:
        Label(login_screen,text="Successfully completed Step1",fg="green").pack()
        Button(login_screen,text="Enter for Step2",command=imagesegmentation,fg="blue",bg="grey").pack()
    else:
        Label(login_screen,text="Oops!!It seems password doesn't match",fg="red").pack() 
        
    username_entry.delete(0,END)
    password_entry.delete(0,END)


def login():
    global username_entry
    global password_entry
    global username
    global password
    global login_screen
    #global username_store
    login_screen=Toplevel(screen)
    login_screen.geometry("500x400")
    login_screen.title("Password Login")
    username=StringVar()
    password=StringVar()
    #agree=IntVar()

    Label(login_screen,text="Enter Your Details",font="Helvetica 16 bold").pack()
    Label(login_screen,text="Username",font="Helvetica 16 bold").pack()
    username_entry=Entry(login_screen,textvariable=username)
    username_entry.pack(pady=10)
    Label(login_screen,text="Password",font="Helvetica 16 bold").pack()
    password_entry=Entry(login_screen,show="*",textvariable=password)
    password_entry.pack(pady=10)
    Button(login_screen,text="Login",height=2,width=20,command=validation).pack(pady=10)
    Button(login_screen,text="Quit",command=quit_from).pack()
    

def check_database(username):
        file= open("database.txt","r") 
        for line in file:
                fields=line.split(" ")
                field1=fields[0]
                if(field1==username):
                        file.close()
                        return fields[1]
        file.close()                
        return None

def Register_user():
    global username_store
    username_store=username.get()
    check=check_database(username.get())
    if(check is None):
        user=username.get()
        file= open("database.txt","a") 
        data=str(user)+" "+str(hashing_method(password.get()))+"\n"
        print(data)
        file.write(data) 
        file.close()         
    username_entry.delete(0,END)
    password_entry.delete(0,END) 
    if(check is None):
        Label(r_screen,text="Succesfully completed step1",fg="green").pack()
        #for image segmentation
        choosefile(user)
        Message(username_store)
        
    else:
        Label(r_screen,text="Oops!!It seems username already exist",fg="red").pack()
    
    #gesture.create_new_gesture(username.get())

    #call to Image Segmentation
    #Image_segmentation()

def Register():
    #r_screen=Tk()
    global username_entry
    global password_entry
    global username
    global password
    global r_screen
    r_screen=Toplevel(screen)
    r_screen.title("Register")
    username=StringVar()
    password=StringVar()
    agree=IntVar()
    r_screen.geometry("540x400")
    Label(r_screen,text="Enter Your Details",font="Helvetica 16 bold").pack()
    Label(r_screen,text="Username",font="Helvetica 16 bold").pack()
    username_entry=Entry(r_screen,textvariable=username)
    username_entry.pack(pady=10)
    Label(r_screen,text="Password",font="Helvetica 16 bold").pack()
    password_entry=Entry(r_screen,show="*",textvariable=password)
    password_entry.pack(pady=10)
    Button(r_screen,text="Submit",height=2,width=20,command=Register_user).pack(pady=10)

    #r_screen.mainloop()
     
def main_screen():
    global screen
    screen=Tk()
    screen.geometry("500x400")
    image=Image.open("login.jpeg")
    photo=ImageTk.PhotoImage(image)
    #photo.resize()
    Label(image=photo).pack()
    screen.title("Welcome to login")
    Button(text="Login",height="2",width="30",command=login).pack(pady=20)
    Button(text="Register",height="2",width="30",command=Register).pack()

    screen.mainloop()

main_screen()
#Authentication_failed()