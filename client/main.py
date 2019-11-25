from connect import Connection
from dao.pessoa import PessoaDAO
from model.pessoa import Pessoa
from dao.campeonato import CampeonatoDAO

def insertTime():
    print("Time")


conn = Connection()
pessoaDao = PessoaDAO(conn)
campeonatoDao = CampeonatoDAO(conn)

while True:
    op = int(input("Digite sua opcao: "))
    if(op == 1):
        break
    elif(op == 3): 
        insertTime()
    elif(op == 2):
        conn.listAllPlayers()
    elif(op == 4):
        enrico = Pessoa("47043508860","Enrico Robazza", "453409192","981947929","Meu endereco", "1997-03-31")
        pessoaDao.delete(enrico.cpf)
        pessoaDao.insert(enrico)
        print("%s inserido"%(enrico.nome))
    elif(op == 5):
        cpf = input("Digite o cpf a procurar: ")
        pessoa = pessoaDao.findPessoaByCpf(cpf)
        if(pessoa is not None):
            print(pessoa.nome)
        else:
            print("Não encontrado!!")
    elif(op == 6):
        conn.testReturn()
    elif(op == 7):
        campeonatoDao.listAll()
