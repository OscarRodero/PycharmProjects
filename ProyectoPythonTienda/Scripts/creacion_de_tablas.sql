CREATE TABLE cliente (
    id SERIAL PRIMARY KEY,
    nombre TEXT,
    cif TEXT,
    direccion TEXT
);

CREATE TABLE modelo (
    id SERIAL PRIMARY KEY,
    descripcion TEXT
);

CREATE TABLE marca (
    id SERIAL PRIMARY KEY,
    descripcion TEXT
);

CREATE TABLE marca_modelo (
    id SERIAL PRIMARY KEY,
    id_marca INT REFERENCES marca(id),
    id_modelo INT REFERENCES modelo(id)
);

CREATE TABLE producto (
    id SERIAL PRIMARY KEY,
    descripcion TEXT,
    precio DECIMAL,
    id_marca_modelo INT REFERENCES marca_modelo(id),
    fecha_creacion DATE
);

CREATE TABLE ventas (
    id SERIAL PRIMARY KEY,
    id_producto INT REFERENCES producto(id),
    cantidad INT,
    id_cliente INT REFERENCES cliente(id),
    fecha_inicio_compra DATE,
    fecha_fin_compra DATE
);

CREATE TABLE reposicion (
    id SERIAL PRIMARY KEY,
    id_producto INT REFERENCES producto(id),
    cantidad INT,
    fecha_inicio_reposicion DATE,
    fecha_fin_reposicion DATE
);

CREATE TABLE inventario (
    id SERIAL PRIMARY KEY,
    id_producto INT REFERENCES producto(id),
    fecha_actualizacion DATE,
    cantidad_existente INT,
    cantidad_entrante INT,
    cantidad_saliente INT,
    id_venta INT REFERENCES ventas(id),
    id_reposicion INT REFERENCES reposicion(id)
);
