from tkinter import *
from connect import Connection
from dao.campeonato import CampeonatoDAO

class Campeonato(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        self.controller = controller
        conn = Connection()
        self.campeonatoDao = CampeonatoDAO(conn)

        frameTitle = Frame(self)
        frameTitle.pack(side=TOP, fill=X, padx=20, pady=5)

        self.title = Label(frameTitle, text="Campeonato")
        self.title.pack()

        frameGrid = Frame(self)
        frameGrid.pack(side=TOP, fill=X, padx=20, pady=10)

        Label(frameGrid, text="Partida1").grid(row=0,column=0)
        Label(frameGrid, text="Partida2").grid(row=1,column=0)
        Label(frameGrid, text="Partida3").grid(row=2,column=0)

        frameBottom = Frame(self)
        frameBottom.pack(side=TOP, fill=X, padx=20, pady=10)

        Label(frameBottom, text="Bottom").pack()

    def setIdCampeonato(self, id):
        self.id_campeonato = id
        name = self.campeonatoDao.getName(id)
        # print(self.title)
        self.title["text"] = name
        # print(name)