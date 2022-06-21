import tkinter as tk
from gui import player, addQuizzQuestion
from functions import listboxManagement
from functions import adminManagement
from functions import windowManagement

# CLASS INITIALISATION
windowManagement = windowManagement.WindowManagementClass()
listboxManagement = listboxManagement.ListboxManagementClass()
adminManagement = adminManagement.AdminManagementClass()


# SWAP WINDOW FUNCTION
def goBackToMainWindow(window, userID, mode):
    window.destroy()
    player.mainWindow(userID, mode)


def goToQuizzFormWindow(window, userID, mode):
    window.destroy()
    addQuizzQuestion.quizzFormWindow(userID, mode)


def adminPanelWindow(userID, mode):
    # WINDOW INITIALISATION
    window = tk.Tk()

    # MEASUREMENTS
    screenWidth = 820
    screenHeight = 230
    buttonWidth = 30

    # WINDOW CONFIGURATION
    if mode == "WHITE":
        bgColor = "#f5faf5"
        widgetColor = "#c0c2c0"
        textColor = "#000000"
    else:
        bgColor = "#3d3d3d"
        widgetColor = "#9c9c9c"
        textColor = "black"
    window.configure(bg=bgColor)
    window.geometry("820x230+30+30")
    window.top_bar = tk.Frame(window, bg="Red", cursor="sizing")
    window.title("Admin Panel")
    window.resizable(False, False)
    pixelVirtual = tk.PhotoImage(width=1, height=1)

    # CREATION
    # LABEL CREATION
    userLabel = tk.Label(window, text='userID', width=10, bg=widgetColor, font="sans 8 bold",
                         fg=textColor)
    songLabel = tk.Label(window, text='songID', width=10, bg=widgetColor, font="sans 8 bold",
                         fg=textColor)

    # ENTRY CREATION
    userEntry = tk.Entry(window, bg=widgetColor, fg=textColor, font="sans 8 bold", width=30)
    songEntry = tk.Entry(window, bg=widgetColor, fg=textColor, font="sans 8 bold", width=30)

    # LISTBOX CREATION
    adminListbox = tk.Listbox(window, height=8, width=60, selectmode='multiple',
                              borderwidth=1, font="sans 8 bold",
                              highlightthickness=0)
    scrollbar = tk.Scrollbar(adminListbox)

    # BUTTON CREATION
    deleteUserButton = tk.Button(window, width=int(buttonWidth / 3), text='Delete User', bg=widgetColor,
                                 fg=textColor, font="sans 8 bold",
                                 command=lambda: adminManagement.deleteUserAdmin(userEntry, songEntry))
    deleteSongButton = tk.Button(window, width=int(buttonWidth / 3), text='Delete Song', bg=widgetColor,
                                 fg=textColor, font="sans 8 bold",
                                 command=lambda: adminManagement.deleteSongAdmin(userEntry, songEntry))
    giveAdminButton = tk.Button(window, width=int(buttonWidth / 3), text='Update', bg=widgetColor,
                                fg=textColor, font="sans 8 bold",
                                command=lambda: adminManagement.giveUserAdminRights(userEntry, songEntry))

    showUserDataButton = tk.Button(window, width=7, text='Users', bg=widgetColor,
                                   fg=textColor, font="sans 8 bold",
                                   command=lambda: listboxManagement.getUsersDataAdminListbox(adminListbox))
    showSongDataButton = tk.Button(window, width=7, text='Songs', bg=widgetColor, font="sans 8 bold",
                                   fg=textColor,
                                   command=lambda: listboxManagement.getSongsDataAdminListbox(adminListbox))
    showQuestionDataButton = tk.Button(window, width=8, text='Questions', bg=widgetColor, font="sans 8 bold",
                                       fg=textColor,
                                       command=lambda: listboxManagement.getQuestionsDataAdminListbox(adminListbox))
    backButton = tk.Button(window, text="Back", width=6,
                           bg=widgetColor,
                           fg=textColor,
                           font="sans 8 bold",
                           command=lambda: goBackToMainWindow(window, userID, mode))
    quizzFormButton = tk.Button(window, text="Quizz", width=int(buttonWidth / 3),
                                bg=widgetColor,
                                fg=textColor,
                                font="sans 8 bold",
                                command=lambda: goToQuizzFormWindow(window, userID, mode))
    exitButton = tk.Button(window, text="Leave", height=20, width=40, image=pixelVirtual,
                           bg=widgetColor,
                           fg=textColor,
                           compound="c", font="sans 8 bold", command=lambda: [windowManagement.exitApp(window)])
    # CREATION END

    # CONFIGURATION
    # LISTBOX CONFIGURATION
    adminListbox.config(yscrollcommand=scrollbar.set)
    adminListbox.configure(justify="center")
    adminListbox.configure(bg=widgetColor, fg=textColor)
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
    quizzFormButton.place(x=screenWidth * 0.75 - 50, y=screenHeight / 10 * 7)
    showSongDataButton.place(x=120, y=screenHeight / 10 * 8)
    showQuestionDataButton.place(x=200, y=screenHeight / 10 * 8)
    showUserDataButton.place(x=290, y=screenHeight / 10 * 8)
    backButton.place(x=screenWidth - 45, y=screenHeight / 10 * 8.9)
    exitButton.place(x=screenWidth - 50, y=2)
    # PLACING END

    window.mainloop()
