LOCK TABLES `EXPERIMENT_TYPE` WRITE;
/*!40000 ALTER TABLE `EXPERIMENT_TYPE` DISABLE KEYS */;
INSERT INTO `EXPERIMENT_TYPE` VALUES (1,'metatranscriptomic'),(2,'metagenomic'),(3,'amplicon'),(4,'assembly'),(5,'metabarcoding'),(6,'unknown');
/*!40000 ALTER TABLE `EXPERIMENT_TYPE` ENABLE KEYS */;
UNLOCK TABLES;