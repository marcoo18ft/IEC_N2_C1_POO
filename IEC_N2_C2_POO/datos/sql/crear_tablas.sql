-- Sistema de Turnos Médicos - Creación de la base de datos y las tablas (MySQL)
CREATE DATABASE IF NOT EXISTS turnos_medicos CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE turnos_medicos;

CREATE TABLE IF NOT EXISTS especialidad (
    id_especialidad INT AUTO_INCREMENT PRIMARY KEY,
    especialidad    VARCHAR(100) NOT NULL UNIQUE,
    descripcion     VARCHAR(255) NOT NULL DEFAULT '',
    habilitado      TINYINT(1)   NOT NULL DEFAULT 1
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS estado (
    id_estado   INT AUTO_INCREMENT PRIMARY KEY,
    estado      VARCHAR(100) NOT NULL UNIQUE,
    descripcion VARCHAR(255) NOT NULL DEFAULT '',
    habilitado  TINYINT(1)   NOT NULL DEFAULT 1
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS profesional (
    id_profesional  INT AUTO_INCREMENT PRIMARY KEY,
    rut             VARCHAR(12)  NOT NULL UNIQUE,
    nombres         VARCHAR(100) NOT NULL,
    apellidos       VARCHAR(100) NOT NULL,
    id_especialidad INT          NOT NULL,
    telefono        VARCHAR(15)  NOT NULL,
    email           VARCHAR(100) NOT NULL,
    habilitado      TINYINT(1)   NOT NULL DEFAULT 1,
    FOREIGN KEY (id_especialidad) REFERENCES especialidad (id_especialidad)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS horario_atencion (
    id_horario      INT AUTO_INCREMENT PRIMARY KEY,
    id_profesional  INT        NOT NULL,
    fecha           DATE       NOT NULL,
    hora_inicio     TIME       NOT NULL,
    hora_fin        TIME       NOT NULL,
    duracion_bloque INT        NOT NULL DEFAULT 30,
    habilitado      TINYINT(1) NOT NULL DEFAULT 1,
    FOREIGN KEY (id_profesional) REFERENCES profesional (id_profesional),
    CHECK (hora_fin > hora_inicio)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS paciente (
    id_paciente      INT AUTO_INCREMENT PRIMARY KEY,
    rut              VARCHAR(12)  NOT NULL UNIQUE,
    nombres          VARCHAR(100) NOT NULL,
    apellidos        VARCHAR(100) NOT NULL,
    fecha_nacimiento DATE         NOT NULL,
    telefono         VARCHAR(15)  NOT NULL,
    email            VARCHAR(100) NOT NULL,
    habilitado       TINYINT(1)   NOT NULL DEFAULT 1
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS cita (
    id_cita        INT AUTO_INCREMENT PRIMARY KEY,
    id_paciente    INT          NOT NULL,
    id_profesional INT          NOT NULL,
    id_estado      INT          NOT NULL,
    observaciones  VARCHAR(255) NOT NULL DEFAULT '',
    fecha_registro DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_paciente)    REFERENCES paciente (id_paciente),
    FOREIGN KEY (id_profesional) REFERENCES profesional (id_profesional),
    FOREIGN KEY (id_estado)      REFERENCES estado (id_estado)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS ficha_paciente (
    id_ficha    INT AUTO_INCREMENT PRIMARY KEY,
    id_paciente INT          NOT NULL UNIQUE,
    motivo      VARCHAR(255) NOT NULL,
    diagnostico VARCHAR(255) NOT NULL DEFAULT '',
    tratamiento VARCHAR(255) NOT NULL DEFAULT '',
    FOREIGN KEY (id_paciente) REFERENCES paciente (id_paciente)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS historial_clinica (
    id_historial        INT AUTO_INCREMENT PRIMARY KEY,
    id_ficha            INT          NOT NULL,
    id_paciente         INT          NOT NULL,
    id_cita             INT          NOT NULL,
    motivo              VARCHAR(255) NOT NULL,
    diagnostico         VARCHAR(255) NOT NULL DEFAULT '',
    tratamiento         VARCHAR(255) NOT NULL DEFAULT '',
    observaciones       VARCHAR(255) NOT NULL DEFAULT '',
    fecha_actualizacion DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (id_ficha)    REFERENCES ficha_paciente (id_ficha) ON DELETE CASCADE,
    FOREIGN KEY (id_paciente) REFERENCES paciente (id_paciente),
    FOREIGN KEY (id_cita)     REFERENCES cita (id_cita) ON DELETE CASCADE
) ENGINE=InnoDB;

CREATE TABLE USUARIOS