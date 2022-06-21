import tkinter as tk
from gui import player
from functions import windowManagement
from functions import quizzGameManagement as quizzGameManagementFile

# CLASS INITIALISATION
windowManagement = windowManagement.WindowManagementClass()
quizzGameManagement = quizzGameManagementFile.QuizzGameManagement()


# SWAP PAGE FUNCTIONS
def goBackToMainWindow(window, userID, mode):
    window.destroy()
    player.mainWindow(userID, mode)


def quizzGameWindow(userID, mode):
    # WINDOW INITIALISATION
    window = tk.Tk()

    # MEASUREMENTS
    screenWidth = 800
    screenHeight = 600
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
    window.geometry("800x600+30+30")
    window.top_bar = tk.Frame(window, bg="Red", cursor="sizing")
    window.title("Quizz game")
    window.resizable(False, False)
    pixelVirtual = tk.PhotoImage(width=1, height=1)

    # CREATION
    # LABEL CREATION
    correctCounterString = tk.StringVar()
    correctCounterString.set("Correct : 0/10")
    correctCounterLabel = tk.Label(window, textvariable=correctCounterString, relief=tk.RAISED, bg=widgetColor,
                                   fg=textColor, width=14, height=4, borderwidth=1, font="sans 8 bold",
                                   highlightthickness=0, )
    questionCounterString = tk.StringVar()
    questionCounterString.set("Questions : 1/10")
    questionCounterLabel = tk.Label(window, textvariable=questionCounterString, relief=tk.RAISED, bg=widgetColor,
                                    fg=textColor, width=14, height=4, borderwidth=1, font="sans 8 bold",
                                    highlightthickness=0, )
    # TEXT BOX CREATION
    questionTextBox = tk.Text(window, relief=tk.RAISED, bg=widgetColor, wrap=tk.WORD,
                              fg=textColor, width=78, height=8, borderwidth=0, font="sans 8 bold",
                              highlightthickness=0, )
    # ENTRY CREATION
    answerEntry = tk.Entry(window, bg=widgetColor, fg=textColor, font="sans 8 bold", width=40)

    # BUTTON CREATION

    firstVariant = tk.Button(window, width=int(buttonWidth), height=(int(buttonWidth / 6)), text='',
                             bg=widgetColor,
                             fg=textColor, font="sans 8 bold",

                             )
    secondVariant = tk.Button(window, width=int(buttonWidth), height=(int(buttonWidth / 6)), text='',
                              bg=widgetColor,
                              fg=textColor, font="sans 8 bold",

                              )
    thirdVariant = tk.Button(window, width=int(buttonWidth), height=(int(buttonWidth / 6)), text='',
                             bg=widgetColor,
                             fg=textColor, font="sans 8 bold",

                             )
    fourthVariant = tk.Button(window, width=int(buttonWidth), height=(int(buttonWidth / 6)), text='',
                              bg=widgetColor,
                              fg=textColor, font="sans 8 bold",

                              )

    backButton = tk.Button(window, text="Back", width=int(buttonWidth / 2),
                           bg=widgetColor,
                           fg=textColor,
                           font="sans 8 bold",
                           command=lambda: goBackToMainWindow(window, userID, mode))
    exitButton = tk.Button(window, text="Leave", height=20, width=40, image=pixelVirtual,
                           bg=widgetColor,
                           fg=textColor,
                           compound="c", font="sans 8 bold", command=lambda: [windowManagement.exitApp(window)])

    leaveQuizz = tk.Button(window, text="Back", width=int(buttonWidth * 0.8),
                           height=(int(buttonWidth / 7)),
                           bg=widgetColor,
                           fg=textColor,
                           compound="c", font="sans 8 bold", command=lambda: goBackToMainWindow(window, userID, mode))
    submitButton = tk.Button(window, text="Submit Answer", width=int(buttonWidth / 2),
                             bg=widgetColor,
                             fg=textColor,
                             font="sans 8 bold",
                             command=lambda: quizzGameManagementFile.checkAnswer(questionTextBox,
                                                                                 firstVariant, secondVariant,
                                                                                 thirdVariant,
                                                                                 fourthVariant,
                                                                                 answerEntry,
                                                                                 submitButton, correctCounterString,
                                                                                 leaveQuizz, backButton,
                                                                                 questionCounterString))
    startButton = tk.Button(window, width=int(buttonWidth), height=(int(buttonWidth / 6)), text='Start quizz',
                            bg=widgetColor,
                            fg=textColor, font="sans 8 bold",
                            command=lambda: [
                                quizzGameManagementFile.startQuizz(questionTextBox, correctCounterLabel,
                                                                   firstVariant, secondVariant, thirdVariant,
                                                                   fourthVariant, startButton, answerEntry,
                                                                   submitButton, questionCounterLabel)])

    # CREATION END

    # CONFIGURATION
    answerEntry.configure(justify="center")
    # CONFIGURATION END

    # PLACING
    # BUTTON PLACING
    startButton.place(x=screenWidth / 2 - 100, y=screenHeight / 2 - 50)
    backButton.place(x=2, y=2)
    exitButton.place(x=screenWidth - 50, y=2)
    # PLACING END

    window.mainloop()
