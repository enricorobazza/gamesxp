class TimeDAO:
    def __init__(self, conn):
        self.conn = conn

    def getAll(self):
        self.conn.execute("SELECT * FROM time")
        return self.conn.fetchall()


    def getJogadores(self, sigla):
        self.conn.execute("SELECT gamertag FROM jogador WHERE time = '"+sigla+"'")
        return self.conn.fetchall()