-- Datos base del sistema (INSERT IGNORE evita duplicados si se ejecuta más de una vez)
USE turnos_medicos;

INSERT IGNORE INTO estado (estado, descripcion) VALUES ('Reservada', 'Cita reservada, pendiente de confirmación');
INSERT IGNORE INTO estado (estado, descripcion) VALUES ('Confirmada', 'Cita confirmada por el paciente');
INSERT IGNORE INTO estado (estado, descripcion) VALUES ('Cancelada', 'Cita cancelada');
INSERT IGNORE INTO estado (estado, descripcion) VALUES ('Atendida', 'Cita realizada');

INSERT IGNORE INTO especialidad (especialidad, descripcion) VALUES ('Medicina General', 'Atención médica general');
INSERT IGNORE INTO especialidad (especialidad, descripcion) VALUES ('Pediatría', 'Atención de niños y adolescentes');
INSERT IGNORE INTO especialidad (especialidad, descripcion) VALUES ('Cardiología', 'Enfermedades del corazón');
