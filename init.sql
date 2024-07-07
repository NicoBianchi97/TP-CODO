create table if not exists authors (
    author_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    birth_date DATE
);

create table if not exists movies (
    movie_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    release_date DATE,
    rating DECIMAL(2, 1),
    language VARCHAR(50),
    author_id INTEGER,
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
);

create table if not exists characters (
    character_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    birth_date DATE
);

create table if not exists genres (
    genre_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

create table if not exists movie_genres (
    movie_id INTEGER,
    genre_id INTEGER,
    PRIMARY KEY (movie_id, genre_id),
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id),
    FOREIGN KEY (genre_id) REFERENCES genres(genre_id)
);

create table if not exists movie_characters (
    movie_id INTEGER,
    character_id INTEGER,
    PRIMARY KEY (movie_id, character_id),
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id),
    FOREIGN KEY (character_id) REFERENCES characters(character_id)
);

--- inserts
INSERT INTO
    authors (first_name, last_name, birth_date)
VALUES
    ('John', 'Doe', '1970-01-01'),
    ('Jane', 'Doe', '1987-01-01'),
    ('Lucas', 'Nose', '2001-01-01');

INSERT INTO
    characters (first_name, last_name, birth_date)
VALUES
    ('John', 'Snow', '1970-01-01'),
    ('Harry', 'Potter', '1987-01-01');

insert into
    genres (name)
values
    ('Action'),
    ('Drama'),
    ('Fantasy');

insert into
    movies (
        name,
        description,
        release_date,
        rating,
        language,
        author_id
    )
values
    (
        'Peli 1',
        'lorem 10',
        '2024-01-01',
        8.5,
        'English',
        1
    ),
    (
        'Peli 2',
        'lorem 20',
        '1980-01-01',
        6.5,
        'English',
        2
    );

insert into
    movie_genres (movie_id, genre_id)
values
    (1, 1),
    (1, 3),
    (2, 3);

insert into
    movie_characters (movie_id, character_id)
values
    (1, 1),
    (1, 2),
    (2, 1);

--- tpo14
create table if not exists libros (
    id_libros SERIAL PRIMARY KEY,
    nombre_libro varchar(100) NOT NULL,
    autor varchar(150) NOT NULL,
    precio decimal(6, 2) DEFAULT NULL,
    genero varchar(50) DEFAULT NULL,
    imagen varchar(255) DEFAULT NULL
);

--- inserts
INSERT INTO
    libros
VALUES
    (
        1,
        'Cien años de soledad',
        'Gabriel García Marquez',
        19.99,
        'Realismo mágico',
        'cien_años_de_soledad.jpg'
    ),
(
        2,
        'El nombre del viento',
        'Patrick Rothfuss',
        29.99,
        'Fantasía',
        'el_nombre_del_viento.png'
    ),
(
        3,
        '1984',
        'George Orwell',
        22.75,
        'Romance',
        '1984.jpg'
    ),
(
        4,
        'Orgullo y prejuicio',
        'Austen',
        9999.99,
        'Drama',
        'orgullo_y_prejuicio.jpg'
    ),
(
        5,
        'La sombra del viento',
        'Carlos Ruiz Zafón',
        24.95,
        'Fantasía',
        'la_sombra_del_viento.jpg'
    ),
(
        6,
        'Harry Potter y la piedra filosofal',
        'J.K. Rowling',
        27.50,
        'Drama',
        'harry_potter_y_la_piedra_filosofal.jpg'
    ),
(
        7,
        'Crónica de una muerte anunciada',
        'Gabriel García Márquez',
        19.99,
        'Ciencia ficción',
        'cronica_de_una_muerte_anunciada.jpg'
    ),
(
        8,
        'Los juegos del hambre',
        'Suzanne Collins',
        21.25,
        'Fantasía',
        'los_juegos_del_hambre.png'
    ),
(
        9,
        'El retrato de Dorian Gray',
        'Oscar Wilde',
        30.99,
        'Ficción',
        'el_retrato_de_dorian_gray.jpg'
    ),
(
        10,
        'Matar a un ruiseñor',
        'Harper Lee',
        23.50,
        'Novela histórica',
        'matar_a _un_ruiseñor.jpg'
    ),
(
        11,
        'El perfume',
        'Patrick Süskind',
        20.75,
        'Espiritualidad',
        'el_perfume.jpg'
    ),
(
        12,
        'El alquimista',
        'Paulo Coelho',
        17.99,
        'Ficción literaria',
        'el_alquimista.jpg'
    ),
(
        13,
        'Rayuela',
        'Julio Cortázar',
        26.95,
        'Fantasía',
        'rayuela.jpg'
    ),
(
        15,
        'El nombre de la rosa',
        'Umberto Eco',
        25.99,
        'Novela histórica',
        'el_nombre_de_la_rosa.jpg'
    );