class JogoDAO:
    def __init__(self, conn):
        self.conn = conn

    def getTipoMaisAssistido(self):
        self.conn.execute("with assistidos as(select tc.nome, tc.jogo, count(*) as qtd from partida p inner join assistir a on(a.id_partida = p.id) inner join campeonato c on(c.id = p.id_campeonato) inner join tipo_campeonato tc on(tc.jogo = c.jogo and tc.nome = c.tipo_campeonato) group by(tc.nome, tc.jogo)), max_assistidos as (select jogo, max(qtd) as max_qtd from assistidos group by(jogo)) select a.nome, a.jogo, a.qtd as visualizacoes from assistidos a inner join max_assistidos ma on(a.jogo = ma.jogo and a.qtd = ma.max_qtd);")

        return self.conn.fetchall()

        
