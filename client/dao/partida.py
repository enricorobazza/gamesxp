from model.partida import Partida

class PartidaDAO:
    def __init__(self, conn):
        self.conn = conn

    def getEquipes(self, id):
        self.conn.execute("SELECT ej.id_equipe, e.time FROM equipe_joga ej INNER JOIN equipe e ON(e.id = ej.id_equipe) WHERE ej.id_partida = "+str(id))
        return self.conn.fetchall()

    def insert(self, equipe):
        id = self.conn.insertID("INSERT INTO equipe(time, id_campeonato) VALUES('%s', %s) RETURNING id" 
        % (equipe.time, equipe.id_campeonato))
        equipe.id = id

        for jogador in equipe.jogadores:
            self.conn.execute("INSERT INTO jogador_equipe(id_equipe, gamertag) VALUES("+str(id)+",'"+jogador+"')")

        return equipe

    def insert(self, partida):
        id = self.conn.insertID("INSERT INTO partida(data, local, id_campeonato) VALUES('%s', '%s', %s) RETURNING id" 
        % (partida.data, partida.local ,partida.id_campeonato))
        partida.id = id

        for equipe in partida.equipes:
            self.conn.execute("INSERT INTO equipe_joga(id_equipe, id_partida, colocacao) VALUES(%s, %s, %s)"%(equipe.id, id, equipe.colocacao))

        return partida
        


