from tkinter import*
from PIL import Image, ImageTk
from password_hasher import hashing_method
#from gesture import create_new_gesture
from gesture import login_gesture
from  fileacess import choosefile
from image_br import image_seg
from successMessage import Message
#from Movieplay import play
from account import account

username_store="uda"

def destroy(s):
    s.destroy()
    

def Authentication_failed():
    screen.destroy()
    auth_screen=Tk()
    auth_screen.geometry("400x400")
    oops=Image.open("oops.jpeg")
    photo=ImageTk.PhotoImage(oops)
    
    auth_screen.title("Authentication Failed")
    Label(auth_screen,image=photo).pack()
    Label(auth_screen,text="Authentication Failed!!!",fg="red",font="calibri 14 bold").pack()
    Button(auth_screen,text="Quit",command=quit_from,height=3,width=20,bg="brown",font="calibri 15 bold",pady=10).pack()
    auth_screen.mainloop()

def Goaccount():
    g_screen.destroy()
    screen.destroy()
    account(username_store)


def quit_from():
    quit()
def playmovie():
    play()
    pass

def Gesture_verification():
    auth=login_gesture(username_store)
    if auth is False:
        g_screen.destroy() 
        Authentication_failed()
    else:
        Label(g_screen,text="Authentication completed succesfully",bg="yellow",fg="Green",font="Calibri 12 bold").pack(pady=5)
        #Button(g_screen,text="Click to play the movie",bg="Blue",command=playmovie).pack()
        Button(g_screen,text="Go to Account",command=Goaccount,fg="Black",bg="red",font="calibri 12 bold").pack(pady=5)
    pass
def Gesture_verification_gui():
    global g_screen
    g_screen=Toplevel(screen)
    g_screen.geometry("800x400")
    ges=Image.open("gesture.jpeg")
    photto=ImageTk.PhotoImage(ges)
    g_screen.title("Gesture verification")
    Label(g_screen,image=photto).pack()
    Label(g_screen,text="Congratulation!! You have completed two steps of verification",fg="Green",font="Calibri 16 bold").pack()
    Button(g_screen,text="Click for Gesture Verification",fg="blue",bg="magenta",command=Gesture_verification).pack()
    g_screen.mainloop()

def imagesegmentation():
    login_screen.destroy()
    image="imagesegImg/"+username_store+".jpeg"
    ff=image_seg(image)
    if(ff is False):
        Authentication_failed()  
    else:
        Gesture_verification_gui()
        
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
    login_screen.geometry("500x500")
    login_screen.title("Password Login")
    username=StringVar()
    password=StringVar()
    detail=Image.open("detail.png")
    photo=ImageTk.PhotoImage(detail)
    Label(login_screen,image=photo).pack()
    Label(login_screen,text="Enter Your Details",font="Helvetica 16 bold",bg="violet").pack()
    Label(login_screen,text="Username",font="Helvetica 16 bold",bg="violet").pack()
    username_entry=Entry(login_screen,textvariable=username)
    username_entry.pack(pady=10)
    Label(login_screen,text="Password",font="Helvetica 16 bold",bg="violet").pack()
    password_entry=Entry(login_screen,show="*",textvariable=password)
    password_entry.pack(pady=10)
    Button(login_screen,text="Login",height=2,width=20,command=validation,bg="orange").pack(pady=10)
    Button(login_screen,text="Quit",command=quit_from,bg="red").pack()
    login_screen.mainloop() 

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
        #print(data)
        file.write(data) 
        file.close()         
    username_entry.delete(0,END)
    password_entry.delete(0,END) 
    if(check is None):
        Label(r_screen,text="Succesfully completed step1",bg="yellow",fg="green").pack()
        #for image segmentation
        screen.destroy()
        choosefile(user)
        Message(username_store)
    else:
        Label(r_screen,text="Oops!!It seems username already exist",fg="red").pack()
     
def Register():
    global username_entry
    global password_entry
    global username
    global password
    global r_screen
    r_screen=Toplevel(screen)
    r_screen.title("Register to Create Account")
    username=StringVar()
    password=StringVar()
    agree=IntVar()
    r_screen.geometry("540x400")
    Label(r_screen,text="Enter Your Details",font="Helvetica 16 bold",bg="pink").pack()
    Label(r_screen,text="Username",font="Helvetica 16 bold",bg="pink").pack()
    username_entry=Entry(r_screen,textvariable=username)
    username_entry.pack(pady=10)
    Label(r_screen,text="Password",font="Helvetica 16 bold",bg="pink").pack()
    password_entry=Entry(r_screen,show="*",textvariable=password)
    password_entry.pack(pady=10)
    Button(r_screen,text="Submit",height=2,width=20,command=Register_user,bg="violet").pack(pady=10)

    
     
def main_screen():
    global screen
    screen=Tk()
    screen.geometry("500x400")
    image=Image.open("login.jpeg")
    photo=ImageTk.PhotoImage(image)
    
    Label(image=photo).pack()
    screen.title("Welcome to login")
    Button(text="Login",height="2",width="30",command=login,bg="orange").pack(pady=20)
    Button(text="Register",height="2",width="30",command=Register,bg="pink").pack()
    screen.mainloop()

main_screen()
