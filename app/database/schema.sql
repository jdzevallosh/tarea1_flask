DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dni TEXT NOT NULL UNIQUE,
    given_name TEXT NOT NULL,
    family_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone_number TEXT,
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Registros iniciales de prueba
INSERT INTO users (dni, given_name, family_name, email, phone_number, address) 
VALUES ('72807793', 'Javier', 'Zevallos', 'jdzevallosh@gmail.com', '921234730', 'Av. Javier de luna pizarro 308');

INSERT INTO users (dni, given_name, family_name, email, phone_number, address) 
VALUES ('73038414', 'Yajaira', 'Charahua', 'estrellita.tlv710@gmail.com', '916477807', 'Enace sector 3 Mz D Lote 4');