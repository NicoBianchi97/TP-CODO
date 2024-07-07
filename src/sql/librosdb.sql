-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: librosdb
-- ------------------------------------------------------
-- Server version	8.0.37

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `libros`
--

DROP TABLE IF EXISTS libros;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE libros (
  id_libros SERIAL NOT NULL PRIMARY KEY,
  nombre_libro varchar(100) NOT NULL,
  autor varchar(150) NOT NULL,
  precio decimal(6,2) DEFAULT NULL,
  genero varchar(50) DEFAULT NULL,
  imagen varchar(255) DEFAULT NULL,
 )

-- LOCK TABLES `libros` WRITE;
/*!40000 ALTER TABLE `libros` DISABLE KEYS */;
INSERT INTO libros VALUES (1,'Cien años de soledad','Gabriel García Marquez',19.99,'Realismo mágico','cien_años_de_soledad.jpg'),(2,'El nombre del viento','Patrick Rothfuss',29.99,'Fantasía','el_nombre_del_viento.png'),(3,'1984','George Orwell',22.75,'Romance','1984.jpg'),(4,'Orgullo y prejuicio','Austen',9999.99,'Drama','orgullo_y_prejuicio.jpg'),(5,'La sombra del viento','Carlos Ruiz Zafón',24.95,'Fantasía','la_sombra_del_viento.jpg'),(6,'Harry Potter y la piedra filosofal','J.K. Rowling',27.50,'Drama','harry_potter_y_la_piedra_filosofal.jpg'),(7,'Crónica de una muerte anunciada','Gabriel García Márquez',19.99,'Ciencia ficción','cronica_de_una_muerte_anunciada.jpg'),(8,'Los juegos del hambre','Suzanne Collins',21.25,'Fantasía','los_juegos_del_hambre.png'),(9,'El retrato de Dorian Gray','Oscar Wilde',30.99,'Ficción','el_retrato_de_dorian_gray.jpg'),(10,'Matar a un ruiseñor','Harper Lee',23.50,'Novela histórica','matar_a _un_ruiseñor.jpg'),(11,'El perfume','Patrick Süskind',20.75,'Espiritualidad','el_perfume.jpg'),(12,'El alquimista','Paulo Coelho',17.99,'Ficción literaria','el_alquimista.jpg'),(13,'Rayuela','Julio Cortázar',26.95,'Fantasía','rayuela.jpg'),(15,'El nombre de la rosa','Umberto Eco',25.99,'Novela histórica','el_nombre_de_la_rosa.jpg');
/*!40000 ALTER TABLE `libros` ENABLE KEYS */;
-- UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-07-05 15:34:40
