-- Criação da tabela de usuários
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    role ENUM('gerente','mecanico','administrador') NOT NULL,
    empresa_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Criação da tabela de veículos
CREATE TABLE IF NOT EXISTS veiculos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    placa VARCHAR(20) UNIQUE NOT NULL,
    modelo VARCHAR(100),
    ano INT,
    quilometragem_atual INT,
    empresa_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Criação da tabela de pneus
CREATE TABLE IF NOT EXISTS pneus (
    id INT AUTO_INCREMENT PRIMARY KEY,
    codigo VARCHAR(50) UNIQUE NOT NULL,
    marca VARCHAR(50),
    modelo VARCHAR(50),
    status ENUM('estoque','veiculo','manutencao') DEFAULT 'estoque',
    veiculo_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Associação pneu-veículo
CREATE TABLE IF NOT EXISTS pneus_veiculos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pneu_id INT NOT NULL,
    veiculo_id INT NOT NULL,
    data_associacao DATE,
    FOREIGN KEY (pneu_id) REFERENCES pneus(id),
    FOREIGN KEY (veiculo_id) REFERENCES veiculos(id)
);
