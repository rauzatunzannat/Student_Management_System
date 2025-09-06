from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

def login():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error', 'Fields cannot be empty')
    elif usernameEntry.get() == 'EWU' and passwordEntry.get() == '1234':
        messagebox.showinfo('Success', 'Welcome')
        window.destroy()
        try:
            import sms
        except ImportError:
            messagebox.showerror('Error', 'sms.py file not found!')
    else:
        messagebox.showerror('Error', 'Please enter correct credentials')

#  Main Window
window = Tk()
window.geometry('1280x700+0+0')
window.title('Login System Of Student Management System')
window.resizable(False, False)

# Background
try:
    bg_img = Image.open('5f5dc1f24c66b961259136.jpg')
    bg_img = bg_img.resize((1280, 700))
    backgroundImage = ImageTk.PhotoImage(bg_img)
    bgLabel = Label(window, image=backgroundImage)
    bgLabel.place(x=0, y=0, relwidth=1, relheight=1)
except:
    window.configure(bg="lightblue")

# Login Frame
LoginFrame = Frame(window, bg="white", bd=5, relief=RIDGE)
LoginFrame.place(x=400, y=150)

# Load Images
try:
    LogoImage = PhotoImage(file='logo.png')
    userImage = PhotoImage(file='user.png')
    passwordImage = PhotoImage(file='password.png')
except:
    LogoImage = userImage = passwordImage = None

# Logo
if LogoImage:
    logoLabel = Label(LoginFrame, image=LogoImage, bg="white")
    logoLabel.grid(row=0, column=0, columnspan=2, pady=10)

# Username row
usernameLabel = Label(LoginFrame, image=userImage, text=" Username",
                      font=("Arial", 14), compound=LEFT, bg="white")
usernameLabel.grid(row=1, column=0, padx=10, pady=10)

usernameEntry = Entry(LoginFrame, font=("Arial", 14))
usernameEntry.grid(row=1, column=1, padx=10, pady=10)

# Password row
passwordLabel = Label(LoginFrame, image=passwordImage, text=" Password",
                      font=("Arial", 14), compound=LEFT, bg="white")
passwordLabel.grid(row=2, column=0, padx=10, pady=10)

passwordEntry = Entry(LoginFrame, font=("Arial", 14), show="*")
passwordEntry.grid(row=2, column=1, padx=10, pady=10)

# Login button
loginButton = Button(LoginFrame, text="Login", font=("Arial", 14), bg="blue", fg="white", command=login)
loginButton.grid(row=3, column=0, columnspan=2, pady=20)

window.mainloop()
