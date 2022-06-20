import tkinter as tk
from gui import player
from functions import listboxManagement
from functions import adminManagement
from functions import windowManagement

# CLASS INITIALISATION
windowManagement = windowManagement.WindowManagementClass()
listboxManagement = listboxManagement.ListboxManagementClass()
adminManagement = adminManagement.AdminManagementClass()


# BACK FUNCTION
def goBackToMainWindow(window, userID):
    window.destroy()
    player.mainWindow(userID)


def adminPanelWindow(userID):
    # WINDOW INITIALISATION
    window = tk.Tk()

    # MEASUREMENTS
    screenWidth = 820
    screenHeight = 230
    buttonWidth = 30

    # WINDOW CONFIGURATION
    window.geometry("%dx%d" % (screenWidth, screenHeight))
    window.configure(bg="silver")
    window.top_bar = tk.Frame(window, bg="Red", cursor="sizing")
    window.title("Admin Panel")
    window.resizable(False, False)
    pixelVirtual = tk.PhotoImage(width=1, height=1)

    # CREATION
    # LABEL CREATION
    userLabel = tk.Label(window, text='userID', width=10, bg="#5c1a56",
                         fg="silver")
    songLabel = tk.Label(window, text='songID', width=10, bg="#5c1a56",
                         fg="silver")

    # ENTRY CREATION
    userEntry = tk.Entry(window, width=30)
    songEntry = tk.Entry(window, width=30)

    # LISTBOX CREATION
    adminListbox = tk.Listbox(window, height=8, width=60, selectmode='multiple',
                              borderwidth=0,
                              highlightthickness=0)
    scrollbar = tk.Scrollbar(adminListbox)

    # BUTTON CREATION
    deleteUserButton = tk.Button(window, width=int(buttonWidth / 3), text='Delete User', bg="#5c1a56",
                                 fg="silver",
                                 command=lambda: adminManagement.deleteUserAdmin(userEntry, songEntry))
    deleteSongButton = tk.Button(window, width=int(buttonWidth / 3), text='Delete Song', bg="#5c1a56",
                                 fg="silver",
                                 command=lambda: adminManagement.deleteSongAdmin(userEntry, songEntry))
    giveAdminButton = tk.Button(window, width=int(buttonWidth / 3), text='Update', bg="#5c1a56",
                                fg="silver",
                                command=lambda: adminManagement.giveUserAdminRights(userEntry, songEntry))

    showUserDataButton = tk.Button(window, width=5, text='Users', bg="#5c1a56",
                                   fg="silver",
                                   command=lambda: listboxManagement.getUsersDataAdminListbox(adminListbox))
    showSongDataButton = tk.Button(window, width=5, text='Songs', bg="#5c1a56",
                                   fg="silver",
                                   command=lambda: listboxManagement.getSongsDataAdminListbox(adminListbox))
    backButton = tk.Button(window, text="Back", width=5,
                           bg="#5c1a56",
                           fg="silver",
                           font="sans 8 bold",
                           command=lambda: goBackToMainWindow(window, userID))
    exitButton = tk.Button(window, text="Leave", height=20, width=40, image=pixelVirtual,
                           bg="#5c1a56",
                           fg="silver",
                           compound="c", font="sans 8 bold", command=lambda: [windowManagement.exitApp(window)])
    # CREATION END

    # CONFIGURATION
    # LISTBOX CONFIGURATION
    adminListbox.config(yscrollcommand=scrollbar.set)
    adminListbox.configure(justify="center")
    adminListbox.configure(background="#260033", foreground="white")
    scrollbar.config(command=adminListbox.yview)
    # CONFIGURATION END

    # PLACING
    # LABEL PLACING
    songLabel.place(x=screenWidth * 0.75 - 140, y=screenHeight / 10 * 2)
    userLabel.place(x=screenWidth * 0.75 - 140, y=screenHeight / 10 * 3)

    # ENTRY PLACING
    songEntry.place(x=screenWidth * 0.75 - 65, y=screenHeight / 10 * 2)
    userEntry.place(x=screenWidth * 0.75 - 65, y=screenHeight / 10 * 3)

    # LISTBOX PLACING
    adminListbox.place(x=screenWidth * 0.25 - 160, y=screenHeight / 10 * 1.25)

    # BUTTON PLACING
    deleteSongButton.place(x=screenWidth * 0.75 - 140, y=screenHeight / 10 * 5)
    deleteUserButton.place(x=screenWidth * 0.75 - 50, y=screenHeight / 10 * 5)
    giveAdminButton.place(x=screenWidth * 0.75 + 40, y=screenHeight / 10 * 5)
    showSongDataButton.place(x=175, y=screenHeight / 10 * 8)
    showUserDataButton.place(x=235, y=screenHeight / 10 * 8)
    backButton.place(x=screenWidth - 45, y=screenHeight / 10 * 8.9)
    exitButton.place(x=screenWidth - 50, y=2)
    # PLACING END

    window.mainloop()
