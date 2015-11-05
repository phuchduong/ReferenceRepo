#changing a table name
ALTER TABLE name RENAME TO new_name

        #example: renames a hive table called irisData to iris.
        ALTER TABLE irisData RENAME TO iris

#creating a blank table for emploees.
CREATE TABLE IF NOT EXISTS employee (
        EmpID int, 
        EmployeeName String, 
        Salary String, 
        Department String
) 
COMMENT 'Employee Details'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n'
STORED AS TEXTFILE;

# IF NOT EXISTS, an optional parameter, 
# Hive ignores the statement in case the table 

        #creates hive table for iris data.
CREATE TABLE IF NOT EXISTS iris (
        SepalLengthCM float, 
        SepalWidthCM float,
        PetalLengthCM float,
        PetalWidthCM float,
        IrisType String
) 
COMMENT 'Iris Dataset from UCI'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
STORED AS TEXTFILE;

#load data into a table, won't work in query console for HDInsight. must upload to blob storage.
LOAD DATA [LOCAL] INPATH 'filepath' [OVERWRITE] INTO TABLE tablename
        
        #example
        LOAD DATA [LOCAL] INPATH 'C:\\Users\\PhucHDuong\\Documents\\DSD Working Folder\\Azure\\Hive\\iris.data.csv' [OVERWRITE] INTO TABLE irisData

#view all hive tables within the HDFS
SHOW TABLES;

#view the metadata of the given hive table
DESCRIBE iris;

#view header for table
set hive.cli.print.header=true;

#turns on apache tez. Allows HDInsight to run hive queries faster.
set hive.execution.engine=tez;