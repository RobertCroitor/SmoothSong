import tkinter as tk
from tkinter.messagebox import showinfo
from postgres import userTableClass as userClass
from functions import cryptingManagement

# CLASS INITIALISATION
userTable = userClass.Users()


class AuthentificationManagerClass:
    # LOGIN FUNCTIONS
    @staticmethod
    def login(nameEntry, passwordEntry):
        inputUsername = (nameEntry.get())
        inputPassword = (passwordEntry.get())
        if inputUsername == "" and inputPassword == "":
            tk.messagebox.showwarning(title="Error", message="Username and Password cannot be empty")
        else:
            if inputUsername == "":
                passwordEntry.delete(0, tk.END)
                tk.messagebox.showwarning(title="Error", message="Username cannot be empty")
            else:
                if inputPassword == "":
                    tk.messagebox.showwarning(title="Error", message="Password cannot be empty")
                else:

                    count = userTable.getCountUserByUsername(inputUsername)[0][0]
                    if count == 0:
                        passwordEntry.delete(0, tk.END)
                        tk.messagebox.showwarning(title="Error", message="Wrong Username")

                    else:
                        cryptedInputPassword = cryptingManagement.encrypt(inputPassword)
                        dbPassword = userTable.getUserByUsername(inputUsername)[0][2]
                        if dbPassword != cryptedInputPassword:
                            passwordEntry.delete(0, tk.END)
                            tk.messagebox.showwarning(title="Error", message="Wrong Password")

                        else:
                            userID = userTable.getUserByUsername(inputUsername)[0][0]
                            return userID
        return -1

    # LOGIN FUNCTIONS END

    # REGISTER FUNCTIONS
    @staticmethod
    def register(nameEntry, passwordEntry, rePasswordEntry):
        inputUsername = (nameEntry.get())
        inputPassword = (passwordEntry.get())
        inputRePassword = (rePasswordEntry.get())
        if inputUsername == "":
            passwordEntry.delete(0, tk.END)
            rePasswordEntry.delete(0, tk.END)
            tk.messagebox.showwarning(title="Error", message="Username cannot be empty")
        else:

            count = userTable.getCountUserByUsername(inputUsername)[0][0]
            if count == 1:
                passwordEntry.delete(0, tk.END)
                rePasswordEntry.delete(0, tk.END)
                tk.messagebox.showwarning(title="Error", message="Username is already used")
            else:
                if inputPassword == "":
                    rePasswordEntry.delete(0, tk.END)
                    tk.messagebox.showwarning(title="Error", message="Password cannot be empty")
                else:
                    if inputRePassword == "":
                        tk.messagebox.showwarning(title="Error", message="Password confirmation cannot be empty")
                    else:
                        if len(inputPassword) < 8:
                            passwordEntry.delete(0, tk.END)
                            rePasswordEntry.delete(0, tk.END)
                            tk.messagebox.showwarning(title="Error", message="Password must be at least 8 characters")
                        else:
                            if inputPassword != inputRePassword:
                                rePasswordEntry.delete(0, tk.END)
                                tk.messagebox.showwarning(title="Error", message="Passwords do not match")
                            else:
                                confirmation = userTable.insertUser(inputUsername, inputPassword)
                                if confirmation:
                                    tk.messagebox.showwarning(title="Success",
                                                              message="Register Successfully")
                                    return True
                                else:
                                    tk.messagebox.showwarning(title="Error",
                                                              message="Register Failed")
        return False

    # REGISTER FUNCTIONS END
