from tkinter import *
from tkinter import ttk
from connect import Connection
from dao.equipe import EquipeDAO

class AddPartida(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        self.controller = controller
        conn = Connection()

        self.equipeDao = EquipeDAO(conn)

        frameTitle = Frame(self)
        frameTitle.pack(side=TOP, fill=X, padx=20, pady=5)

        Button(frameTitle, text="← Voltar", command=lambda: controller.show_frame("Campeonato")).pack(anchor="w")

        Label(frameTitle, text="Adicionar Partida", font=('Helvetica', 16, 'bold')).pack()
        
        mainFrame = Frame(self)
        mainFrame.pack(side=TOP, fill=X, padx=20, pady=5)

        frameData = Frame(mainFrame)
        frameData.pack(anchor="w")

        Label(frameData, text="Data: ").pack(anchor="w", side=LEFT)
        self.txtData = Entry(frameData)
        self.txtData.pack(anchor="w", side=LEFT)

        frameLocal = Frame(mainFrame)
        frameLocal.pack(anchor="w")

        Label(frameLocal, text="Local: ").pack(anchor="w", side=LEFT)
        self.txtLocal = Entry(frameLocal)
        self.txtLocal.pack(anchor="w", side=LEFT)

        frameAddEquipe = Frame(mainFrame)
        frameAddEquipe.pack(anchor="w", pady=10)

        self.cbEquipes = ttk.Combobox(frameAddEquipe, value=["a","b","c"])
        self.cbEquipes.pack(anchor="w", side=LEFT)
        Label(frameAddEquipe, text="Colocação: ").pack(anchor="w", side=LEFT)
        self.txtColocacao = Entry(frameAddEquipe)
        self.txtColocacao.pack(anchor="w", side=LEFT)
        Button(frameAddEquipe, text="Adicionar Equipe", command = self.addEquipe).pack(anchor="w", side=LEFT)

        self.frameEquipes = Frame(mainFrame)
        self.frameEquipes.pack(anchor="w", pady=10)

        Label(self.frameEquipes, text="Equipes:",font=('Helvetica', 14, 'bold')).pack(anchor="w")

        self.lblEquipes = []
        self.equipes = []

        frameBottom = Frame(self)
        frameBottom.pack(side=TOP, fill=X, padx=20, pady=5)

        Button(frameBottom, text="Adicionar partida").pack()
        
    def addEquipe(self):
        equipe = self.cbEquipes.get()
        self.cbEquipes.set('')
        self.cbEquipesOptions.remove(equipe)
        self.cbEquipes["value"] = self.cbEquipesOptions

        lblEquipe = Label(self.frameEquipes, text=equipe)
        lblEquipe.pack(anchor="w")

        self.lblEquipes.append(lblEquipe)
        self.equipes.append(equipe)

    def resetScreen(self):
        for label in self.lblEquipes:
            label.destroy()
        self.lblEquipes = []
        self.equipes = []
        self.cbEquipes.set('')

    def setIdCampeonato(self, id):
        self.id_campeonato = id
        equipes = self.equipeDao.getAllFromCampeonato(id)
        self.cbEquipesOptions = []
        for equipe in equipes:
            self.cbEquipesOptions.append(equipe[0])
        self.cbEquipes["value"] = self.cbEquipesOptions
