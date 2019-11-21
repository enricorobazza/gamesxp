/* >>>>>>>>TEMOS QUE DAR UMA ATENÇAO PARA ALGUMAS COISAS :

- COMO SERA O FORMATO CPF E RG, SE TERA . OU -
- NO CASO DO ATRIBUTO DO TIPO SERIAL, VER COM GERAR ELE, PARA USAR NA POPULAÇÃO SEGUINTE.. EM AGUNS CASOS COLOQUEI 'XXX'
- VER COMO PEGAR O HORARIO LOCAL NO CASO DO COMENTARIO


*/

/* DADOS PARA TABELA PESSOA */

INSERT INTO pessoa (cpf, nome, rg, telefone, endereco, dt_nasc)
	VALUES ('40056029861', 'joao', '100002013', '33782534', 'avenida são carlos, nº100, são carlos - SP', TO_DATE('1995/09/02', 'YYYY/MM/DD'));

INSERT INTO pessoa (cpf, nome, rg, telefone, endereco, dt_nasc)
	VALUES ('50056029861', 'luiz', '151002013', '33782534', 'rua xv de novembro, nº356, são carlos - SP', TO_DATE('1994/11/02', 'YYYY/MM/DD'));
	
INSERT INTO pessoa (cpf, nome, rg, telefone, endereco, dt_nasc)
	VALUES ('60056029861', 'fernando', '122002013', '33782534', 'rua bruno lazarini, nº36, ibate- SP', TO_DATE('2000/10/02', 'YYYY/MM/DD'));
	
INSERT INTO pessoa (cpf, nome, rg, telefone, endereco, dt_nasc)
	VALUES ('70056029861', 'joao pedro', '191002013', '33782534', 'avenida paulista, nº100, são paulo - SP', TO_DATE('2000/05/02', 'YYYY/MM/DD'));
	
INSERT INTO pessoa (cpf, nome, rg, telefone, endereco, dt_nasc)
	VALUES ('80056029861', 'arnaldo', '255002013', '33782534', 'avenida getulio vargas, nº1560, frutal - MG', TO_DATE('1996/07/02', 'YYYY/MM/DD'));
	
INSERT INTO pessoa (cpf, nome, rg, telefone, endereco, dt_nasc)
	VALUES ('90056029861', 'thiago', '270002013', '33782534', 'avenida são carlos, nº100, são carlos - sp', TO_DATE('1995/02/02', 'YYYY/MM/DD'));
	
INSERT INTO pessoa (cpf, nome, rg, telefone, endereco, dt_nasc)
	VALUES ('10056029861', 'paulo', '352562013', '33782534', 'avenida são carlos, nº100, são carlos - SP', TO_DATE('1997/03/02', 'YYYY/MM/DD'));
	
INSERT INTO pessoa (cpf, nome, rg, telefone, endereco, dt_nasc)
	VALUES ('20056029861', 'jose', '207862013', '33782534', 'rua 7 de setembro, nº975, são carlos - SP', TO_DATE('1994/03/02', 'YYYY/MM/DD'));
	
INSERT INTO pessoa (cpf, nome, rg, telefone, endereco, dt_nasc)
	VALUES ('30056029861', 'carlos', '200352013', '33782534', 'avenida do estado, nº1500, araraquara - SP', TO_DATE('1999/11/02', 'YYYY/MM/DD'));
	
INSERT INTO pessoa (cpf, nome, rg, telefone, endereco, dt_nasc)
	VALUES ('10556035061', 'pedro', '151352013', '33782534', 'rua savoie, nº10, são paulo - sp', TO_DATE('1995/09/02', 'YYYY/MM/DD'));


----------------------------------------------------------------------------------------------------------------------------------------------------

/* DADOS PARA TABELA TIME */

INSERT INTO TIME (sigla, nome, fundador) 
	VALUES ('paiN', 'painN Gaming', 'joao da silva');
INSERT INTO TIME (sigla, nome, fundador) 
	VALUES ('CNB', 'CNB eSports Club', 'Matheus Vidal');
INSERT INTO TIME (sigla, nome, fundador) 
	VALUES ('INTZ', 'INTZ E-Sports', 'Pedro Magalhães');
INSERT INTO TIME (sigla, nome, fundador) 
	VALUES ('KBM', 'Kabum eSports', 'Jorge Luiz');
INSERT INTO TIME (sigla, nome, fundador) 
	VALUES ('Keyd', 'Vivo Keyd', 'Pedro Oliveira');
INSERT INTO TIME (sigla, nome, fundador) 
	VALUES ('RED', 'RED Canids', 'Fernando');
INSERT INTO TIME (sigla, nome, fundador) 
	VALUES ('FLA', 'Flamengo eSports', 'zico');

----------------------------------------------------------------------------------------------------------------------------------------------------

/* DADOS PARA TABELA JOGADOR */


INSERT INTO jogador (gamertag, time, cpf)
    VALUES ('Yang', 'paiN', '40056029861');
INSERT INTO JOGADOR (gamertag, time, cpf)
    VALUES ('FREIRE', 'CNB', '50056029861');
INSERT INTO JOGADOR (gamertag, time, cpf)
    VALUES ('TAY', 'INTZ', '60056029861');
INSERT INTO JOGADOR (gamertag, time, cpf)
    VALUES ('WIZER', 'KBM', '70056029861');
INSERT INTO JOGADOR (gamertag, time, cpf)
    VALUES ('LEP', 'Keyd', '80056029861');
INSERT INTO JOGADOR (gamertag, time, cpf)
    VALUES ('LOOP', 'RED', '90056029861');
INSERT INTO JOGADOR (gamertag, time, cpf)
    VALUES ('ROBO', 'FLA', '10056029861');
INSERT INTO JOGADOR (gamertag, time, cpf)
    VALUES ('ASLAN', 'CNB', '20056029861');
INSERT INTO JOGADOR (gamertag, time, cpf)
    VALUES ('MINERVA', 'paiN', '30056029861');

----------------------------------------------------------------------------------------------------------------------------------------------------

/* DADOS PARA TABELA PATROCINADOR */

INSERT INTO patrocinador (patrocinador, jogador, quantia)
	VALUES ('Nestle', 'Yang', 10165);
INSERT INTO patrocinador (patrocinador, jogador, quantia)
	VALUES ('Google', 'ROBO', 15165);
INSERT INTO patrocinador (patrocinador, jogador, quantia)
	VALUES ('Kabum', 'WIZER', 1165);
	

----------------------------------------------------------------------------------------------------------------------------------------------------

/* DADOS PARA TABELA JOGO */

INSERT INTO jogo (nome, desenvolvedor, versao)
	VALUES ('League of Legends', 'RIOT Games', '9.22');
INSERT INTO jogo (nome, desenvolvedor, versao)
	VALUES ('Counter Strike Global Offensive', 'Valve', '2.0');
INSERT INTO jogo (nome, desenvolvedor, versao)
	VALUES ('Fortnite', 'Epic Games', '3.4');

----------------------------------------------------------------------------------------------------------------------------------------------------

/* DADOS PARA TABELA TIPO_CAMPEONATO */

INSERT INTO tipo_campeonato (jogo, nome, qtd_equipes, tipo_pontuacao, tamanho_equipes)
	VALUES('Counter Strike Global Offensive', 'CS GO', '10', 'Rounds', '5');
INSERT INTO tipo_campeonato (jogo, nome, qtd_equipes, tipo_pontuacao, tamanho_equipes)
	VALUES('Fortnite', 'Fortnite', '25', 'Mata Mata', '4');
INSERT INTO tipo_campeonato (jogo, nome, qtd_equipes, tipo_pontuacao, tamanho_equipes)
	VALUES('League of Legends', 'LOL', '15', 'Tabela de Pontos', '5');

----------------------------------------------------------------------------------------------------------------------------------------------------

/* DADOS PARA TABELA CAMPEONATO */

SELECT CURRVAL(pg_get_serial_sequence('campeonato','id'));

INSERT INTO campeonato (jogo, tipo_campeonato, dt_inicio, dt_termino)
	VALUES('Counter Strike Global Offensive', 'CS GO', '2019-11-27', '2019-12-23')
	RETURNING id;




----------------------------------------------------------------------------------------------------------------------------------------------------

/* DADOS PARA TABELA PREMIACAO */ 

/* >>>>>>>ESSA TABELA NAO TEM NO MAPEAMENTO <<<< */

INSERT INTO premiacao (id_campeonato, colocacao, premio)
	VALUES ('1', '10', '1º colocado = 1000,00 - 2° colocado = 500,00 - 3º colocado = vaga para o proximo ano');


----------------------------------------------------------------------------------------------------------------------------------------------------

/* DADOS PARA TABELA EQUIPE */
INSERT INTO equipe ( time, id_campeonato)
	VALUES ('paiN','1') RETURNING id;
INSERT INTO equipe ( time, id_campeonato)
	VALUES ('FLA','1')RETURNING id; 
INSERT INTO equipe ( time, id_campeonato)
	VALUES ('CNB','1')RETURNING id;  


----------------------------------------------------------------------------------------------------------------------------------------------------

/* DADOS PARA TABELA PATROCINIO EQUIPE */

INSERT INTO patrocinio_equipe (patrocinador, id_equipe, quantia)
	VALUES ('Nestle', '1', '10534.00');
INSERT INTO patrocinio_equipe (patrocinador, id_equipe, quantia)
	VALUES ('Google', '3', '1534.00');






----------------------------------------------------------------------------------------------------------------------------------------------------

/* DADOS PARA PARTIDA  */

INSERT INTO partida ( data, local, id_campeonato)
	VALUES ( '2019-12-10 16:00:01','bloco 10 sala 102', '1')RETURNING ID;
INSERT INTO partida (data, local, id_campeonato)
	VALUES ( '2019-12-10 10:00:01','bloco 3 sala 35', '1')RETURNING ID;
----------------------------------------------------------------------------------------------------------------------------------------------------

/* DADOS PARA TABELA EQUIPE_JOGA */

INSERT INTO equipe_joga (id_equipe, id_partida, colocacao)
	VALUES ('1','3', '2');
INSERT INTO equipe_joga (id_equipe, id_partida, colocacao)
	VALUES ('2','4', '3');
INSERT INTO equipe_joga (id_equipe, id_partida, colocacao)
	VALUES ('3','3', '1');

----------------------------------------------------------------------------------------------------------------------------------------------------

/* DADOS PARA TABELA juiz_arbitra */

INSERT INTO juiz_arbitra (id_partida, juiz)
	VALUES ('3','40056029861');
INSERT INTO juiz_arbitra (id_partida, juiz)
	VALUES ('4','50056029861');


----------------------------------------------------------------------------------------------------------------------------------------------------

/* DADOS PARA TABELA ASSISTIR */

INSERT INTO assistir (  email, id_partida)
	VALUES ( 'teste@gmail.com','3') RETURNING id;
INSERT INTO assistir (  email, id_partida)
	VALUES ( 'teste2@gmail.com','3') RETURNING id;
INSERT INTO assistir (  email, id_partida)
	VALUES ( 'teste3@gmail.com','4') RETURNING id;

----------------------------------------------------------------------------------------------------------------------------------------------------

/* DADOS PARA TABELA ASSISTIR */

INSERT INTO comentario ( id_assistir, horario, texto)
	VALUES ('2', '2019-12-10 10:00:01', 'texto de exemplo do comentario');


------------------------------------------------

