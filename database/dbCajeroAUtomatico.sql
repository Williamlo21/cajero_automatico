-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         8.0.30 - MySQL Community Server - GPL
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.6.0.6765
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para cajero_automatico
CREATE DATABASE IF NOT EXISTS `cajero_automatico` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `cajero_automatico`;

-- Volcando estructura para tabla cajero_automatico.usuarios
CREATE TABLE IF NOT EXISTS `usuarios` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `nombres` varchar(50) NOT NULL,
  `apellidos` varchar(50) NOT NULL,
  `numero_documento` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `usuario_unico` (`nombres`,`apellidos`,`numero_documento`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla cajero_automatico.usuarios: ~0 rows (aproximadamente)

-- Volcando estructura para tabla cajero_automatico.cuenta_bancaria
CREATE TABLE IF NOT EXISTS `cuenta_bancaria` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `numero_cuenta` int unsigned NOT NULL,
  `user_titular_id` bigint unsigned NOT NULL,
  `saldo` float unsigned NOT NULL DEFAULT (0),
  `tipo_cuenta` enum('AHORRO','NEQUI','A LA MANO','CREDITO','CORRIENTE') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `create_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `tope` float NOT NULL DEFAULT (2000000),
  PRIMARY KEY (`id`),
  UNIQUE KEY `cuenta_unica` (`numero_cuenta`) USING BTREE,
  KEY `FK_cuenta_bancaria_usuarios` (`user_titular_id`),
  CONSTRAINT `FK_cuenta_bancaria_usuarios` FOREIGN KEY (`user_titular_id`) REFERENCES `usuarios` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla cajero_automatico.cuenta_bancaria: ~0 rows (aproximadamente)


-- Volcando estructura para tabla cajero_automatico.tarjetas
CREATE TABLE IF NOT EXISTS `tarjetas` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `numero_tarjeta` int unsigned NOT NULL,
  `cuenta_bancaria_id` bigint unsigned NOT NULL,
  `tipo_tarjeta` enum('CREDITO','DEBITO') NOT NULL,
  `fecha_vencimiento` date DEFAULT NULL,
  `codigo_cvc` int NOT NULL,
  `clave` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tarjeta_unica` (`numero_tarjeta`),
  KEY `FK_tarjetas_cuenta_bancaria` (`cuenta_bancaria_id`),
  CONSTRAINT `FK_tarjetas_cuenta_bancaria` FOREIGN KEY (`cuenta_bancaria_id`) REFERENCES `cuenta_bancaria` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla cajero_automatico.tarjetas: ~0 rows (aproximadamente)

-- Volcando estructura para tabla cajero_automatico.transacciones
CREATE TABLE IF NOT EXISTS `transacciones` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `tipo_transaccion` enum('TRANSFERENCIA','RETIRO','AVANCE','PAGO') NOT NULL,
  `cuenta_bancaria_origen_id` bigint unsigned NOT NULL,
  `cuenta_bancaria_destino_id` bigint unsigned DEFAULT NULL,
  `saldo` decimal(20,2) unsigned NOT NULL,
  `descripcion` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `fecha` date NOT NULL,
  `create_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `FK_transacciones_cuenta_bancaria` (`cuenta_bancaria_origen_id`),
  KEY `FK_transacciones_cuenta_bancaria_2` (`cuenta_bancaria_destino_id`),
  CONSTRAINT `FK_transacciones_cuenta_bancaria` FOREIGN KEY (`cuenta_bancaria_origen_id`) REFERENCES `cuenta_bancaria` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_transacciones_cuenta_bancaria_2` FOREIGN KEY (`cuenta_bancaria_destino_id`) REFERENCES `cuenta_bancaria` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla cajero_automatico.transacciones: ~0 rows (aproximadamente)


-- Volcando estructura para tabla cajero_automatico.cuentas_inscritas
CREATE TABLE IF NOT EXISTS `cuentas_inscritas` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `cuenta_bancaria_id` bigint unsigned NOT NULL,
  `cuenta_bancaria_inscrita_id` bigint unsigned NOT NULL,
  `create_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `update_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cuenta_inscrita_unica` (`cuenta_bancaria_id`,`cuenta_bancaria_inscrita_id`),
  KEY `FK_cuentas_inscritas_cuenta_bancaria_2` (`cuenta_bancaria_inscrita_id`),
  CONSTRAINT `FK_cuentas_inscritas_cuenta_bancaria` FOREIGN KEY (`cuenta_bancaria_id`) REFERENCES `cuenta_bancaria` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_cuentas_inscritas_cuenta_bancaria_2` FOREIGN KEY (`cuenta_bancaria_inscrita_id`) REFERENCES `cuenta_bancaria` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla cajero_automatico.cuentas_inscritas: ~0 rows (aproximadamente)
-- Volcando estructura para tabla cajero_automatico.servicios
CREATE TABLE IF NOT EXISTS `servicios` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `referencia` varchar(50) NOT NULL,
  `servicio` varchar(50) NOT NULL,
  `factura` float unsigned NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla cajero_automatico.servicios: ~0 rows (aproximadamente)

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
