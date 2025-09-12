-- Crear la base de datos si no existe
CREATE DATABASE tienda;

-- Usar la base de datos tienda
USE tienda;

-- Crear la tabla de productos
CREATE TABLE IF NOT EXISTS productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    descripcion TEXT,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Crear la tabla de categorías
CREATE TABLE IF NOT EXISTS categorias (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Crear la tabla de productos_categorias para la relación muchos a muchos
CREATE TABLE IF NOT EXISTS productos_categorias (
    producto_id INT,
    categoria_id INT,
    PRIMARY KEY (producto_id, categoria_id),
    FOREIGN KEY (producto_id) REFERENCES productos(id) ON DELETE CASCADE,
    FOREIGN KEY (categoria_id) REFERENCES categorias(id) ON DELETE CASCADE
);


-- Crear un nuevo producto
INSERT INTO productos (nombre, precio, descripcion)
VALUES ('Producto 1', 10.99, 'Descripción del producto 1');
INSERT INTO productos (nombre, precio, descripcion)
VALUES ('Producto 2', 15.49, 'Descripción del producto 2');
INSERT INTO productos (nombre, precio, descripcion)
VALUES ('Producto 3', 7.99, 'Descripción del producto 3');
INSERT INTO productos (nombre, precio, descripcion)
VALUES ('Producto 4', 20.00, 'Descripción del producto 4');
INSERT INTO productos (nombre, precio, descripcion)
VALUES ('Producto 5', 5.75, 'Descripción del producto 5');


-- Leer todos los productos
SELECT * FROM productos;

-- insertar categorías
INSERT INTO categorias (nombre, descripcion)
VALUES ('Categoría A', 'Descripción de la categoría A');
INSERT INTO categorias (nombre, descripcion)
VALUES ('Categoría B', 'Descripción de la categoría B');
INSERT INTO categorias (nombre, descripcion)
VALUES ('Categoría C', 'Descripción de la categoría C');
INSERT INTO categorias (nombre, descripcion)
VALUES ('Categoría D', 'Descripción de la categoría D');
INSERT INTO categorias (nombre, descripcion)
VALUES ('Categoría E', 'Descripción de la categoría E');

-- Leer todas las categorías
SELECT * FROM categorias;
-- Asignar productos a categorías
INSERT INTO productos_categorias (producto_id, categoria_id)
VALUES (1, 1);
INSERT INTO productos_categorias (producto_id, categoria_id)
VALUES (1, 2);
INSERT INTO productos_categorias (producto_id, categoria_id)
VALUES (2, 1);
INSERT INTO productos_categorias (producto_id, categoria_id)
VALUES (3, 3);
INSERT INTO productos_categorias (producto_id, categoria_id)
VALUES (4, 4);
INSERT INTO productos_categorias (producto_id, categoria_id)
VALUES (5, 5);
INSERT INTO productos_categorias (producto_id, categoria_id)
VALUES (2, 3);
INSERT INTO productos_categorias (producto_id, categoria_id)
VALUES (3, 4);
INSERT INTO productos_categorias (producto_id, categoria_id)
VALUES (4, 5);
INSERT INTO productos_categorias (producto_id, categoria_id)
VALUES (5, 1);

-- Leer productos con sus categorías
SELECT p.id, p.nombre AS producto, c.nombre AS categoria
FROM productos p
JOIN productos_categorias pc ON p.id = pc.producto_id
JOIN categorias c ON pc.categoria_id = c.id;
-- Actualizar un producto
UPDATE productos
SET precio = 12.99, descripcion = 'Descripción actualizada del producto 5'
WHERE id = 5;
-- Eliminar un producto
DELETE FROM productos
WHERE id = 4;
-- Eliminar una categoría
DELETE FROM categorias
WHERE id = 3;

-- Leer todos los productos después de las actualizaciones
SELECT * FROM productos;
-- Leer todas las categorías después de las eliminaciones
SELECT * FROM categorias;
-- Leer productos con sus categorías después de las eliminaciones
SELECT p.id, p.nombre AS producto, c.nombre AS categoria
FROM productos p
JOIN productos_categorias pc ON p.id = pc.producto_id
JOIN categorias c ON pc.categoria_id = c.id;
