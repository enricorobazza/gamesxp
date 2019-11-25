from tkinter import *
from tkinter import ttk
from connect import Connection
from dao.time import TimeDAO
from dao.campeonato import CampeonatoDAO
from dao.equipe import EquipeDAO
from model.equipe import Equipe
import numpy as np

class AddEquipe(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        self.controller = controller
        conn = Connection()

        self.timeDao = TimeDAO(conn)
        self.campeonatoDao = CampeonatoDAO(conn)
        self.equipeDao = EquipeDAO(conn)

        frameTitle = Frame(self)
        frameTitle.pack(side=TOP, fill=X, padx=20, pady=5)

        Button(frameTitle, text="← Voltar", command=lambda: controller.show_frame("Campeonato")).pack(anchor="w")

        Label(frameTitle, text="Adicionar Equipe", font=('Helvetica', 16, 'bold')).pack()

        mainFrame = Frame(self)
        mainFrame.pack(side = TOP, fill=X, padx=20, pady=10)

        self.cbTimes = ttk.Combobox(mainFrame)
        self.cbTimes.pack()
        self.cbTimes.bind("<<ComboboxSelected>>", self.selectTime)

        Label(mainFrame, text="Jogadores",font=('Helvetica', 14, 'bold') ).pack(anchor="w", pady=10)

        self.jogadoresFrame = Frame(self)
        self.jogadoresFrame.pack(side = TOP, fill=X, padx=20, pady=10)

        self.jogadores = []
        self.lblJogadores = []

        self.cbJogadores = ttk.Combobox(mainFrame)

        self.btnAddJogador = Button(mainFrame, text="Adicionar Jogador", command = self.addJogador)
        # self.cbJogadores.bind("<<ComboboxSelected>>", self.selectTime)

        bottomFrame = Frame(self)
        bottomFrame.pack(side = TOP, fill=X, padx=20, pady=10)

        Button(bottomFrame, text="Criar Equipe", command = self.criarEquipe).pack(pady=5)

    def criarEquipe(self):
        equipe = Equipe(self.time, self.id_campeonato)
        equipe.setJogadores(self.jogadores)
        self.equipeDao.insert(equipe)
        self.controller.get_frame("Campeonato").setIdCampeonato(self.id_campeonato)
        self.controller.show_frame("Campeonato")

    def resetScreen(self):
        self.cbTimes.set('')
        self.cbJogadores.set('')
        self.cbJogadores.pack_forget()
        self.btnAddJogador.pack_forget()
        for jogador in self.lblJogadores:
            jogador.destroy()
        self.jogadores = []
        self.lblJogadores = []

    def selectTime(self, pos):
        self.time = self.cbTimes.get()
        self.cbJogadores.pack(anchor="w", side=LEFT)
        self.btnAddJogador.pack(side=LEFT)
        jogadores = self.timeDao.getJogadores(self.time)
        self.cbJogadoresOptions = []
        for jogador in jogadores:
            self.cbJogadoresOptions.append(jogador[0])
        
        self.cbJogadores["value"] = self.cbJogadoresOptions

    def addJogador(self):
        jogador = self.cbJogadores.get()
        self.cbJogadores.set('')
        self.cbJogadoresOptions.remove(jogador)
        self.cbJogadores["value"] = self.cbJogadoresOptions

        lblJogador = Label(self.jogadoresFrame, text=jogador)
        lblJogador.pack(anchor="w")

        self.lblJogadores.append(lblJogador)
        self.jogadores.append(jogador)

        if(len(self.jogadores) >= self.tamanho_equipes):
            self.cbJogadores.pack_forget()
            self.btnAddJogador.pack_forget()


    def setIdCampeonato(self, id):
        self.id_campeonato = id
        self.tamanho_equipes = self.campeonatoDao.getTamEquipes(id)

        times = self.timeDao.getAllNotInCampeonato(self.id_campeonato)
        cbTimesOptions = []
        for time in times:
            cbTimesOptions.append(time[0])

        self.cbTimes["value"] = cbTimesOptions