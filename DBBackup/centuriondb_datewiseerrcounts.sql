CREATE DATABASE  IF NOT EXISTS `centuriondb` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `centuriondb`;
-- MySQL dump 10.13  Distrib 5.7.12, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: centuriondb
-- ------------------------------------------------------
-- Server version	5.7.15-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `datewiseerrcounts`
--

DROP TABLE IF EXISTS `datewiseerrcounts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `datewiseerrcounts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cust_name` varchar(255) NOT NULL,
  `date_stamp` date NOT NULL,
  `month_name` varchar(255) NOT NULL,
  `appsrv_name` varchar(255) NOT NULL,
  `err_counts` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=163 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `datewiseerrcounts`
--

LOCK TABLES `datewiseerrcounts` WRITE;
/*!40000 ALTER TABLE `datewiseerrcounts` DISABLE KEYS */;
INSERT INTO `datewiseerrcounts` VALUES (39,'IBMCons','2016-05-01','May','App1',6),(40,'IBMCons','2016-05-02','May','App1',0),(41,'IBMCons','2016-05-03','May','App1',26),(42,'IBMCons','2016-05-04','May','App1',139),(43,'IBMCons','2016-05-05','May','App1',198),(44,'IBMCons','2016-05-06','May','App1',9),(45,'IBMCons','2016-05-07','May','App1',2),(46,'IBMCons','2016-05-08','May','App1',6),(47,'IBMCons','2016-05-09','May','App1',5),(48,'IBMCons','2016-05-10','May','App1',18),(49,'IBMCons','2016-05-11','May','App1',16),(50,'IBMCons','2016-05-12','May','App1',4),(51,'IBMCons','2016-05-13','May','App1',7),(52,'IBMCons','2016-05-14','May','App1',0),(53,'IBMCons','2016-05-15','May','App1',8),(54,'IBMCons','2016-05-16','May','App1',0),(55,'IBMCons','2016-05-17','May','App1',245),(56,'IBMCons','2016-05-18','May','App1',232),(57,'IBMCons','2016-05-19','May','App1',9),(58,'IBMCons','2016-05-20','May','App1',0),(59,'IBMCons','2016-05-21','May','App1',151),(60,'IBMCons','2016-05-22','May','App1',6),(61,'IBMCons','2016-05-23','May','App1',0),(62,'IBMCons','2016-05-24','May','App1',1072),(63,'IBMCons','2016-05-25','May','App1',4),(64,'IBMCons','2016-05-26','May','App1',6),(65,'IBMCons','2016-05-27','May','App1',125),(66,'IBMCons','2016-05-28','May','App1',6),(67,'IBMCons','2016-05-29','May','App1',6),(68,'IBMCons','2016-05-30','May','App1',140),(69,'IBMCons','2016-05-31','May','App1',5),(70,'IBMCons','2016-05-01','May','App2',9),(71,'IBMCons','2016-05-02','May','App2',10),(72,'IBMCons','2016-05-03','May','App2',11),(73,'IBMCons','2016-05-04','May','App2',361),(74,'IBMCons','2016-05-05','May','App2',160),(75,'IBMCons','2016-05-06','May','App2',5),(76,'IBMCons','2016-05-07','May','App2',3),(77,'IBMCons','2016-05-08','May','App2',12),(78,'IBMCons','2016-05-09','May','App2',34),(79,'IBMCons','2016-05-10','May','App2',6),(80,'IBMCons','2016-05-11','May','App2',21),(81,'IBMCons','2016-05-12','May','App2',13),(82,'IBMCons','2016-05-13','May','App2',0),(83,'IBMCons','2016-05-14','May','App2',0),(84,'IBMCons','2016-05-15','May','App2',8),(85,'IBMCons','2016-05-16','May','App2',0),(86,'IBMCons','2016-05-17','May','App2',641),(87,'IBMCons','2016-05-18','May','App2',292),(88,'IBMCons','2016-05-19','May','App2',3),(89,'IBMCons','2016-05-20','May','App2',1),(90,'IBMCons','2016-05-21','May','App2',0),(91,'IBMCons','2016-05-22','May','App2',7),(92,'IBMCons','2016-05-23','May','App2',4),(93,'IBMCons','2016-05-24','May','App2',23),(94,'IBMCons','2016-05-25','May','App2',18),(95,'IBMCons','2016-05-26','May','App2',3),(96,'IBMCons','2016-05-27','May','App2',8),(97,'IBMCons','2016-05-28','May','App2',0),(98,'IBMCons','2016-05-29','May','App2',6),(99,'IBMCons','2016-05-30','May','App2',6),(100,'IBMCons','2016-05-31','May','App2',3),(101,'IBMCons','2016-05-01','May','App98',12),(102,'IBMCons','2016-05-02','May','App98',2),(103,'IBMCons','2016-05-03','May','App98',2),(104,'IBMCons','2016-05-04','May','App98',2),(105,'IBMCons','2016-05-05','May','App98',2),(106,'IBMCons','2016-05-06','May','App98',2),(107,'IBMCons','2016-05-07','May','App98',2),(108,'IBMCons','2016-05-08','May','App98',12),(109,'IBMCons','2016-05-09','May','App98',2),(110,'IBMCons','2016-05-10','May','App98',2),(111,'IBMCons','2016-05-11','May','App98',2),(112,'IBMCons','2016-05-12','May','App98',2),(113,'IBMCons','2016-05-13','May','App98',2),(114,'IBMCons','2016-05-14','May','App98',2),(115,'IBMCons','2016-05-15','May','App98',12),(116,'IBMCons','2016-05-16','May','App98',2),(117,'IBMCons','2016-05-17','May','App98',2),(118,'IBMCons','2016-05-18','May','App98',2),(119,'IBMCons','2016-05-19','May','App98',2),(120,'IBMCons','2016-05-20','May','App98',2),(121,'IBMCons','2016-05-21','May','App98',2),(122,'IBMCons','2016-05-22','May','App98',12),(123,'IBMCons','2016-05-23','May','App98',2),(124,'IBMCons','2016-05-24','May','App98',2),(125,'IBMCons','2016-05-25','May','App98',2),(126,'IBMCons','2016-05-26','May','App98',2),(127,'IBMCons','2016-05-27','May','App98',2),(128,'IBMCons','2016-05-28','May','App98',2),(129,'IBMCons','2016-05-29','May','App98',12),(130,'IBMCons','2016-05-30','May','App98',2),(131,'IBMCons','2016-05-31','May','App98',2),(132,'IBMCons','2016-05-01','May','App99',58),(133,'IBMCons','2016-05-02','May','App99',34),(134,'IBMCons','2016-05-03','May','App99',0),(135,'IBMCons','2016-05-04','May','App99',43),(136,'IBMCons','2016-05-05','May','App99',199),(137,'IBMCons','2016-05-06','May','App99',0),(138,'IBMCons','2016-05-07','May','App99',0),(139,'IBMCons','2016-05-08','May','App99',10),(140,'IBMCons','2016-05-09','May','App99',26),(141,'IBMCons','2016-05-10','May','App99',0),(142,'IBMCons','2016-05-11','May','App99',105),(143,'IBMCons','2016-05-12','May','App99',68),(144,'IBMCons','2016-05-13','May','App99',68),(145,'IBMCons','2016-05-14','May','App99',68),(146,'IBMCons','2016-05-15','May','App99',10),(147,'IBMCons','2016-05-16','May','App99',10),(148,'IBMCons','2016-05-17','May','App99',93),(149,'IBMCons','2016-05-18','May','App99',120),(150,'IBMCons','2016-05-19','May','App99',120),(151,'IBMCons','2016-05-20','May','App99',120),(152,'IBMCons','2016-05-21','May','App99',142),(153,'IBMCons','2016-05-22','May','App99',10),(154,'IBMCons','2016-05-23','May','App99',33),(155,'IBMCons','2016-05-24','May','App99',102),(156,'IBMCons','2016-05-25','May','App99',21),(157,'IBMCons','2016-05-26','May','App99',21),(158,'IBMCons','2016-05-27','May','App99',21),(159,'IBMCons','2016-05-28','May','App99',21),(160,'IBMCons','2016-05-29','May','App99',10),(161,'IBMCons','2016-05-30','May','App99',68),(162,'IBMCons','2016-05-31','May','App99',68);
/*!40000 ALTER TABLE `datewiseerrcounts` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-11-17 17:36:08
