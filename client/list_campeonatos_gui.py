from tkinter import *
from dao.campeonato import CampeonatoDAO
from connect import Connection
from functools import partial

class ListCampeonatos(Frame):
    def verCampeonato(self, id):
        # print("ID do campeonato: "+str(id))
        self.controller.get_frame("Campeonato").setIdCampeonato(id)
        self.controller.show_frame("Campeonato")


    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        self.controller = controller
        conn = Connection()
        campeonatoDao = CampeonatoDAO(conn)
        campeonatos = campeonatoDao.listAll()

        frameTitle = Frame(self)
        frameTitle.pack(side=TOP, fill=X, padx=20, pady=5)

        frameGrid = Frame(self)
        frameGrid.pack(side=TOP, fill=X, padx=20, pady=10)

        title = Label(frameTitle,text="Campeonatos", font=('Helvetica', 16, 'bold')).pack()
        self.campeonatos = []
        h = 2
        for campeonato in campeonatos:
            campeonatoWidgets = []

            label = Label(frameGrid, text=campeonato[2],borderwidth=1, relief="solid")
            label.grid(row=h,column=1,columnspan=1,sticky=W+E+N+S)
            campeonatoWidgets.append(label)

            btnVerCampeonato = Button(frameGrid, text="Ver Campeonato", command= partial(self.verCampeonato, campeonato[0]))
            btnVerCampeonato.grid(row=h, column=3, columnspan=1,sticky=W+E+N+S)
            campeonatoWidgets.append(btnVerCampeonato)


            self.campeonatos.append(campeonatoWidgets)
            h += 1
