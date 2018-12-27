CREATE TABLE partitioned_user(
firstname VARCHAR(64),
lastname VARCHAR(64),
address STRING,
city VARCHAR(64),
post STRING,
phone1 VARCHAR(64),
phone2 STRING,
email STRING,
web STRING
)
PARTITIONED BY (country VARCHAR(64), state VARCHAR(64))
STORED AS TEXTFILE;

LOAD DATA LOCAL INPATH '/home/cloudera/Desktop/Partition' into table partitioned_user
PARTITION (country='US', state='CA');

