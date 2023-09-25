import os
from tkinter import *
from gtts import gTTS
from playsound import playsound

# Initialize UI
root = Tk()
root.geometry('600x300')
root.resizable(0, 0)
root.config(bg='black')
root.title('TEXT TO SPEECH')

Label(root, text='Convert your Text into Voice',
      font='arial 20 bold', bg='black').pack()

Label(root, text='Enter Text', font='arial 15 bold',
      bg='black').place(x=20, y=60)

# Input field + entry handling
Msg = StringVar()
entry_field = Entry(root, textvariable=Msg, width='60')
entry_field.place(x=20, y=100)

# Define event handling for buttons
def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text=Message)
    speech.save('Data.mp3')
    playsound('Data.mp3')
    os.remove('Data.mp3')

def Exit():
    root.destroy()

def Reset():
    Msg.set("")


# Render Button with event handling
Button(root, text="PLAY", font='arial 15 bold',
       command=Text_to_speech, width=4).place(x=25, y=140)
Button(root, text='EXIT', font='arial 15 bold',
       command=Exit, bg='OrangeRed1').place(x=100, y=140)
Button(root, text='RESET', font='arial 15 bold',
       command=Reset).place(x=175, y=140)

# Loop infinitely
root.mainloop()