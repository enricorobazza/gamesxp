from tkinter import *
from connect import Connection

class AddPartida(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        self.controller = controller
        conn = Connection()

        frameTitle = Frame(self)
        frameTitle.pack(side=TOP, fill=X, padx=20, pady=5)

        Button(frameTitle, text="← Voltar", command=lambda: controller.show_frame("Campeonato")).pack(anchor="w")

        Label(frameTitle, text="Adicionar Partida").pack()

        frameGrid = Frame(self)
        frameGrid.pack(side=TOP, fill=X, padx=20, pady=10)

    def setIdCampeonato(self, id):
        self.id_campeonato = id