# Jupyter notebooks with SQL queries

# Note - the ; is not necessary for a single query but is when chaining multiple queries.

# Loading the SQL extension...
%load_ext sql;

# Connecting to sample MySQL dataset via..
%sql mysql://studentuser:studentpw@mysqlserver/dognitiondb

# Designate this as the default database for queries this session...
%sql USE dognitiondb;

# Take a look at which tables are included for this database...
%sql SHOW tables;

# Note: the syntax, which sounds very similar to what you would actually say in the spoken English language, looks like this:
## SHOW columns FROM (enter table name here)
## or if you have multiple databases loaded:
## SHOW columns FROM (enter table name here) FROM (enter database name here)
## or
## SHOW columns FROM databasename.tablename

# The dogs table has 21 columns...
%sql SHOW columns FROM dogs;
# OR for identical output in this case...
%sql DESCRIBE dogs;

# Note: Table or column names with spaces in them need to be surrounded by quotation marks in SQL. 
# MySQL accepts both double and single quotation marks, but some database systems only accept single 
# quotation marks. In all database systems, if a table or column name contains an SQL keyword, the 
# name must be enclosed in backticks instead of quotation marks.





