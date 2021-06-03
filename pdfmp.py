import PyPDF2
import pyttsx3
from tkinter import *     
from tkinter.filedialog import askopenfilename
import os


base = Tk()
base.geometry('150x100')

def file_open():
    bookname = askopenfilename()
    filepath = os.path.dirname(bookname)
    with open(bookname, 'rb') as book:

        text = ""

        reader = PyPDF2.PdfFileReader(book)

        audio_read = pyttsx3.init()
        audio_read.setProperty('volume',1)
        audio_read.setProperty('rate',150)
        voices = audio_read.getProperty('voices')       
        audio_read.setProperty('voice', voices[1].id) 

        for page in range(reader.numPages):
            next_pg = reader.getPage(page)
            content = next_pg.extractText()
            text += content
        print("start")
        audio_read.save_to_file(text, filepath + "/audio_pdf.mp3")
        audio_read.runAndWait()
        print("end")
x = Button(base, text ='Select Pdf file \nto convert mp3', command = lambda:file_open())
x.pack()
mainloop()