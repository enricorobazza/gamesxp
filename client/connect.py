import psycopg2
from config import username, password

class Connection:
    def __init__(self):
        self.conn = psycopg2.connect("dbname=xgames user=%s password=%s"%(username, password))
        self.cur = self.conn.cursor()
        print("Connection started")

    def __del__(self):
        self.cur.close()
        self.conn.close()
        print("Connection finished")

    def listAllPlayers(self):
        self.cur.execute("SELECT * from jogador;")
        for jogador in self.cur.fetchall():
            print(jogador[0])

# conn = Connection()