from tkinter import *
from tkinter import ttk
import datetime

from connect import Connection
from dao.equipe import EquipeDAO
from dao.partida import PartidaDAO
from model.partida import Partida
from model.equipe import Equipe

class AddPartida(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        self.controller = controller
        conn = Connection()

        self.equipeDao = EquipeDAO(conn)
        self.partidaDao = PartidaDAO(conn)

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

        self.cbEquipes = ttk.Combobox(frameAddEquipe)
        self.cbEquipes.pack(anchor="w", side=LEFT)

        Label(frameAddEquipe, text="Colocação: ").pack(anchor="w", side=LEFT)

        self.cbColocacao = ttk.Combobox(frameAddEquipe)
        self.cbColocacao.pack(anchor="w", side=LEFT)

        Button(frameAddEquipe, text="Adicionar Equipe", command = self.addEquipe).pack(anchor="w", side=LEFT)

        self.frameEquipes = Frame(mainFrame)
        self.frameEquipes.pack(anchor="w", pady=10)

        Label(self.frameEquipes, text="Equipes:",font=('Helvetica', 14, 'bold')).pack(anchor="w")

        self.lblEquipes = []
        self.equipes = []

        frameBottom = Frame(self)
        frameBottom.pack(side=TOP, fill=X, padx=20, pady=5)

        Button(frameBottom, text="Criar partida", command=self.criarPartida).pack()

        self.lblErro = Label(frameBottom, text="", fg="red")

    def validate_date(self, date):
        try:
            datetime.datetime.strptime(date, '%d/%m/%Y %H:%M')
            return 1
        except ValueError:
            return 0

    def criarPartida(self):
        if(len(self.equipes) == 0):
            self.lblErro["text"] = "Adicione pelo menos uma equipe"
            self.lblErro.pack()
            return
        elif(self.txtData.get() == ""):
            self.lblErro["text"] = "Adicione uma Data"
            self.lblErro.pack()
            return
        elif(self.txtLocal.get() == ""):
            self.lblErro["text"] = "Adicione um Local"
            self.lblErro.pack()
            return  
        elif(not self.validate_date(self.txtData.get())):
            self.lblErro["text"] = "Adicione uma data no formato: DD/MM/YYYY HH:mm"
            self.lblErro.pack()
            return

        partida = Partida(self.txtData.get(), self.txtLocal.get(), self.id_campeonato)
        partida.setEquipes(self.equipes)
        self.partidaDao.insert(partida)
        self.controller.get_frame("Campeonato").setIdCampeonato(self.id_campeonato)
        self.controller.show_frame("Campeonato")
        
    def addEquipe(self):
        equipe = self.cbEquipes.get()
        colocacao = self.cbColocacao.get()

        self.cbEquipes.set('')
        self.cbEquipesOptions.remove(equipe)
        self.cbEquipes["value"] = self.cbEquipesOptions

        self.cbColocacao.set('')
        self.cbColocacaoOptions.remove(colocacao)
        self.cbColocacao["value"] = self.cbColocacaoOptions

        lblEquipe = Label(self.frameEquipes, text="%s(%sº lugar)"%(equipe, colocacao))
        lblEquipe.pack(anchor="w")

        equipe_obj = Equipe(equipe, self.id_campeonato)
        equipe_obj.setColocacao(colocacao)

        self.lblEquipes.append(lblEquipe)
        self.equipes.append(equipe_obj)

    def resetScreen(self):
        for label in self.lblEquipes:
            label.destroy()
        self.lblEquipes = []
        self.equipes = []
        self.cbEquipes.set('')
        self.txtData.delete(0, 'end')
        self.txtLocal.delete(0, 'end')
        self.lblErro.pack_forget()

    def setIdCampeonato(self, id):
        self.id_campeonato = id
        equipes = self.equipeDao.getAllFromCampeonato(id)
        self.cbEquipesOptions = []
        self.cbColocacaoOptions = []
        i = 1
        for equipe in equipes:
            self.cbEquipesOptions.append(equipe[0])
            self.cbColocacaoOptions.append(str(i))
            i+=1

        self.cbEquipes["value"] = self.cbEquipesOptions
        self.cbColocacao["value"] = self.cbColocacaoOptions
