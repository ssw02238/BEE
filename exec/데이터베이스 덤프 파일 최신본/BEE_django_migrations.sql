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
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2021-09-21 12:20:31.910791'),(2,'contenttypes','0002_remove_content_type_name','2021-09-21 12:20:32.054965'),(3,'auth','0001_initial','2021-09-21 12:20:32.498356'),(4,'auth','0002_alter_permission_name_max_length','2021-09-21 12:20:32.595025'),(5,'auth','0003_alter_user_email_max_length','2021-09-21 12:20:32.620434'),(6,'auth','0004_alter_user_username_opts','2021-09-21 12:20:32.657750'),(7,'auth','0005_alter_user_last_login_null','2021-09-21 12:20:32.678399'),(8,'auth','0006_require_contenttypes_0002','2021-09-21 12:20:32.695038'),(9,'auth','0007_alter_validators_add_error_messages','2021-09-21 12:20:32.721492'),(10,'auth','0008_alter_user_username_max_length','2021-09-21 12:20:32.739106'),(11,'auth','0009_alter_user_last_name_max_length','2021-09-21 12:20:32.759192'),(12,'auth','0010_alter_group_name_max_length','2021-09-21 12:20:32.796067'),(13,'auth','0011_update_proxy_permissions','2021-09-21 12:20:32.833427'),(14,'auth','0012_alter_user_first_name_max_length','2021-09-21 12:20:32.862483'),(15,'accounts','0001_initial','2021-09-21 12:20:33.449258'),(16,'admin','0001_initial','2021-09-21 12:20:33.683802'),(17,'admin','0002_logentry_remove_auto_add','2021-09-21 12:20:33.713504'),(18,'admin','0003_logentry_add_action_flag_choices','2021-09-21 12:20:33.734619'),(19,'corporates','0001_initial','2021-09-21 12:20:34.071116'),(20,'sessions','0001_initial','2021-09-21 12:20:34.166197'),(21,'corporates','0002_auto_20210923_1443','2021-09-23 14:44:01.802513'),(22,'corporates','0003_social_woman_ratio','2021-09-24 17:00:04.024065'),(23,'corporates','0004_auto_20210927_1608','2021-09-27 16:08:51.499149'),(24,'corporates','0004_rename_board_ration_governance_board_ratio','2021-09-28 10:48:46.658075'),(25,'corporates','0005_merge_20210928_1158','2021-09-28 11:58:24.418319'),(26,'accounts','0002_auto_20210928_1203','2021-09-28 12:03:53.100163'),(27,'accounts','0003_rename_s_sore_user_s_score','2021-09-29 17:02:45.990219'),(28,'corporates','0006_auto_20210930_1414','2021-09-30 14:14:26.915324'),(29,'corporates','0007_auto_20210930_1544','2021-09-30 15:45:06.694120'),(30,'corporates','0008_auto_20211001_1057','2021-10-01 10:57:57.915449'),(31,'accounts','0004_auto_20211001_1118','2021-10-01 11:18:47.942569'),(32,'accounts','0005_auto_20211001_1348','2021-10-01 13:48:17.829081'),(33,'corporates','0009_news_evaluation','2021-10-01 13:49:09.953544'),(34,'corporates','0010_alter_governance_board_independency','2021-10-01 16:19:35.680515'),(35,'corporates','0011_alter_news_url','2021-10-02 14:39:18.038679'),(36,'corporates','0012_auto_20211005_1147','2021-10-05 11:47:10.375946');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
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

-- Dump completed on 2021-10-07 16:43:23
