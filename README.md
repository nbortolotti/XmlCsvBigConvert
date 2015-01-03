XmlCsvBigConvert
================
This is a tool to convert xml large files to csv files. The goal is process large xml files to model this information into #BigQuery.
The model processing tool locates the set of repetitive data and then works with the attributes of this node.
example:
```<?xml version="1.0" encoding="utf-8"?>
     <users(iterative row-node )> 
      <row (interative row) [attribute 1], [attribute 2]....```

- Nicolas Bortolotti, 2014
- License: Apache 2.0

##Commandline utilities
###Arguments
--input 	input XML document's filename*
--output 	output CSV file's filename*
--row 		identify the node in the xml file (iterative)*
--schema 	xml-csv schema
