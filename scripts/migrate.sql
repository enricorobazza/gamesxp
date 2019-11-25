-- Desconectar todas as conexões atuais com o DB 
SELECT
   pg_terminate_backend (pg_stat_activity.pid)
FROM
   pg_stat_activity
WHERE
   pg_stat_activity.datname = 'gamexp';

-- Drop database, create and connect
DROP DATABASE IF EXISTS gamexp;
CREATE DATABASE gamexp;
\c gamexp

-- Tables
CREATE TABLE pessoa(
    cpf VARCHAR(11),
    nome VARCHAR(100),
    rg VARCHAR(9),
    telefone VARCHAR(11),
    endereco TEXT,
    dt_nasc DATE,
    PRIMARY KEY(cpf),
    CHECK(cpf ~* '\d{11}'),
    CHECK(rg ~* '\d{8}[\dXx]'),
    CHECK(telefone ~* '\d{10,11}')
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

CREATE TABLE patrocinador_jogador(
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
    PRIMARY KEY(nome)
);

CREATE TABLE tipo_campeonato(
    jogo VARCHAR(100),
    nome VARCHAR(50),
    qtd_equipes INT,
    tipo_pontuacao VARCHAR(30),
    tamanho_equipes INT,
    PRIMARY KEY(jogo, nome),
    FOREIGN KEY(jogo) REFERENCES jogo(nome) ON DELETE CASCADE
);

CREATE TABLE campeonato(
    id SERIAL,
    jogo VARCHAR(100),
    tipo_campeonato VARCHAR(50),
    dt_inicio TIMESTAMP,
    dt_termino TIMESTAMP,
    PRIMARY KEY(id),
    UNIQUE(jogo, tipo_campeonato, dt_inicio),
    FOREIGN KEY(jogo, tipo_campeonato) REFERENCES tipo_campeonato(jogo, nome) ON DELETE CASCADE,
    CHECK(dt_termino > dt_inicio)
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
    FOREIGN KEY(time) REFERENCES time(sigla) ON DELETE CASCADE,
    FOREIGN KEY(id_campeonato) REFERENCES campeonato(id) ON DELETE CASCADE
);

-- Verificar em aplicação se pertence ao time da equipe
-- Verificar em aplicação se pertence a apenas uma equipe
CREATE TABLE jogador_equipe(
    id_equipe INT,
    gamertag VARCHAR(50),
    PRIMARY KEY(id_equipe, gamertag),
    FOREIGN KEY(id_equipe) REFERENCES equipe(id) ON DELETE CASCADE,
    FOREIGN KEY(gamertag) REFERENCES jogador(gamertag) ON DELETE CASCADE
);

CREATE TABLE patrocinio_equipe(
    patrocinador VARCHAR(50),
    id_equipe INT,
    quantia FLOAT,
    PRIMARY KEY(patrocinador, id_equipe),
    FOREIGN KEY(id_equipe) REFERENCES equipe(id) ON DELETE CASCADE,
    CHECK(quantia >= 0)
);

CREATE TABLE partida(
    id SERIAL,
    data TIMESTAMP,
    local VARCHAR(100),
    id_campeonato INT,
    PRIMARY KEY(id),
    UNIQUE(data, local),
    FOREIGN KEY(id_campeonato) REFERENCES campeonato(id) ON DELETE CASCADE
);

CREATE TABLE equipe_joga(
    id_equipe INT,
    id_partida INT,
    colocacao INT,
    PRIMARY KEY(id_equipe, id_partida),
    UNIQUE(id_partida, colocacao),
    FOREIGN KEY(id_equipe) REFERENCES equipe(id) ON DELETE CASCADE,
    FOREIGN KEY(id_partida) REFERENCES partida(id) ON DELETE CASCADE
);

-- Olhar observação da professora
CREATE TABLE juiz_arbitra(
    id_partida INT,
    juiz VARCHAR(11),
    PRIMARY KEY(id_partida, juiz),
    FOREIGN KEY(id_partida) REFERENCES partida(id) ON DELETE CASCADE,
    FOREIGN KEY(juiz) REFERENCES pessoa(cpf) ON DELETE CASCADE
);

CREATE TABLE assistir(
    id SERIAL,
    email VARCHAR(100),
    id_partida INT,
    PRIMARY KEY(id),
    UNIQUE(email, id_partida),
    FOREIGN KEY(id_partida) REFERENCES partida(id) ON DELETE CASCADE
);

CREATE TABLE comentario(
    id_assistir INT,
    horario TIMESTAMP,
    texto TEXT,
    PRIMARY KEY(id_assistir, horario),
    FOREIGN KEY(id_assistir) REFERENCES assistir(id) ON DELETE CASCADE
);