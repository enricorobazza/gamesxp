from model.equipe import Equipe

class EquipeDAO:
    def __init__(self, conn):
        self.conn = conn

    def insert(self, equipe):
        id = self.conn.insertID("INSERT INTO equipe(time, id_campeonato) VALUES('%s', %s) RETURNING id" 
        % (equipe.time, equipe.id_campeonato))
        equipe.id = id

        for jogador in equipe.jogadores:
            self.conn.execute("INSERT INTO jogador_equipe(id_equipe, gamertag) VALUES("+str(id)+",'"+jogador+"')")

        return equipe


