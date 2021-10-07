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
-- Table structure for table `accounts_user`
--

DROP TABLE IF EXISTS `accounts_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb4_general_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `email` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `nickname` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_admin` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `nickname` (`nickname`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_user`
--

LOCK TABLES `accounts_user` WRITE;
/*!40000 ALTER TABLE `accounts_user` DISABLE KEYS */;
INSERT INTO `accounts_user` VALUES (1,'pbkdf2_sha256$260000$vKHoLYhui8aPs2ROfsctoU$FQ7tsAS7nIqXPgew36I6Nc1lbqsv1t6w2WrHe37wpoM=','2021-09-21 12:21:57.909673','rbwjdsladlek@gmail.com','admin',1,1,1,1,'2021-09-21 12:21:21.259354'),(2,'1234',NULL,'dqq9744@naver.com','kim',1,0,0,0,'2021-09-21 12:34:17.837669'),(3,'pbkdf2_sha256$260000$pIh0Al1TPWYnV0FtqzusZ5$p55Uz5FFHks6E2H+lZ24NmEQm71DVkbGCr7c+5qf3fc=',NULL,'gyujeong@gmail.com','gyugyu',1,0,0,0,'2021-09-21 14:49:08.380307'),(4,'pbkdf2_sha256$260000$8THSmVjcD44KbmFZaJyO9b$GkYM5gcBbBdxMD5/0PA1OPdqEZOQ1b2S65v6wtOeGnk=',NULL,'gyu@gmail.com','gyu',1,0,0,0,'2021-09-23 15:51:50.213162'),(5,'pbkdf2_sha256$260000$kqzfX9m2SpGDqFcjaBHcSM$OBnjr+a9zrRZ0pbfAZW32sfv4EQdDikgYB3LB9rfG3s=',NULL,'ssw02238@naver.com','윤서',1,0,0,0,'2021-09-23 15:53:37.521836'),(6,'pbkdf2_sha256$260000$gpifyyk3NZySXIKq6vS0AX$CgF+Htyi80NyscBjN2L1y+X0bFT+Z8m2JkCI0cs1IFg=',NULL,'ssw@naver.com','hi',1,0,0,0,'2021-09-23 17:44:28.679739'),(7,'pbkdf2_sha256$260000$OyyXLh8GQ822mY2NZywlk2$ciirOSGU4hkGowdZUNBVcQa067Iicv5W+biK/0PLliA=',NULL,'kys@naver.com','ys',1,0,0,0,'2021-09-24 10:58:58.971973'),(8,'pbkdf2_sha256$260000$ULYa21XGbp9WQdoGYDpoYh$5g+Htx4M9nZXmToFovMTNdG3nxtcpoeTJfDLBeXBKRQ=',NULL,'yechan2@naver.com','찬찬이',1,0,0,0,'2021-09-24 14:59:55.330332'),(9,'pbkdf2_sha256$260000$xyuZU4XZa0Eb4Gry60bVNc$x9HPM+4Brzlv5P8GDV182SWaacY1zTBBzldtjsKNoK4=',NULL,'ss@naver.com','ss',1,0,0,0,'2021-09-28 16:48:01.620639'),(10,'pbkdf2_sha256$260000$57oO85EoFqYU9ueL3qPewU$AL9JEDCNG1pPKcaCyRtnf60Gn2fepdefnV8p5g6CBvU=',NULL,'yechan3@naver.com','찬',1,0,0,0,'2021-09-29 15:53:43.762369'),(11,'pbkdf2_sha256$260000$Enq7zlo6CrD7uUyyD753qQ$j/tyBqqgfVT24+Glb+do2crC3zInfQPC74UV0wsNAhM=',NULL,'rbwjd@naver.com','aaa',1,0,0,0,'2021-09-29 16:36:50.008723'),(13,'pbkdf2_sha256$260000$YXCuPbGhfAh0f6BR5c8wzl$3EB9u4QXB0IQOwGiumUgJw8XrwmOWK45Jkjwk/hgLak=',NULL,'gyujeong6917@gmail.com','gyygygygygy',1,0,0,0,'2021-10-03 13:45:08.276594'),(14,'pbkdf2_sha256$260000$AaRmDJfNlznUyItU06s4cw$2sYRmylTEez/ADbO4e8zf0ZPYkClnpQ3720hFPBsrAg=',NULL,'jihwan@naver.com','지환',1,0,0,0,'2021-10-03 15:14:01.874541'),(15,'pbkdf2_sha256$260000$I5WxVRIoiyDVEsjNzD8gpC$4ZZ9LiyvQN1fGtUGcEnXpV5gfzelhg61ebS91YYHrbo=',NULL,'jihwan2@naver.com','지환2',1,0,0,0,'2021-10-03 16:18:26.769857'),(16,'pbkdf2_sha256$260000$s1BjJoTz3ys2fhc9JfAX2V$xL+3KKK1s3VL++rBfmCBjPNVuo3G/K4OS6ZkwaD6JoQ=',NULL,'sksgmlwlsl34@naver.com','힂',1,0,0,0,'2021-10-05 00:24:32.781245'),(17,'pbkdf2_sha256$260000$fhbmrBdRS8W2x5LMs4uwTz$+HyomA+pNUmo39OwJsSPda+a+XWh9zNJwKB/56feup4=',NULL,'sksgmlwlsl34@gmail.com','jhj',1,0,0,0,'2021-10-05 00:29:22.824276'),(18,'pbkdf2_sha256$260000$THOnIiRCBbxfVUXN69tBVI$9V4XbAVPLTyGi68SecukXfTFRgAkKaBwyQdO/rD8In4=',NULL,'yechan5@naver.com','찬ㅋㅋ',1,0,0,0,'2021-10-05 16:32:23.436057');
/*!40000 ALTER TABLE `accounts_user` ENABLE KEYS */;
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

-- Dump completed on 2021-10-07 16:43:22
