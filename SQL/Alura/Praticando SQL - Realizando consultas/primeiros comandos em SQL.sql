-- Visualiza a tabela 
SELECT * -- NÂO DAR SELECT SEM O LIMIT 
FROM TabelaColaboradores
LIMIT 10;

-- Deleta linhas da tabela - NÂO DELETAR SEM WHERE
DELETE
FROM TabelaColaboradores
WHERE salario = 4000;

-- Adiciona dados na tabala
INSERT INTO TabelaColaboradores (id_colaborador, salario, nomecolaborador, emailcolaborador, cargo, cpfcolaborador, telefonecolaborador, id_departamento)
VALUES ('C06', 4900, 'Josue Costa', 'josue@gmail.com', 'Gerente', 12365485974, 62999999999, 'D06');

-- Atualiza dados das linhas - NÂO DAR UPDATE SEM WHERE
UPDATE
TabelaColaboradores
SET
salario = 7000
WHERE
id_colaborador = 'C06';