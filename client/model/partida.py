class Partida:
    def __init__(self, data=None, local="", id_campeonato =-1):
        self.data = data
        self.local = local
        self.id_campeonato = id_campeonato

    def setEquipes(self, equipes):
        self.equipes = equipes

    def setId(self, id):
        self.id = id