from tkinter import *
from tkinter import ttk
from connect import Connection
from dao.time import TimeDAO
import numpy as np

class AddEquipe(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        self.controller = controller
        conn = Connection()

        self.timeDao = TimeDAO(conn)

        frameTitle = Frame(self)
        frameTitle.pack(side=TOP, fill=X, padx=20, pady=5)

        Button(frameTitle, text="← Voltar", command=lambda: controller.show_frame("Campeonato")).pack(anchor="w")

        Label(frameTitle, text="Adicionar Equipe", font=('Helvetica', 16, 'bold')).pack()

        mainFrame = Frame(self)
        mainFrame.pack(side = TOP, fill=X, padx=20, pady=10)

        times = self.timeDao.getAll()
        cbTimesOptions = []
        for time in times:
            cbTimesOptions.append(time[0])

        self.cbTimes = ttk.Combobox(mainFrame, value=cbTimesOptions)
        self.cbTimes.pack()
        self.cbTimes.bind("<<ComboboxSelected>>", self.selectTime)

        Label(mainFrame, text="Jogadores",font=('Helvetica', 14, 'bold') ).pack(anchor="w", pady=10)

        self.cbJogadores = ttk.Combobox(mainFrame)
        self.cbJogadores.pack_forget()

        self.btnAddJogador = Button(mainFrame, text="Adicionar Jogador")
        self.btnAddJogador.pack_forget()
        # self.cbJogadores.bind("<<ComboboxSelected>>", self.selectTime)

    def resetScreen(self):
        self.cbTimes.set('')
        self.cbJogadores.set('')
        self.cbJogadores.pack_forget()
        self.btnAddJogador.pack_forget()

    def selectTime(self, pos):
        self.time = self.cbTimes.get()
        self.cbJogadores.pack(anchor="w", side=LEFT)
        self.btnAddJogador.pack(side=LEFT)
        jogadores = self.timeDao.getJogadores(self.time)
        cbJogadoresOptions = []
        for jogador in jogadores:
            cbJogadoresOptions.append(jogador[0])
        
        self.cbJogadores["value"] = cbJogadoresOptions



    def setIdCampeonato(self, id):
        self.id_campeonato = id