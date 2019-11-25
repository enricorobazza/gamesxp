class CampeonatoDAO:
    def __init__(self, conn):
        self.conn = conn

    def listAll(self):
        self.conn.execute("SELECT * FROM campeonato;")
        return self.conn.fetchall()

    def getName(self, id):
        self.conn.execute("SELECT jogo, tipo_campeonato, dt_inicio from campeonato where id = "+str(id))
        result = self.conn.fetchone()
        return result[0] + ": " + result[1] + " " + result[2].strftime("%d/%m/%Y")