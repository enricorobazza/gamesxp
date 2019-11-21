from connect import Connection

def insertTime():
    print("Time")


conn = Connection()

while True:
    op = int(input("Digite sua opcao: "))
    if(op == 4):
        break
    elif(op == 3): 
        insertTime()
    elif(op == 2):
        conn.listAllPlayers()
    elif(op == 1):
        print(op)
