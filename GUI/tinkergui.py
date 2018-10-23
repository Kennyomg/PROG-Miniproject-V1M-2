from tkinter import *
from tkinter.messagebox import showinfo
#from marvel import * #weet nog niet helemaal hoe ik dit moet importen ipv github


def startquiz():
    if len(inputname.get()) >= 1 and inputname.get() != 'Input Username':
        showquestion()
    else:
        showinfo(title='Username error', message = 'Please enter a valid username')

def showquestion():
    Startscreen.pack_forget()
    quizquestions.pack


def loadStartscreen():
    Startscreen.pack()

#clear The asking for username sentence
def Clearinput(event):
    inputname.delete(0, "end")



#creating the main window and fixing it's size
gamewd = Tk()
icon = PhotoImage(file='icon.png')
gamewd.tk.call('wm', 'iconphoto', gamewd._w, icon)
gamewd.title("Super Quizz")
gamewd.geometry("500x500")
gamewd.resizable(0,0)
gamewd.config(bg='black')

#creating start frame
Startscreen = Frame(master=gamewd)
Startscreen.pack(fill="both",expand = True)


#set image as background in startscreen
bkg = PhotoImage(file="bkgmarvel.png")
bkgwallpaper = Label(master=Startscreen, image=bkg)
bkgwallpaper.pack(side=BOTTOM)

#specifying start frame containments
header = Label(master=Startscreen,
               text= "Super Quizz\n The G A M E",
               background = 'black',
               foreground = '#2CADE9',
               font=('Elephant',25,'bold'))

#place header
header.place(relx=0.5, rely=0.1, anchor=CENTER)

#Input bar to save username
inputname = Entry(master=Startscreen)
inputname.insert(0,'Input Username')
inputname.place(relx=0.5, rely=0.5, anchor=CENTER)

#if Left mouse button preseed clear inputname
inputname.bind("<Button-1>", Clearinput)


#startquizbutton on startscreen
startquizbutton = Button(master=Startscreen,text = 'Start quiz',command=startquiz)
startquizbutton.place(relx=0.5,rely=0.6,anchor=CENTER)



#quiz started display question
quizquestions = Frame(master=gamewd)
quizquestions.pack(fill="both", expand= True)



#Startscreen()
gamewd.mainloop()