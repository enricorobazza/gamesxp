class Equipe:
    def __init__(self, time="", id_campeonato=-1, id=-1):
        self.time = time
        self.id_campeonato = id_campeonato
        self.id = id

    def setJogadores(self, jogadores):
        self.jogadores = jogadores

    def setColocacao(self, colocacao):
        self.colocacao = colocacao
