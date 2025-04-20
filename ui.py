import tkinter
from tkinter import * 
from userDatabaseManager import *
from encryptionManager import *
from userActionManager import * 

def loginWindow():
    Login=Toplevel(root)
    Login.title("Login")
    Login.geometry("500x500")

    existingUsernameInput = StringVar()
    existingPasswordInput = StringVar()

    titleLabel = Label(Login, text = "Welcome back!", width=30)
    titleLabel.place(x=70, y=60)

    usernameLabel = Label(Login, text = "Enter username", width=30)
    usernameLabel.place(x=70, y=100)
    usernameEntry = Entry(Login, textvariable=existingUsernameInput)
    usernameEntry.place(x=110, y=130)

    passwordLabel = Label(Login, text = "Enter password", width=30)
    passwordLabel.place(x=70, y=160)
    passwordEntry = Entry(Login, textvariable=existingPasswordInput)
    passwordEntry.place(x=110, y=190)

    Button(Login, text="Login", width=20, bg="grey", fg="white",  command=lambda: loginExistingUser(existingUsernameInput.get(), existingPasswordInput.get())).place(x=120, y=240)
    Button(Login, text="Login with Injection Mode", width=20, bg="grey", fg="white", command=lambda: loginExistingUserForInjection(existingUsernameInput.get(), existingPasswordInput.get())).place(x=120, y=270)


root = Tk()
root.geometry("500x500")
root.title("Registration Window")

newUsernameInput = StringVar()
newPasswordInput = StringVar()

titleLabel = Label(root, text = "Welcome new user!", width=30)
titleLabel.place(x=100, y=60)

usernameLabel = Label(root, text = "Enter new username", width=30)
usernameLabel.place(x=80, y=100)
usernameEntry = Entry(root, textvariable=newUsernameInput)
usernameEntry.place(x=110, y=130)

usernameLabel = Label(root, text = "Enter new password", width=30)
usernameLabel.place(x=80, y=160)
usernameEntry = Entry(root, textvariable=newPasswordInput)
usernameEntry.place(x=110, y=190)

Button(root, text="Register", width=20, bg="grey", fg="white", command=lambda: addNewUser(newUsernameInput.get(), newPasswordInput.get())).place(x=120, y=240)
Button(root, text="I already have an account.", width=20, bg="grey", fg="white", command=loginWindow).place(x=120, y=290)

root.mainloop()

'''
Academic Integrity Notes:
    The underlying structure of the two page UI was adapated from this source: https://owlbuddy.com/login-and-signup-using-sqlite/
    Inspriation for the method used for login and password passing is from this source: https://www.w3resource.com/python-exercises/tkinter/python-tkinter-basic-exercise-16.php#google_vignette
    Information on understand lambda functions in Tkinter was taken from:
        https://stackoverflow.com/questions/70406400/understanding-python-lambda-behavior-with-tkinter-button
        https://www.geeksforgeeks.org/using-lambda-in-gui-programs-in-python/
    Creation and styling of UI elements was sourced from:
        https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/label.html
        https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/tkMessageBox.html

    All sources can be found in sources.md in repo
'''

