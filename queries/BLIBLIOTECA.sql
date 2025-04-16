-- Tabla Editorial
CREATE TABLE Editorial(
	id_editorial INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    pais VARCHAR(100),
    anio_fundacion INT
);

-- Tabla Autor
CREATE TABLE Autor(
	id_autor INT PRIMARY KEY,
    nombre_completo VARCHAR(100) NOT NULL,
    nacionalidad VARCHAR(50),
    fecha_nacimiento DATE,
    biografia TEXT
);

-- Tabla Libro (Relacion uno a muchos(1:N))
CREATE TABLE Libro(
    id_libro INT PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    isbn VARCHAR(20) UNIQUE NOT NULL,
    anio_publicacion INT,
    numero_paginas INT,
    genero VARCHAR(50),
    editorial_id INT,
    FOREIGN KEY (editorial_id) REFERENCES Editorial(id_editorial),
);

-- Table intermedia LibroAutor (Relacion muchos a muchos(N:N))S
CREATE TABLE LibroAutor(
    libro_id INT,
    autor_id INT,
    PRIMARY KEY (libro_id, autor_id),
    FOREIGN KEY (libro_id) REFERENCES Libro(id_libro),
    FOREIGN KEY (autor_id) REFERENCES Autor(id_autor)
);

-- Tabla Usuario
CREATE TABLE Usuario(
    id_usuario INT PRIMARY KEY,
    nombre_completo VARCHAR(100) NOT NULL,
    correo_electronico VARCHAR(100) UNIQUE NOT NULL,
    telefono VARCHAR(20),
    direccion TEXT,
    fecha_registro DATE DEFAULT CURRENT_DATE,
);

-- Tabla prestamo (Relacion uno a muchos(1:N))
CREATE TABLE Prestamo(
    id_prestamo INT PRIMARY KEY,
    fecha_prestamo DATE NOT NULL,
    fecha_devolucion DATE,
    estado VARCHAR(20) DEFAULT 'pendiente', -- 'Pendiente', 'Devuelto', 'cancelado'
    usuario_id INT,
    libro_id INT,
    FOREIGN KEY (usuario_id) REFERENCES Usuario(id_usuario),
    FOREIGN KEY (libro_id) REFERENCES Libro(id_libro)
)

-- Insert de prueba para todas las tablas

-- Editorial
INSERT INTO Editorial(id_editorial, nombre, pais, anio_fundacion)
VALUES (1, 'Editorial Planeta', 'Espa a', 1949),
        (2, 'Anagrama', 'Espa a', 1969),
        (3, 'Santillana', 'Argentina', 1960),
        (4, 'Alfaguara', 'España', 1964),
        (5, 'Seix Barral', 'España', 1911),
        (6, 'Tusquets', 'España', 1969),
        (7, 'Penguin Random House', 'Estados Unidos', 1927),
        (8, 'HarperCollins', 'Reino Unido', 1989);

-- Autor
INSERT INTO Autor(id_autor, nombre_completo, nacionalidad, fecha_nacimiento, biografia)
VALUES (1, 'Gabriel Garcia Marquez', 'Colombia', '1927-03-06', 'Escritor colombiano ganador del Premio Nobel de Literatura en 1982'),
        (2, 'Ernesto S bato', 'Argentina', '1911-06-24', 'Escritor argentino'),
        (3, 'Julio Cort zar', 'Argentina', '1914-08-26', 'Escritor argentino'),
        (4, 'Mario Vargas Llosa', 'Perú', '1936-03-28', 'Escritor peruano ganador del Premio Nobel de Literatura en 2010'),
        (5, 'Isabel Allende', 'Chile', '1942-08-02', 'Escritora chilena, una de las autoras más leídas en español'),
        (6, 'Carlos Fuentes', 'México', '1928-11-11', 'Escritor mexicano, uno de los principales exponentes de la literatura latinoamericana'),
        (7, 'Jorge Luis Borges', 'Argentina', '1899-08-24', 'Escritor argentino, uno de los más destacados de la literatura del siglo XX'),
        (8, 'Pablo Neruda', 'Chile', '1904-07-12', 'Poeta chileno ganador del Premio Nobel de Literatura en 1971');

-- Libro
INSERT INTO Libro(id_libro, titulo, isbn, anio_publicacion, numero_paginas, genero, editorial_id)
VALUES (1, 'Cien a os de soledad', '978-607-07-0366-8', 1967, 448, 'Novela', 1),
        (2, 'El t nel', '978-84-339-0416-4', 1959, 272, 'Novela', 2),
        (3, 'Rayuela', '978-950-49-1441-6', 1963, 560, 'Novela', 3),
        (4, 'La casa de los espíritus', '978-84-322-0847-0', 1982, 432, 'Novela', 4),
        (5, 'La ciudad y los perros', '978-84-322-0847-1', 1963, 384, 'Novela', 5),
        (6, 'La muerte de Artemio Cruz', '978-84-322-0847-2', 1962, 320, 'Novela', 6),
        (7, 'Ficciones', '978-84-376-0494-7', 1944, 224, 'Cuento', 7),
        (8, 'Veinte poemas de amor y una canción desesperada', '978-84-376-0495-4', 1924, 64, 'Poesía', 8);

-- LibroAutor
INSERT INTO LibroAutor(libro_id, autor_id)
VALUES (1, 1),
        (2, 2),
        (3, 3),
        (4, 5),
        (5, 4),
        (6, 6),
        (7, 7),
        (8, 8);

-- Usuario
INSERT INTO Usuario(id_usuario, nombre_completo, correo_electronico, telefono, direccion)
VALUES (1, 'Juan P rez', 'jperez@dominio.com', '1234567', 'Calle 1 # 2-3'),
        (2, 'Mar a G mez', 'mgomez@dominio.com', '9876543', 'Calle 2 # 4-5'),
        (3, 'Pedro L pez', 'plopez@dominio.com', '555-1234', 'Calle 3 # 6-7'),
        (4, 'Ana María Rodríguez', 'arodriguez@dominio.com', '555-9876', 'Avenida Principal #123'),
        (5, 'Carlos Sánchez', 'csanchez@dominio.com', '555-4321', 'Calle Secundaria #456'),
        (6, 'Laura Martínez', 'lmartinez@dominio.com', '555-7890', 'Plaza Central #789'),
        (7, 'Sofía Ramírez', 'sramirez@dominio.com', '555-1111', 'Calle Nueva #123'),
        (8, 'Luis Fernández', 'lfernandez@dominio.com', '555-2222', 'Avenida Central #456');

-- Prestamo
INSERT INTO Prestamo(id_prestamo, fecha_prestamo, fecha_devolucion, estado, usuario_id, libro_id)
VALUES (1, '2020-01-01', NULL, 'pendiente', 1, 1),
        (2, '2020-01-15', '2020-01-20', 'devuelto', 2, 2),
        (3, '2020-02-01', NULL, 'cancelado', 3, 3),
        (4, '2020-03-01', '2020-03-15', 'devuelto', 4, 4),
        (5, '2020-03-10', NULL, 'pendiente', 5, 5),
        (6, '2020-03-15', NULL, 'pendiente', 6, 6),
        (7, '2025-04-01', NULL, 'pendiente', 7, 7),
        (8, '2025-04-05', NULL, 'pendiente', 8, 8);

-- Consultar entre tablas (Con JOIN)

-- Mostrar todos los prestamos con informacion de usuario y libro
SELECT 
    p.id_prestamo AS id_prestamo,
    U.nombre_completo AS nombre_usuario,
    L.titulo AS titulo_libro,
    P.fecha_prestamo,
    p.fecha_devolucion,
    p.estado,
    CASE
        WHEN p.estado = 'cancelado' THEN 'Prestamo cancelado'
        WHEN p.fecha_devolucion IS NULL THEN 'Libro aun no ha sido devuelto'
        ELSE 'Libro devuelto'
    END AS obsevacion
FROM prestamo P
JOIN usuario U ON P.usuario_id = U.id_usuario
JOIN libro L ON P.libro_id = L.id_libro;

--Opcion 2

SELECT 
    p.id_prestamo AS id_prestamo,
    U.nombre_completo AS nombre_usuario,
    L.titulo AS titulo_libro,
    P.fecha_prestamo,
    CASE
        WHEN p.estado = 'cancelado' THEN 'Prestamo cancelado'
        WHEN p.fecha_devolucion IS NULL THEN 'Libro aun no ha sido devuelto'
        ELSE DATE_FORMAT(p.fecha_devolucion, '%Y-%m-%d')
    END AS fecha_devolucion,
	p.estado

FROM prestamo P
JOIN usuario U ON P.usuario_id = U.id_usuario
JOIN libro L ON P.libro_id = L.id_libro;

--Opcion sin alias
SELECT 
    prestamo.id_prestamo,
    usuario.nombre_completo,
    libro.titulo,
    prestamo.fecha_prestamo,
    CASE
        WHEN prestamo.estado = 'cancelado' THEN 'Prestamo cancelado'
        WHEN prestamo.fecha_devolucion IS NULL THEN 'Libro aun no ha sido devuelto'
        ELSE DATE_FORMAT(prestamo.fecha_devolucion, '%Y-%m-%d')
    END AS fecha_devolucion,
    prestamo.estado

FROM prestamo 
JOIN usuario ON prestamo.usuario_id = usuario.id_usuario
JOIN libro ON prestamo.libro_id = libro.id_libro;

-- Obtener todos los libros de un autor
SELECT
    l.titulo AS libro, 
    A.nombre_completo AS autor,
    l.isbn
FROM Libro as l
JOIN LibroAutor as LA ON l.id_libro = LA.libro_id
JOIN Autor as A ON LA.autor_id = A.id_autor

-- Listar los libros por editorial
SELECT
    L.titulo AS libro, 
    E.nombre AS editorial,
    L.isbn
FROM Libro as L
JOIN Editorial as E ON L.editorial_id = E.id_editorial

-- Consultar los prestasmo realizados en una fecha especifica
SELECT 
    p.id_prestamo
FROM Prestamo p
JOIN Usuario u ON p.usuario_id = u.id_usuario
JOIN Libro l ON p.libro_id = l.id_libro
WHERE p.fecha_prestamo = '2020-01-01';

