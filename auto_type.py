from tkinter import * # pylint: disable=unused-wildcard-import
import getpass
import zipfile
import os
import time
from pynput.keyboard import Key, Controller

class Application:
    def __init__(self):
        self.space = "                    "
        self.ui_init()
        self.ui_props()
        self.ui_add()
        self.keyboard = Controller()

    def function_copy(self):
        os.system("press_mouse.exe")
        time.sleep(1)
        self.keyboard.type(self.a1)
    def function_copyII(self):
        os.system("press_mouse.exe")
        time.sleep(1)
        self.pageC = self.pageCEntry.get()
        self.keyboard.type(self.a2.format(self.pageC))
    def function_copyIII(self):
        os.system("press_mouse.exe")
        time.sleep(1)
        self.pageE = self.pageEEntry.get()
        self.keyboard.type(self.a3.format(self.pageE))
    def function_aufgabe(self):
        os.system("press_mouse.exe")
        time.sleep(1)
        self.book = self.bookEntry.get()
        self.pageSA = self.bookPageEntry.get()
        self.A = self.bookAufgabeEntry.get()
        self.keyboard.type(self.a4.format(self.book, self.pageSA, self.A))


    def ui_init(self): #Initialize Widgets
        self.pageC = ""
        self.pageE = ""
        self.pageSA = ""
        self.A = ""
        self.book = ""
        self.a1 = "Αντιγραφή λαθών ορθογραφίας"
        self.a2 = "Λέξεις σελ. {}"
        self.a3 = "Επανάληψη σελ. {}"
        self.a4 = "Ασκήσεις στο {} S.{}, Aufgabe {}"

        self.copy = Button(root)
        self.pageCLabel = Label(root)
        self.pageCEntry = Entry(root)
        self.words = Button(root)
        self.pageELabel = Label(root)
        self.pageEEntry = Entry(root)
        self.words2 = Button(root)
        self.bookLabel = Label(root)
        self.bookEntry = Entry(root)
        self.bookPageLabel = Label(root)
        self.bookPageEntry = Entry(root)
        self.bookAufgabeLabel = Label(root)
        self.bookAufgabeEntry = Entry(root)
        self.bookAufgabeButton = Button(root)

    def ui_props(self): #Properties
        self.copy.config(text='Αντιγραφή λαθών ορθογραφίας')
        self.copy.config(font=("Roboto-Medium", 10))
        self.pageCLabel.config(text='Λέξεις Σελίδα: ')
        self.pageCEntry.config(font=("Roboto-Medium", 10))
        self.words.config(text='Λέξεις')
        self.words.config(font=("Roboto-Medium", 10))
        self.pageELabel.config(text='Επανάληψη Σελίδα: ')
        self.pageEEntry.config(font=("Roboto-Medium", 10))
        self.words2.config(text='Επανάληψη')
        self.words2.config(font=("Roboto-Medium", 10))
        self.bookLabel.config(text='Βιβλίο: ')
        self.bookLabel.config(font=("Roboto-Medium", 10))
        self.bookPageLabel.config(text='Σελίδα για ασκήσεις: ')
        self.bookPageLabel.config(font=("Roboto-Medium", 10))
        self.bookAufgabeLabel.config(text='Ασκήσεις: ')
        self.bookAufgabeLabel.config(font=("Roboto-Medium", 10))
        self.bookAufgabeButton.config(text='Ασκήσεις')
        self.bookAufgabeButton.config(font=("Roboto-Medium", 10))
        self.copy.config(command=self.function_copy)
        self.words.config(command=self.function_copyII)
        self.words2.config(command=self.function_copyIII)
        self.bookAufgabeButton.config(command=self.function_aufgabe)


    def ui_add(self): #Add Widgets
        self.copy.pack()
        self.pageCLabel.pack()
        self.pageCEntry.pack()
        self.words.pack()
        self.pageELabel.pack()
        self.pageEEntry.pack()
        self.words2.pack()
        self.bookLabel.pack()
        self.bookEntry.pack()
        self.bookPageLabel.pack()
        self.bookPageEntry.pack()
        self.bookAufgabeLabel.pack()
        self.bookAufgabeEntry.pack()
        self.bookAufgabeButton.pack()

root = Tk()
root.title("Auto Type")
root.geometry("800x400")
Application = Application()
root.mainloop()
