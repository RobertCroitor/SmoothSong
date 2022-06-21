import tkinter as tk
from tkinter.messagebox import showinfo
import random
from postgres import quizzGameTableClass

quizzGameTable = quizzGameTableClass.QuizzGame()


class QuizzGameManagement:
    @staticmethod
    def addQuestionToQuizzTable(questionEntry, firstAnswersEntry, secondAnswersEntry, thirdAnswersEntry,
                                fourthAnswersEntry, correctEntry):

        questionText = (questionEntry.get()).stip()
        firstAnswerText = (firstAnswersEntry.get()).stip()
        secondAnswerText = (secondAnswersEntry.get()).stip()
        thirdAnswerText = (thirdAnswersEntry.get()).stip()
        fourthAnswerText = (fourthAnswersEntry.get()).stip()
        correctText = (correctEntry.get()).stip()
        if questionText == "" or firstAnswerText == "" or secondAnswerText == "" \
                or thirdAnswerText == "" or fourthAnswerText == "" or correctText == "":
            tk.messagebox.showwarning(title="Error", message="You cannot have empty fields")
        else:
            answers = firstAnswerText + "%" + secondAnswerText + "%" + thirdAnswerText + "%" + fourthAnswerText
            if correctText == firstAnswerText or correctText == secondAnswerText \
                    or correctText == thirdAnswerText or correctText == fourthAnswerText:
                confirmation = quizzGameTable.insertSong(questionText, answers, correctText)
                if confirmation:
                    tk.messagebox.showwarning(title="Success", message=" Question inserted successfully")
                    questionEntry.delete(0, tk.END)
                    firstAnswersEntry.delete(0, tk.END)
                    secondAnswersEntry.delete(0, tk.END)
                    thirdAnswersEntry.delete(0, tk.END)
                    fourthAnswersEntry.delete(0, tk.END)
                    correctEntry.delete(0, tk.END)
                else:
                    tk.messagebox.showwarning(title="Error", message=" Failed to insert in the Quizz Table")

            else:
                tk.messagebox.showwarning(title="Error",
                                          message=" Failed \n Correct answer is not one of the variants!")


quizzGame = QuizzGameManagement()

randomIDSglobal = []
count = 0
correctCount = 0
questionCount = 1
correct = ""


def getQuestionFromTable():
    questionID = randomIDSglobal[count]
    questionData = quizzGameTable.getQuestionDataByID(questionID)[0]
    question = questionData[1]
    answers = questionData[2]
    splitAnswers = answers.split("%")
    firstAnswer = splitAnswers[0]
    secondAnswer = splitAnswers[1]
    thirdAnswer = splitAnswers[2]
    fourthAnswer = splitAnswers[3]
    global correct
    correct = questionData[3]
    return question, firstAnswer, secondAnswer, thirdAnswer, fourthAnswer


def generateRandomIDS():
    dbCount = quizzGameTable.getAllQuestionsCount()[0][0]
    global randomIDSglobal
    randomIDSglobal = (random.sample(range(1, dbCount), 10))


def startQuizz(textbox, countLabel, firstVariant, secondVariant, thirdVariant, fourthVariant, startButton,
               answerEntry, submitButton, questionCounterLabel):
    screenWidth = 800
    screenHeight = 600
    global count
    global correctCount
    global questionCount
    global correct
    count = 0
    correctCount = 0
    questionCount = 1
    correct = ""
    questionCounterLabel.place(x=screenWidth / 2 - 110, y=screenHeight / 2 - 110)
    countLabel.place(x=screenWidth / 2 + 30, y=screenHeight / 2 - 110)
    textbox.place(x=screenWidth / 2 - 225, y=50)
    startButton.place_forget()
    firstVariant.place(x=screenWidth / 2 - 225, y=screenHeight / 2 - 20)
    secondVariant.place(x=screenWidth / 2 + 25, y=screenHeight / 2 - 20)
    thirdVariant.place(x=screenWidth / 2 - 225, y=screenHeight / 2 + 80)
    fourthVariant.place(x=screenWidth / 2 + 25, y=screenHeight / 2 + 80)
    answerEntry.place(x=screenWidth / 2 - 110, y=screenHeight / 2 + 210)
    submitButton.place(x=screenWidth / 2 - 50, y=screenHeight / 2 + 240)
    generateRandomIDS()
    question, firstAnswer, secondAnswer, thirdAnswer, fourthAnswer = getQuestionFromTable()
    shuffleArray = [firstAnswer, secondAnswer, thirdAnswer, fourthAnswer]
    random.shuffle(shuffleArray)
    firstAnswer = shuffleArray[0]
    secondAnswer = shuffleArray[1]
    thirdAnswer = shuffleArray[2]
    fourthAnswer = shuffleArray[3]
    textbox.delete("1.0", tk.END)
    textbox.insert(tk.END, question)
    firstVariant['text'] = "A." + firstAnswer
    secondVariant['text'] = "B." + secondAnswer
    thirdVariant['text'] = "C." + thirdAnswer
    fourthVariant['text'] = "D." + fourthAnswer
    answerEntry.delete(0, tk.END)


def endQuizz(textbox, firstVariant, secondVariant, thirdVariant, fourthVariant,
             answerEntry, submitButton, leaveButton, backButton):
    screenWidth = 800
    screenHeight = 600
    textbox.place_forget()
    firstVariant.place_forget()
    secondVariant.place_forget()
    thirdVariant.place_forget()
    fourthVariant.place_forget()
    answerEntry.place_forget()
    submitButton.place_forget()
    backButton.place_forget()
    leaveButton.place(x=screenWidth / 2 - 80, y=screenHeight / 2 + 50)


def nextQuestion(textbox, firstVariant, secondVariant, thirdVariant, fourthVariant,
                 answerEntry, submitButton, leaveButton, backButton):
    global count
    count += 1
    if count < 10:
        question, firstAnswer, secondAnswer, thirdAnswer, fourthAnswer = getQuestionFromTable()
        textbox.delete("1.0", tk.END)
        textbox.insert(tk.END, question)
        shuffleArray = [firstAnswer, secondAnswer, thirdAnswer, fourthAnswer]
        random.shuffle(shuffleArray)
        firstAnswer = shuffleArray[0]
        secondAnswer = shuffleArray[1]
        thirdAnswer = shuffleArray[2]
        fourthAnswer = shuffleArray[3]
        firstVariant['text'] = "A." + firstAnswer
        secondVariant['text'] = "B." + secondAnswer
        thirdVariant['text'] = "C." + thirdAnswer
        fourthVariant['text'] = "D." + fourthAnswer
        answerEntry.delete(0, tk.END)
    else:
        endQuizz(textbox, firstVariant, secondVariant, thirdVariant, fourthVariant,
                 answerEntry, submitButton, leaveButton, backButton)


def checkAnswer(textbox, firstVariant, secondVariant, thirdVariant, fourthVariant,
                answerEntry, submitButton, countString, leaveButton, backButton, questionCounterString):
    answer = (answerEntry.get())
    if answer != "":
        answerText = ""
        if answer.upper() == "A":
            answerText = firstVariant['text'].split(".")[1]
        else:
            if answer.upper() == "B":
                answerText = secondVariant['text'].split(".")[1]
            else:
                if answer.upper() == "C":
                    answerText = thirdVariant['text'].split(".")[1]
                else:
                    if answer.upper() == "D":
                        answerText = fourthVariant['text'].split(".")[1]
        if answerText != "":
            global correctCount
            if answerText == correct:
                correctCount += 1
            global questionCount
            if questionCount < 10:
                questionCount += 1
            concatenateCorrectCountString = "Correct : " + str(correctCount) + "/10"
            countString.set(concatenateCorrectCountString)
            concatenateQuestionCountString = "Question : " + str(questionCount) + "/10"
            questionCounterString.set(concatenateQuestionCountString)
            nextQuestion(textbox, firstVariant, secondVariant, thirdVariant, fourthVariant,
                         answerEntry, submitButton, leaveButton, backButton)
        else:
            tk.messagebox.showwarning(title="Error", message=" Answer has to be A, B, C or D")
    else:
        tk.messagebox.showwarning(title="Error", message=" No answer given!")
