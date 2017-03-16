-- MySQL dump 10.13  Distrib 5.7.12, for osx10.9 (x86_64)
--
-- Host: 127.0.0.1    Database: centuriondb
-- ------------------------------------------------------
-- Server version	5.6.34

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
-- Table structure for table `ErrorsDict_errorsdict`
--

DROP TABLE IF EXISTS `ErrorsDict_errorsdict`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ErrorsDict_errorsdict` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Error_name` longtext NOT NULL,
  `Error_reportDate` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=76 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ErrorsDict_errorsdict`
--

LOCK TABLES `ErrorsDict_errorsdict` WRITE;
/*!40000 ALTER TABLE `ErrorsDict_errorsdict` DISABLE KEYS */;
INSERT INTO `ErrorsDict_errorsdict` VALUES (1,'java.lang.NullPointerException','2016-07-31'),(2,'[com.gravitant.cloud.appsportfolio.jsf.architecture.beans.ResourceGroupConfigurationBean]','2016-07-31'),(3,'[com.gravitant.cloud.async.mdb.RePriceAsyncTasksConsumerMDB]','2016-07-31'),(4,'[com.gravitant.bms.common.policyframework.engine.PolicyEngineLogger]','2016-07-31'),(5,'[com.gravitant.cloud.async.mdb.VdcSyncConsumerMDB]','2016-07-31'),(6,'[com.gravitant.cloud.appsportfolio.jsf.architecture.beans.ResourceGroupBean]','2016-07-31'),(7,'[org.thymeleaf.TemplateEngine]','2016-07-31'),(8,'[com.gravitant.cloud.core.services.email.ApplicationEmailMDB]','2016-07-31'),(9,'[com.gravitant.softlayer.server.pricing.PricingEngineHandler]','2016-07-31'),(10,'[com.gravitant.cloud.appsportfolio.jsf.architecture.actions.AddResourceGroupHandler]','2016-07-31'),(11,'[com.gravitant.bms.common.util.AbstractRestBase]','2016-07-31'),(12,'[com.gravitant.cloud.appsportfolio.jsf.architecture.beans.ResourceGroupConfigurationBean]','2016-07-31'),(13,'[com.gravitant.cloud.appsportfolio.jsf.architecture.beans.ResourceGroupDetailsBean]','2016-07-31'),(14,'javax.ejb.EJBException: com.gravitant.bts.bms.exception.GraException: Display Message:Transaction commit failed','2016-07-31'),(15,'Failed in refresh: : java.lang.NullPointerException','2016-07-31'),(16,'[com.gravitant.bts.bms.exception.GraBmsRuntimeException]','2016-07-31'),(17,'[com.gravitant.bms.billing.service.estimation.BillEstimationService]','2016-07-31'),(18,'centuriondb.ErrorsDict_errorsdict(Error_name) [stderr] (EJB default','2016-07-31'),(19,'[com.gravitant.bms.sync.impl.centuriondb.ErrorsDict_errorsdict(Error_name)s.NoTemplatecenturiondb.ErrorsDict_errorsdict(Error_name)Processor]','2016-07-31'),(20,'[com.gravitant.bts.bms.exception.GraBmsRuntimeException]','2016-07-31'),(21,'[com.gravitant.cloud.orders.broker.controller.BrokerOrderController]','2016-07-31'),(22,'[org.thymeleaf.TemplateEngine]','2016-07-31'),(23,'[com.gravitant.bms.engine.PricingBase]','2016-07-31'),(24,'[com.gravitant.cloud.common.jsf.core.beans.ActivityLoggerTableListBean]','2016-07-31'),(25,'[com.gravitant.bms.common.policyframework.policyProvider.bootScript.BootScriptConsumer]','2016-07-31'),(26,'[com.gravitant.cloud.async.mdb.AsyncTasksConsumerMDB]','2016-07-31'),(27,'[com.gravitant.cloud.appsportfolio.jsf.architecture.beans.StorageAccountBean]','2016-07-31'),(28,'[com.gravitant.bms.common.planning.util.BmsProvisioningHelper]','2016-07-31'),(29,'javax.faces.FacesException: Cannot add the same component twice: architectureMainContentForm:menuBarArch','2016-07-31'),(30,'java.lang.Exception: Invalid Context Code - APP','2016-07-31'),(31,'centuriondb.ErrorsDict_errorsdict(Error_name)  [com.arjuna.ats.arjuna]','2016-07-31'),(32,'java.lang.Exception: Invalid Context Code - VDC','2016-07-31'),(33,'centuriondb.ErrorsDict_errorsdict(Error_name) [com.gravitant.azure.client.service.AzureComputeService]','2016-07-31'),(34,'centuriondb.ErrorsDict_errorsdict(Error_name) [com.gravitant.cloud.adapters.provision.providers.AmazonEC2]','2016-07-31'),(35,'[com.gravitant.bms.common.planning.util.BmsOrderConsolidationHelper]','2016-07-31'),(36,'[com.gravitant.azure.client.service.AzureComputeService]','2016-07-31'),(37,'[org.picketlink.identity.federation]','2016-07-31'),(38,'[com.gravitant.bts.bms.transaction.BTSTransaction]','2016-07-31'),(39,'Failure in initialisation: java.lang.NullPointerException','2016-07-31'),(40,'centuriondb.ErrorsDict_errorsdict(Error_name) [com.gravitant.cloud.userapp.proxy.impl.ejb.WhiteLabelInfoProxyEjb]','2016-07-31'),(41,'centuriondb.ErrorsDict_errorsdict(Error_name) [org.apache.catalina.core.ContainerBase.[jboss.web]','2016-07-31'),(42,'centuriondb.ErrorsDict_errorsdict(Error_name) [org.jboss.naming.remote.protocol.v1.RemoteNamingStoreV1]','2016-07-31'),(43,'[com.gravitant.bms.sync.util.BmsVdcSyncHelper]','2016-07-31'),(44,'centuriondb.ErrorsDict_errorsdict(Error_name) [com.gravitant.cloud.core.jsf.helpers.CmwSecurity]','2016-07-31'),(45,'[org.hibernate.engine.jdbc.spi.SqlExceptionHelper]','2016-07-31'),(46,'java.lang.IndexOutOfBoundsException','2016-07-31'),(47,'[com.gravitant.cloud.providerservices.proxy.impl.ejb.ProviderManagementProxyEjb]','2016-07-31'),(48,'[com.gravitant.cloud.appsportfolio.jsf.architecture.actions.AddResourceGroupHandler]','2016-07-31'),(49,'[com.gravitant.cloud.common.proxy.impl.ejb.ProviderAccountProxyEjb]','2016-07-31'),(50,'Failed to scanAndUpdateResources data: javax.persistence.OptimisticLockException: Row was updated or deleted by another transaction','2016-07-31'),(51,'[com.gravitant.bts.bms.util.BmsBaseFindersUtil]','2016-07-31'),(52,'com.mysql.jdbc.jdbc2.optional.MysqlXAException: XAER_OUTSIDE: Some work is done outside global transaction','2016-07-31'),(53,'Could not initialize storage provider proxy','2016-07-31'),(54,'[com.gravitant.bts.bms.topology.Topology]','2016-07-31'),(55,'[org.hibernate.engine.jdbc.spi.SqlExceptionHelper]','2016-07-31'),(56,'centuriondb.ErrorsDict_errorsdict(Error_name) [org.hibernate.engine.jdbc.spi.SqlExceptionHelper]','2016-07-31'),(57,'[org.hibernate.engine.jdbc.batch.internal.AbstractBatchImpl]','2016-07-31'),(58,'[com.gravitant.azure.client.service.AzureComputeService]','2016-07-31'),(59,'[org.hibernate.engine.jdbc.batch.internal.AbstractBatchImpl]','2016-07-31'),(60,'centuriondb.ErrorsDict_errorsdict(Error_name) while getting Work Flow Service Task OrderId for asyncTaskId','2016-07-31'),(61,'[com.gravitant.azure.client.service.AzureComputeService]','2016-07-31'),(62,'[com.gravitant.bms.sync.impl.DeleteVMResultProcessor]','2016-07-31'),(63,'[com.gravitant.bms.sync.util.BmsVdcSyncHelper]','2016-07-31'),(64,'[com.gravitant.bts.bms.topology.Topology]','2016-07-31'),(65,'[com.gravitant.cloud.timer.beans.TimerBean]','2016-07-31'),(66,'[org.hibernate.engine.jdbc.batch.internal.AbstractBatchImpl]','2016-07-31'),(67,'[org.jboss.as.ejb3.invocation]','2016-07-31'),(68,'[org.hibernate.engine.jdbc.spi.SqlExceptionHelper]','2016-07-31'),(69,'[com.gravitant.azure.adapter.provider.AzureProvider]','2016-07-31'),(70,'[com.gravitant.azure.client.service.AzureComputeService]','2016-07-31'),(71,'[com.gravitant.bms.common.planning.util.BmsWorkflowHelper]','2016-07-31'),(72,'[com.gravitant.cloud.appsportfolio.jsf.architecture.beans.AddResourceGroupBean]','2016-07-31'),(73,'[com.gravitant.cloud.common.proxy.impl.ejb.ProviderAccountProxyEjb]','2016-07-31'),(74,'[com.gravitant.cloud.core.jsf.beans.ExceptionDisplayContentBean]','2016-07-31'),(75,'[org.jboss.naming.remote.protocol.v1.RemoteNamingStoreV1]','2016-07-31');
/*!40000 ALTER TABLE `ErrorsDict_errorsdict` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-03-16 23:52:56
