CREATE DATABASE IF NOT EXISTS master_python;

use master_python;

CREATE TABLE IF NOT EXISTS usuario(
    id          int(25)  auto_increment not null,
    nombre      varchar(100),
    apellidos   varchar(255),
    email       varchar(255) not null,
    paswword    varchar(255) not null,
    fecha       date not nuLL,
    CONSTRAINT pk_usuario   PRIMARY KEY(id),
    CONSTRAINT uq_email     UNIQUE(email)
)ENGINE=InnoDb;

CREATE TABLE IF NOT EXISTS nota(
    id          int(25) not null,
    id_usuario  int(25) not null,
    titulo      varchar(255) not null,
    descripcion MEDIUMTEXT,
    fecha       date not null,
    CONSTRAINT pk_nota PRIMARY KEY(id),
    CONSTRAINT fk_nota_usuario FOREIGN KEY(id_usuario) REFERENCES usuario(id)
)ENGINE=InnoDb;
