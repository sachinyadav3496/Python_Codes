CREATE TABLE IF NOT EXISTS EmpSalary2 (id INT, name VARCHAR(64), salary INT, department VARCHAR(64)) row format serde 'org.apache.hadoop.hive.contrib.serde2.MultiDelimitSerDe' with SERDEPROPERTIES ("field.delim"="[,/|]") stored as textfile;

load data local inpath'users.txt' into table EmpSalary2;

select * from EmpSalary;
