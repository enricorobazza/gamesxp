DROP TABLE IF EXISTS pessoa;
DROP TABLE IF EXISTS time;
DROP TABLE IF EXISTS jogador;
DROP TABLE IF EXISTS patrocinador;
DROP TABLE IF EXISTS jogo;
DROP TABLE IF EXISTS tipo_campeonato;
DROP TABLE IF EXISTS campeonato;
DROP TABLE IF EXISTS premiacao;
DROP TABLE IF EXISTS equipe;
DROP TABLE IF EXISTS patrocinio_equipe;
DROP TABLE IF EXISTS partida;
DROP TABLE IF EXISTS equipe_joga;
DROP TABLE IF EXISTS juiz_arbitra;
DROP TABLE IF EXISTS assistir;
DROP TABLE IF EXISTS comentario;

CREATE TABLE pessoa(
    cpf VARCHAR(11), -- talvez mudar para int?
    nome VARCHAR(100),
    rg VARCHAR(9),
    telefone VARCHAR(11),
    endereco TEXT,
    dt_nasc DATE,
    PRIMARY KEY(cpf),
    CHECK(cpf LIKE '\d{11}'),
    CHECK(rg LIKE '\d{8}[\dXx]'),
    CHECK(telefone LIKE '\d{10,11}')
); 

CREATE TABLE time(
    sigla VARCHAR(5),
    nome VARCHAR(50),
    fundador VARCHAR(50),
    PRIMARY KEY(sigla)
);

CREATE TABLE jogador(
    gamertag VARCHAR(50),
    time VARCHAR(5) NOT NULL,
    cpf VARCHAR(11),
    PRIMARY KEY(gamertag),
    UNIQUE(cpf),
    FOREIGN KEY(cpf) REFERENCES pessoa(cpf) ON DELETE CASCADE,
    FOREIGN KEY(time)   REFERENCES time(sigla) ON DELETE CASCADE
);

CREATE TABLE patrocinador(
    patrocinador VARCHAR(50),
    jogador VARCHAR(50),
    quantia FLOAT,
    PRIMARY KEY(patrocinador, jogador),
    FOREIGN KEY(jogador) REFERENCES jogador(gamertag) ON DELETE CASCADE,
    CHECK(quantia >= 0)
);

CREATE TABLE jogo(
    nome VARCHAR(100),
    desenvolvedor VARCHAR(50),
    versao VARCHAR(10),
    PRIMARY KEY(nome),
    FOREIGN KEY(jogo)   REFERENCES jogo(nome) ON DELETE CASCADE
);

CREATE TABLE tipo_campeonato(
    jogo VARCHAR(100),
    nome VARCHAR(50),
    qtd_equipes INT,
    tipo_pontuacao VARCHAR(30),
    tamanho_equipes INT,
    PRIMARY KEY(jogo, nome)
);

CREATE TABLE campeonato(
    id SERIAL,
    jogo VARCHAR(100),
    tipo_campeonato VARCHAR(50),
    dt_inicio TIMESTAMP,
    dt_termino TIMESTAMP,
    PRIMARY KEY(id),
    UNIQUE(jogo, tipo_campeonato, dt_inicio),
    FOREIGN KEY(jogo, tipo_campeonato) REFERENCES tipo_campeonato(jogo, nome)
);

CREATE TABLE premiacao(
    id_campeonato INT,
    colocacao INT,
    premio text,
    PRIMARY KEY(id_campeonato, colocacao),
    FOREIGN KEY(id_campeonato) REFERENCES campeonato(id)
);

CREATE TABLE equipe(
    id SERIAL,
    time VARCHAR(5),
    id_campeonato INT,
    PRIMARY KEY(id),
    UNIQUE(time, id_campeonato),
    FOREIGN KEY(time) REFERENCES time(sigla),
    FOREIGN KEY(id_campeonato) REFERENCES campeonato(id)
);

CREATE TABLE patrocinio_equipe(
    patrocinador VARCHAR(50),
    id_equipe INT,
    quantia FLOAT,
    PRIMARY KEY(patrocinador, id_equipe),
    FOREIGN KEY(id_equipe) REFERENCES equipe(id),
    CHECK(quantia >= 0)
);

-- Foi criado id pra partida, pra facilitar
CREATE TABLE partida(
    id SERIAL,
    data TIMESTAMP,
    local VARCHAR(100),
    id_campeonato INT,
    PRIMARY KEY(id),
    UNIQUE(data, local),
    FOREIGN KEY(id_campeonato) REFERENCES campeonato(id)
);

CREATE TABLE equipe_joga(
    id_equipe INT,
    id_partida INT,
    colocacao INT,
    PRIMARY KEY(id_equipe, id_partida),
    UNIQUE(id_partida, colocacao),
    FOREIGN KEY(id_equipe) REFERENCES equipe(id),
    FOREIGN KEY(id_partida) REFERENCES partida(id)
);

-- Olhar observação da professora
CREATE TABLE juiz_arbitra(
    id_partida INT,
    juiz VARCHAR(11),
    PRIMARY KEY(id_partida, juiz),
    FOREIGN KEY(id_partida) REFERENCES partida(id),
    FOREIGN KEY(juiz) REFERENCES pessoa(cpf)
);

CREATE TABLE assistir(
    id SERIAL,
    email VARCHAR(100),
    id_partida INT,
    PRIMARY KEY(id),
    UNIQUE(email, id_partida),
    FOREIGN KEY(id_partida) REFERENCES partida(id)
);

CREATE TABLE comentario(
    id_assistir INT,
    horario TIMESTAMP,
    texto TEXT,
    PRIMARY KEY(id_assistir, horario),
    FOREIGN KEY(id_assistir) REFERENCES assistir(id)
);