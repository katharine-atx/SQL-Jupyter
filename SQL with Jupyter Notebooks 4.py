# Jupyter notebooks with SQL queries

# Summarizing data with AVG(), COUNT(), MAX(), MIN(), SUM()

# Loading the SQL extension...
%load_ext sql

# Connecting to sample MySQL dataset via..
%sql mysql://studentuser:studentpw@mysqlserver/dognitiondb

# Designate this as the default database for queries this session...
%sql USE dognitiondb;

# Running a few summaries...
%%sql
SELECT breed
FROM dogs;
SELECT COUNT(breed)
FROM dogs;

%%sql
SELECT COUNT(DISTINCT breed)
FROM dogs;

# Note: Using COUNT(*) counts # of rows in entire table. There is no DISTINCT option. 

# How many individual dogs completed tests after March 1, 2014?
%%sql
SELECT COUNT(DISTINCT Dog_Guid)
FROM complete_tests
WHERE created_at > '2014-03-01';








