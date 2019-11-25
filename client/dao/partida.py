from model.partida import Partida

class PartidaDAO:
    def __init__(self, conn):
        self.conn = conn

    def getEquipes(self, id):
        self.conn.execute("SELECT ej.id_equipe, e.time FROM equipe_joga ej INNER JOIN equipe e ON(e.id = ej.id_equipe) WHERE ej.id_partida = "+str(id))
        return self.conn.fetchall()


