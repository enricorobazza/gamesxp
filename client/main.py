from connect import Connection
from dao.pessoa import PessoaDAO

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
        pessoaDao = PessoaDAO(conn)
        pessoaDao.delete("47043508860")
        pessoaDao.insert("47043508860","Enrico Robazza", "453409192","981947929","Meu endereco", "1997-03-31")
        print("Enrico inserido")
