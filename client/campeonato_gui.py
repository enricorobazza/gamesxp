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

        Button(frameTitle, text="← Voltar", command=lambda: controller.show_frame("ListCampeonatos")).pack(anchor="w")

        self.title = Label(frameTitle, text="Campeonato")
        self.title.pack()

        Label(frameTitle, text="Partidas:").pack(anchor="w")

        self.frameGrid = Frame(self)
        self.frameGrid.pack(side=TOP, fill=X, padx=20, pady=5)

        self.partidas = []

        self.frameBottom = Frame(self)
        self.frameBottom.pack(side=TOP, fill=X, padx=20, pady=10)

        Label(self.frameBottom, text="Informações").pack()

        self.vencedor = Label(self.frameBottom, text="Atual Vencedor: ")
        self.vencedor.pack(anchor="w")

        self.qtdEquipes = Label(self.frameBottom, text="Qtd equipes participantes: ")
        self.qtdEquipes.pack(anchor="w")

        Button(self.frameBottom, text="Adicionar Equipe", command = lambda: controller.show_frame("AddEquipe")).pack(pady=10)
        Button(self.frameBottom, text="Adicionar Partida", command = lambda: controller.show_frame("AddPartida")).pack(pady=5)


    def setIdCampeonato(self, id):
        self.id_campeonato = id
        name = self.campeonatoDao.getName(id)
        self.title["text"] = name
        self.loadPartidas()

        vencedor = self.campeonatoDao.getVencedor(id)
        if(vencedor is not None):
            self.vencedor["text"] = "Atual Vencedor " + vencedor[1] + ", partidas ganhas: " + str(vencedor[2])

        qtdEquipes = self.campeonatoDao.getQtdEquipes(id)
        self.qtdEquipes["text"] = "Qtd equipes participantes: " + str(qtdEquipes)

    def loadPartidas(self):
        for partida in self.partidas:
            for element in partida:
                element.destroy()

        self.partidas = []

        partidas = self.campeonatoDao.getPartidas(self.id_campeonato)
        r = 0
        for partida in partidas:
            times = ', '.join(map(lambda equipe: equipe[1], partida.equipes))
            partidaContainer = []
            partidaContainer.append(Label(self.frameGrid, text=times,borderwidth=1, relief="solid"))
            partidaContainer[0].grid(row =r, column=0,columnspan=1,sticky=W+E+N+S)

            partidaContainer.append(Label(self.frameGrid, text=partida.local,borderwidth=1, relief="solid"))
            partidaContainer[1].grid(row =r, column=1,columnspan=1,sticky=W+E+N+S)

            partidaContainer.append(Label(self.frameGrid, text=partida.data.strftime("%d/%m/%Y %H:%M"),borderwidth=1, relief="solid"))
            partidaContainer[2].grid(row =r, column=2,columnspan=1,sticky=W+E+N+S)

            self.partidas.append(partidaContainer)

            r+=1