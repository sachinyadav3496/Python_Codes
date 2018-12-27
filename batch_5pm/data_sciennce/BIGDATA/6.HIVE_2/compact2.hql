CREATE TABLE IF NOT EXISTS EmpSalary (id INT, name VARCHAR(64), salary INT, department VARCHAR(64)) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' STORED AS TEXTFILE;

LOAD DATA LOCAL INPATH 'users.txt' INTO TABLE EmpSalary;

CREATE INDEX INDEX1 ON TABLE EmpSalary (salary) AS org.apache.hadoop.hive.ql.index.compact.CompactIndexHandler' WITH DEFERRED REBUILD;

ALTER INDEX INDEX1 on EmpSalary REBUILD;
show formatted index on EmpSalary;

select AVG (salary) from EmpSalary;

DROP INDEX INDEX1 ON EmpSalary;

select AVG (salary) from EmpSalary;
