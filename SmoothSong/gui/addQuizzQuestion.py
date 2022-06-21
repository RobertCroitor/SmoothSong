import tkinter as tk
from gui import adminPage
from functions import windowManagement
from functions import quizzGameManagement

# CLASS INITIALISATION
windowManagement = windowManagement.WindowManagementClass()
quizzGameManagement = quizzGameManagement.QuizzGameManagement()


# SWAP PAGE FUNCTIONS
def goBackToAdminPanel(window, userID, mode):
    window.destroy()
    adminPage.adminPanelWindow(userID, mode)


def quizzFormWindow(userID, mode):
    # WINDOW INITIALISATION
    window = tk.Tk()

    # MEASUREMENTS
    screenWidth = 800
    screenHeight = 384
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
    window.geometry("800x384+30+30")
    window.configure(bg=bgColor)
    window.top_bar = tk.Frame(window, bg="Red", cursor="sizing")
    window.title("Quizz game form")
    window.resizable(False, False)
    pixelVirtual = tk.PhotoImage(width=1, height=1)
    # CREATION
    # LABEL CREATION
    questionLabel = tk.Label(window, text='Question', width=10, bg=widgetColor,
                             fg=textColor, font="sans 8 bold", )

    firstAnswersLabel = tk.Label(window, text='Variant', width=10, bg=widgetColor,
                                 fg=textColor, font="sans 8 bold", )
    secondAnswersLabel = tk.Label(window, text='Variant', width=10, bg=widgetColor,
                                  fg=textColor, font="sans 8 bold", )
    thirdAnswersLabel = tk.Label(window, text='Variant', width=10, bg=widgetColor,
                                 fg=textColor, font="sans 8 bold", )
    fourthAnswersLabel = tk.Label(window, text='Variant', width=10, bg=widgetColor,
                                  fg=textColor, font="sans 8 bold", )

    correctLabel = tk.Label(window, text='Correct', width=10,
                            bg=widgetColor,
                            fg=textColor, font="sans 8 bold", )

    # ENTRY CREATION
    questionEntry = tk.Entry(window, bg=widgetColor, fg=textColor, width=90)
    firstAnswersEntry = tk.Entry(window, bg=widgetColor, fg=textColor, width=35)
    secondAnswersEntry = tk.Entry(window, bg=widgetColor, fg=textColor, width=35)
    thirdAnswersEntry = tk.Entry(window, bg=widgetColor, fg=textColor, width=35)
    fourthAnswersEntry = tk.Entry(window, bg=widgetColor, fg=textColor, width=35)
    correctEntry = tk.Entry(window, bg=widgetColor, fg=textColor, width=50)

    # BUTTON CREATION
    submitButton = tk.Button(window, width=int(buttonWidth / 2),
                             text='Submit', bg=widgetColor,
                             fg=textColor, font="sans 8 bold",
                             command=lambda: quizzGameManagement.addQuestionToQuizzTable(questionEntry,
                                                                                         firstAnswersEntry,
                                                                                         secondAnswersEntry,
                                                                                         thirdAnswersEntry,
                                                                                         fourthAnswersEntry,
                                                                                         correctEntry))
    backButton = tk.Button(window, text="Back", width=int(buttonWidth / 2),
                           bg=widgetColor,
                           fg=textColor,
                           font="sans 8 bold",
                           command=lambda: goBackToAdminPanel(window, userID, mode))
    exitButton = tk.Button(window, text="Leave", height=20, width=40, image=pixelVirtual,
                           bg=widgetColor,
                           fg=textColor,
                           compound="c", font="sans 8 bold", command=lambda: [windowManagement.exitApp(window)])
    # CREATION END

    # PLACING
    # LABEL PLACING
    questionLabel.place(x=screenWidth / 2 - 300, y=screenHeight / 10 * 1.5)
    firstAnswersLabel.place(x=screenWidth / 2 - 300, y=screenHeight / 10 * 3)
    secondAnswersLabel.place(x=screenWidth / 2 + 25, y=screenHeight / 10 * 3)
    thirdAnswersLabel.place(x=screenWidth / 2 - 300, y=screenHeight / 10 * 4.5)
    fourthAnswersLabel.place(x=screenWidth / 2 + 25, y=screenHeight / 10 * 4.5)
    correctLabel.place(x=screenWidth / 2 - 190, y=screenHeight / 10 * 6)

    # ENTRY PLACING
    questionEntry.place(x=screenWidth / 2 - 225, y=screenHeight / 10 * 1.5)
    firstAnswersEntry.place(x=screenWidth / 2 - 225, y=screenHeight / 10 * 3)
    secondAnswersEntry.place(x=screenWidth / 2 + 100, y=screenHeight / 10 * 3)
    thirdAnswersEntry.place(x=screenWidth / 2 - 225, y=screenHeight / 10 * 4.5)
    fourthAnswersEntry.place(x=screenWidth / 2 + 100, y=screenHeight / 10 * 4.5)
    correctEntry.place(x=screenWidth / 2 - 115, y=screenHeight / 10 * 6)

    # BUTTON PLACING
    submitButton.place(x=350, y=screenHeight / 10 * 7.5)
    backButton.place(x=350, y=screenHeight / 10 * 9)
    exitButton.place(x=screenWidth - 50, y=2)
    # PLACING END

    window.mainloop()
