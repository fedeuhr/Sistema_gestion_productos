CREATE TABLE `producto` (
  `codigo` char(6) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `precio` float(5,2) unsigned NOT NULL,
  PRIMARY KEY (`codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='Almacena los datos de los productos.';