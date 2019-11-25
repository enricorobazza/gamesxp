class TimeDAO:
    def __init__(self, conn):
        self.conn = conn

    def getAll(self):
        self.conn.execute("SELECT * FROM time")
        return self.conn.fetchall()

    def getAllNotInCampeonato(self, id_campeonato):
        self.conn.execute("select * from time where sigla not in(select time from equipe where id_campeonato = "+str(id_campeonato)+")")
        return self.conn.fetchall()

    def getJogadores(self, sigla):
        self.conn.execute("SELECT gamertag FROM jogador WHERE time = '"+sigla+"'")
        return self.conn.fetchall()

    def getJogadoresNotInCampeonato(self, sigla, id_campeonato):
        self.conn.execute("select gamertag from jogador where gamertag not in(select je.gamertag from jogador_equipe je inner join equipe e on(e.id = je.id_equipe) where e.id_campeonato = "+str(id_campeonato)+") and time = '"+sigla+"'")
        return self.conn.fetchall()

# select * from time where sigla not in(select time from equipe where id_campeonato = 1);


# select gamertag from jogador where time = 'paiN' and gamertag not in(select gamertag from jogador_equipe);

# select gamertag from jogador where gamertag not in(select je.gamertag from jogador_equipe je inner join equipe e on(e.id = je.id_equipe) where e.id_campeonato = 1);


# select je.gamertag, e.id_campeonato from jogador_equipe je inner join equipe e on(e.id = je.id_equipe);