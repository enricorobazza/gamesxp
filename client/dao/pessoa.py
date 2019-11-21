class PessoaDAO:
    def __init__(self, conn):
        self.conn = conn

    def insert(self, cpf, nome, rg, telefone, endereco, dt_nasc):
        self.conn.execute(
            "INSERT INTO pessoa VALUES('%s', '%s', '%s', '%s', '%s', '%s')"
            %(cpf, nome, rg, telefone, endereco, dt_nasc))
        # self.conn.connection.commit()

    def delete(self, cpf):
        self.conn.execute("DELETE FROM pessoa WHERE cpf = '%s'"%(cpf))