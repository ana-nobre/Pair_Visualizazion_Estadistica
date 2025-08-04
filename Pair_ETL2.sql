USE base_pair_ETL;

CREATE TABLE clientes (
    id_cliente INT,
    id_producto VARCHAR(10),
    fecha_venta DATE,
    cantidad INT,
    total DECIMAL(10, 2),
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    gender VARCHAR(10),
    city VARCHAR(50),
    country VARCHAR(50),
    address VARCHAR(100),
    nombre_producto VARCHAR(100),
    categoria VARCHAR(50),
    precio DECIMAL(10, 2),
    origen VARCHAR(50),
    descripcion TEXT
);

INSERT INTO clientes (
    id_cliente, id_producto, fecha_venta, cantidad, total,
    first_name, last_name, email, gender, city, country,
    address, nombre_producto, categoria, precio, origen,
    descripcion
)
VALUES (
    723, 'A1', '2023-11-22', 2, 17.98,
    'Sephira', 'Bleackley', 'sbleackleyk2@liveinternet.ru', 'NaN', 'Girona', 'NaN',
    '4 Birchwood Road', 'Pizza Margherita', 'Platos Preparados', 8.99, 'Italia',
    'Clásica pizza italiana con tomate'
);

SELECT * FROM clientes;
