from model.partida import Partida

class PartidaDAO:
    def __init__(self, conn):
        self.conn = conn

    def getEquipes(self, id):
        self.conn.execute("SELECT ej.id_equipe, e.time FROM equipe_joga ej INNER JOIN equipe e ON(e.id = ej.id_equipe) WHERE ej.id_partida = "+str(id))
        return self.conn.fetchall()

    def insert(self, partida):
        id = self.conn.insertID("INSERT INTO partida(data, local, id_campeonato) VALUES(TO_TIMESTAMP('%s', 'DD/MM/YYYY HH24:MI'), '%s', %s) RETURNING id" 
        % (partida.data, partida.local ,partida.id_campeonato))
        partida.id = id

        for equipe in partida.equipes:
            self.conn.execute("SELECT e.id FROM equipe e INNER JOIN time t ON(t.sigla = e.time) WHERE t.sigla = '%s'"%(equipe.time))

            equipe.id = self.conn.fetchone()[0]

            self.conn.execute("INSERT INTO equipe_joga(id_equipe, id_partida, colocacao) VALUES(%s, %s, %s)"%(equipe.id, id, equipe.colocacao))

        return partida
        


