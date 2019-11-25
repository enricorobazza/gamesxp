import psycopg2
from config import username, password

class Connection:
    def __init__(self):
        self.connection = psycopg2.connect("dbname=gamexp user=%s password=%s"%(username, password))
        self.cursor = self.connection.cursor()
        print("Connection started")

    def __del__(self):
        self.cursor.close()
        self.connection.close()
        print("Connection finished")

    def execute(self, command):
        try:
            self.cursor.execute(command)
        except psycopg2.Error as e:
            print(e.pgerror)
        self.connection.commit()

    def insertID(self, command):
        self.cursor.execute(command)
        self.connection.commit()
        return self.cursor.fetchone()[0]

    def fetchone(self):
        return self.cursor.fetchone()

    def fetchall(self):
        return self.cursor.fetchall()

    def listAllPlayers(self):
        self.cursor.execute("SELECT * from pessoa;")
        for pessoa in self.cursor.fetchall():
            print(pessoa[1])

    def testReturn(self):
        self.cursor.execute("INSERT INTO equipe(time, id_campeonato) VALUES('KBM',1) RETURNING id")
        print(self.cursor.fetchone()[0])
