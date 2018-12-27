CREATE INDEX EMPindex_bitmap ON TABLE EmpSalary (salary) AS 'BITMAP' WITH DEFERRED REBUILD;

ALTER INDEX EMPindex_bitmap on EmpSalary REBUILD;

show formatted index on EmpSalary;

select AVG (salary) from EmpSalary;

DROP INDEX INDEX1 ON EmpSalary;

select AVG (salary) from EmpSalary;



