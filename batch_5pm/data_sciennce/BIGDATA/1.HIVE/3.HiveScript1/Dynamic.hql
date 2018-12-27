set hive.exec.dynamic.partition=true;
set hive.exec.dynamic.partition.mode=nonstrict;
set hive.exec.max.dynamic.partitions=1000;
set hive.exec.max.dynamic.partitions.pernode=1000;

DROP TABLE IF EXISTS partitioned_user;
 
CREATE TEMPORARY TABLE temp_user(
firstname VARCHAR(64),
lastname  VARCHAR(64),
address   STRING,
country   VARCHAR(64),
city      VARCHAR(64),
state     VARCHAR(64),
post      STRING,
phone1    VARCHAR(64),
phone2    STRING,
email     STRING,
web       STRING
)
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
STORED AS TEXTFILE;
 
LOAD DATA LOCAL INPATH '/home/cloudera/Desktop/text.hql' INTO TABLE temp_user;
 
SELECT firstname, phone1, city 
FROM temp_user 
WHERE country='US' AND state='CA' 
ORDER BY city 
LIMIT 5;

CREATE TABLE partitioned_user(
firstname VARCHAR(64),
lastname  VARCHAR(64),
address   STRING,
city 	  VARCHAR(64),
post      STRING,
phone1    VARCHAR(64),
phone2    STRING,
email     STRING,
web       STRING
)
PARTITIONED BY (country VARCHAR(64), state VARCHAR(64))
STORED AS SEQUENCEFILE;


INSERT INTO TABLE partitioned_user
PARTITION (country, state)
SELECT  firstname ,
lastname  ,
address   ,
city      ,
post      ,
phone1    ,
phone2    ,
email     ,
web       ,
country   ,
state     
FROM temp_user;

SELECT firstname, phone1, city 
FROM partitioned_user 
WHERE country='US' AND state='CA' 
ORDER BY city 
LIMIT 5;		
