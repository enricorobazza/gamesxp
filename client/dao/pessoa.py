from model.pessoa import Pessoa

class PessoaDAO:
    def __init__(self, conn):
        self.conn = conn

    def insert(self, pessoa):
        self.conn.execute(
            "INSERT INTO pessoa VALUES('%s', '%s', '%s', '%s', '%s', '%s')"
            %(pessoa.cpf, pessoa.nome, pessoa.rg, pessoa.telefone, pessoa.endereco, pessoa.dt_nasc))

    def update(self, pessoa):
        self.conn.execute(
            "UPDATE FROM pessoa SET nome = '%s', rg = '%s', telefone = '%s', endereco = '%s', dt_nasc = '%s' WHERE cpf = '%s'" %(pessoa.nome, pessoa.rg, pessoa.telefone, pessoa.endereco, pessoa.dt_nasc, pessoa.cpf))

    def delete(self, cpf):
        self.conn.execute("DELETE FROM pessoa WHERE cpf = '%s'"%(cpf))

    def findPessoaByCpf(self, cpf):
        query = "SELECT * FROM pessoa WHERE cpf = '%s'"%(cpf)
        self.conn.execute(query)
        r = self.conn.fetchone()
        if(r == None):
            return r
        return Pessoa(r[0], r[1], r[2], r[3], r[4], r[5].strftime("%Y-%m-%d"))