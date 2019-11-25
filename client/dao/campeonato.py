from dao.partida import PartidaDAO
from model.partida import Partida

class CampeonatoDAO:
    def __init__(self, conn):
        self.conn = conn
        self.partidaDao = PartidaDAO(conn)

    def listAll(self):
        self.conn.execute("SELECT * FROM campeonato;")
        return self.conn.fetchall()

    def getName(self, id):
        self.conn.execute("SELECT jogo, tipo_campeonato, dt_inicio from campeonato where id = "+str(id))
        result = self.conn.fetchone()
        return result[0] + ": " + result[1] + " " + result[2].strftime("%d/%m/%Y")

    def getPartidas(self, id):
        self.conn.execute("SELECT * from partida where id_campeonato = "+str(id))
        result = self.conn.fetchall()
        partidas = []
        for p in result:
            partida = Partida(p[1], p[2], p[3])
            partida.setEquipes(self.partidaDao.getEquipes(p[0]))
            partida.setId(p[0])
            partidas.append(partida)
        return partidas

    def getVencedor(self, id):
        self.conn.execute("SELECT ej.id_equipe, e.time, COUNT(*) FROM equipe_joga ej INNER JOIN partida p ON(p.id = ej.id_partida) INNER JOIN equipe e ON(e.id = ej.id_equipe) WHERE ej.colocacao = 1 AND p.id_campeonato = "+str(id) + " GROUP BY(ej.id_equipe, e.time) ORDER BY(COUNT(*));")

        return self.conn.fetchone()

    def getQtdEquipes(self, id):
        self.conn.execute("SELECT count(*) from equipe where id_campeonato = "+str(id)+" group by(id_campeonato)")
        return self.conn.fetchone()[0]

    def getQtdMaxEquipes(self, id):
        self.conn.execute("SELECT tc.qtd_equipes from campeonato c INNER JOIN tipo_campeonato tc ON(tc.nome = c.tipo_campeonato)WHERE c.id = "+str(id))
        return self.conn.fetchone()[0]
