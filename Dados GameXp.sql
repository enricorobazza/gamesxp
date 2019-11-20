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
    VALUES ('Yang"', 'paiN', '400.560.298-61');
INSERT INTO JOGADOR (gamertag, time, cpf)
    VALUES ('FREIRE', 'CNB', '500.560.298-61');
INSERT INTO JOGADOR (gamertag, time, cpf)
    VALUES ('TAY', 'INTZ', '600.560.298-61');
INSERT INTO JOGADOR (gamertag, time, cpf)
    VALUES ('WIZER', 'KBM', '700.560.298-61');
INSERT INTO JOGADOR (gamertag, time, cpf)
    VALUES ('LEP', 'Keyd', '800.560.298-61');
INSERT INTO JOGADOR (gamertag, time, cpf)
    VALUES ('LOOP', 'RED', '900.560.298-61');
INSERT INTO JOGADOR (gamertag, time, cpf)
    VALUES ('ROBO', 'FLA', '100.560.298-61');
INSERT INTO JOGADOR (gamertag, time, cpf)
    VALUES ('ASLAN', 'CNB', '200.560.298-61');
INSERT INTO JOGADOR (gamertag, time, cpf)
    VALUES ('MINERVA', 'paiN', '300.560.298-61');

----------------------------------------------------------------------------------------------------------------------------------------------------

/* DADOS PARA TABELA PATROCINADOR */

INSERT INTO patrocinador (patrocinador, jogador, quantia)
	VALUES ('Nestle', 'Yang', '10.165,00');
INSERT INTO patrocinador (patrocinador, jogador, quantia)
	VALUES ('Google', 'ROBO', '15.165,00');
INSERT INTO patrocinador (patrocinador, jogador, quantia)
	VALUES ('Kabum', 'WIZER', '1.165,00');
	

----------------------------------------------------------------------------------------------------------------------------------------------------

/* DADOS PARA TABELA JOGO */

INSERT INTO jogo (nome, desenvolvedor, versao)
	VALUES ('League of Legends', 'RIOT Games', '9.22')
INSERT INTO jogo (nome, desenvolvedor, versao)
	VALUES ('Counter Strike Global Offensive', 'Valve', '2.0')
INSERT INTO jogo (nome, desenvolvedor, versao)
	VALUES ('Fortnite', 'Epic Games', '3.4')

----------------------------------------------------------------------------------------------------------------------------------------------------

/* DADOS PARA TABELA TIPO_CAMPEONATO */

INSERT INTO tipo_campeonato ( jogo, nome, qtd_equipes, tipo_pontuacao, tamanho_equipes)
	VALUES('Counter Strike Global Offensive', 'CS GO', '10', 'Rounds', '5');
INSERT INTO tipo_campeonato ( jogo, nome, qtd_equipes, tipo_pontuacao, tamanho_equipes)
	VALUES('Fortnite', 'Fortnite', '25', 'Mata Mata', '4');
INSERT INTO tipo_campeonato ( jogo, nome, qtd_equipes, tipo_pontuacao, tamanho_equipes)
	VALUES('League of Legends', 'LOL', '15', 'Tabela de Pontos', '5');

----------------------------------------------------------------------------------------------------------------------------------------------------

/* DADOS PARA TABELA CAMPEONATO */

