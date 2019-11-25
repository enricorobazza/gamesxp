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
        self.conn.execute("SELECT ej.id_equipe, e.time, COUNT(*) FROM equipe_joga ej INNER JOIN partida p ON(p.id = ej.id_partida) INNER JOIN equipe e ON(e.id = ej.id_equipe) WHERE ej.colocacao = 1 AND p.id_campeonato = "+str(id) + " GROUP BY(ej.id_equipe, e.time) ORDER BY(COUNT(*)) DESC;")

        return self.conn.fetchone()


    def getMaiorJogadorVencedor(self, id):
        self.conn.execute("with vitoriosos as(SELECT ej.id_equipe, p.id_campeonato, count(*) as qtd_vitorias FROM equipe_joga ej INNER JOIN partida p ON(p.id = ej.id_partida) WHERE ej.colocacao = 1 GROUP BY(ej.id_equipe,p.id_campeonato)), max_vitoriosos as(select id_campeonato, max(qtd_vitorias) as max_vitorias from vitoriosos group by(id_campeonato)), vencedores_campeonatos as (select v.id_equipe, v.id_campeonato, v.qtd_vitorias from vitoriosos v inner join max_vitoriosos mv ON(v.id_campeonato = mv.id_campeonato and v.qtd_vitorias = mv.max_vitorias) order by(v.id_campeonato))select je.gamertag, count(*) from vencedores_campeonatos vc inner join jogador_equipe je on(je.id_equipe = vc.id_equipe)group by(je.gamertag) order by(count(*)) DESC;")

        return self.conn.fetchone()


    def getVencedorBasedOnWeight(self, id, weights=[3,2,1]):
        self.conn.execute("SELECT ej.id_equipe, e.time, p.id_campeonato, SUM(CASE WHEN ej.colocacao = 1 THEN %s ELSE CASE WHEN ej.colocacao = 2 THEN %s ELSE CASE WHEN ej.colocacao = 3 THEN %s ELSE 0 END END END) as pontuacao FROM equipe_joga ej INNER JOIN partida p ON(p.id = ej.id_partida) INNER JOIN equipe e ON(e.id = ej.id_equipe) WHERE p.id_campeonato = %s GROUP BY(p.id_campeonato, ej.id_equipe, e.time) ORDER BY(pontuacao) DESC"%(weights[0], weights[1], weights[2], id))

        return self.conn.fetchone()

    def getQtdEquipes(self, id):
        self.conn.execute("SELECT count(*) from equipe where id_campeonato = "+str(id)+" group by(id_campeonato)")
        return self.conn.fetchone()[0]

    def getQtdMaxEquipes(self, id):
        self.conn.execute("SELECT tc.qtd_equipes from campeonato c INNER JOIN tipo_campeonato tc ON(tc.nome = c.tipo_campeonato)WHERE c.id = "+str(id))
        return self.conn.fetchone()[0]

    def getTamEquipes(self, id):
        self.conn.execute("SELECT tc.tamanho_equipes from campeonato c INNER JOIN tipo_campeonato tc ON(tc.nome = c.tipo_campeonato)WHERE c.id = "+str(id))
        return self.conn.fetchone()[0]
