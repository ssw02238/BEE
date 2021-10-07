-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: bee.cjkrtt0iwcwz.ap-northeast-2.rds.amazonaws.com    Database: BEE
-- ------------------------------------------------------
-- Server version	8.0.23

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
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ '';

--
-- Table structure for table `corporates_corporate_scrap_user`
--

DROP TABLE IF EXISTS `corporates_corporate_scrap_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `corporates_corporate_scrap_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `corporate_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `corporates_corporate_scr_corporate_id_user_id_f041d654_uniq` (`corporate_id`,`user_id`),
  KEY `corporates_corporate_user_id_a9842f8d_fk_accounts_` (`user_id`),
  CONSTRAINT `corporates_corporate_corporate_id_f0053b51_fk_corporate` FOREIGN KEY (`corporate_id`) REFERENCES `corporates_corporate` (`id`),
  CONSTRAINT `corporates_corporate_user_id_a9842f8d_fk_accounts_` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=117 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `corporates_corporate_scrap_user`
--

LOCK TABLES `corporates_corporate_scrap_user` WRITE;
/*!40000 ALTER TABLE `corporates_corporate_scrap_user` DISABLE KEYS */;
INSERT INTO `corporates_corporate_scrap_user` VALUES (95,1,10),(74,1,13),(90,1,15),(94,3,10),(103,10,10),(107,17,10),(96,18,10),(114,21,8),(106,25,10),(97,27,10),(109,31,7),(73,31,13),(78,31,17),(110,33,7),(91,33,17),(102,53,10),(108,75,10),(88,88,7),(113,100,8),(81,100,13),(104,108,10),(105,112,10),(101,142,10),(98,144,10),(68,164,10),(99,165,10),(100,190,10);
/*!40000 ALTER TABLE `corporates_corporate_scrap_user` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-10-07 16:43:02
