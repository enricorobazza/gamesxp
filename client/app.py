from tkinter import *
from list_campeonatos_gui import ListCampeonatos
from addPartida_gui import AddPartida
from campeonato_gui import Campeonato

class Application(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        container = Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        allFrames = [
            {"id":"ListCampeonatos", "frame":ListCampeonatos}, 
            {"id":"Campeonato", "frame":Campeonato},
            {"id":"AddPartida", "frame":AddPartida}
        ]

        for F in allFrames:

            frame = F["frame"](container, self)

            self.frames[F["id"]] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("ListCampeonatos")

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def get_frame(self, cont):
        return self.frames[cont]

app = Application()
app.minsize(500,500)
app.title("GamesXP")
app.mainloop()