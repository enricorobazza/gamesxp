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
        self.cursor.execute(command)
        self.connection.commit()

    def listAllPlayers(self):
        self.cursor.execute("SELECT * from pessoa;")
        for pessoa in self.cursor.fetchall():
            print(pessoa[1])

# conn = Connection()