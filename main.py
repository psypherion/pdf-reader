
import pyttsx3
import PyPDF2
from  tkinter.filedialog import *
from tkinter import *
import tkinter as tk

root = tk.Tk()



def pdmsfread():
    book = askopenfilename()
    pdfreader = PyPDF2.PdfFileReader(book)
    pages = pdfreader.numPages
    print(pdfreader.documentInfo)
    print(pdfreader.getNumPages())

    for num in range (0,pages):
        page = pdfreader.getPage(num)
        text = page.extractText()
        player =  pyttsx3.init()
        player.say(text)
        player.runAndWait()

T = tk.Text(root, height=40, width=37)
T.pack()
T.insert(tk.END, "TAKE NOTES HERE!!!!!")

btn1 = tk.Button(root, text="pdfreader", command=pdmsfread)
btn1.pack()
btn2 = tk.Button(root, text="OCR", state=DISABLED)
btn2.pack()
btn3 = tk.Button(root, text="Text to speech", state=DISABLED)
btn3.pack()
btn4 = tk.Button(root, text="speech to text", state=DISABLED)
btn4.pack()
tk.mainloop() 
