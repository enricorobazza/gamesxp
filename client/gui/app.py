from tkinter import *

class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="Primeiro widget")
        self.btn = Button(self.widget1, text="Meu botão")
        self.msg.pack()
        self.btn.pack()


root = Tk()
root.title("My app")
root.minsize(500,500)
Application(root)
root.mainloop()