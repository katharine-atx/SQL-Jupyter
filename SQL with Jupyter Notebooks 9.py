# Jupyter notebooks with SQL queries
# Subqueries and derived tables...

# Loading the SQL extension...
%load_ext sql

# Connecting to sample MySQL dataset via..
%sql mysql://studentuser:studentpw@mysqlserver/dognitiondb

# Designate this as the default database for queries this session...
%sql USE dognitiondb;

# Notes: Subqueries can be used in SELECT, WHERE, and FROM clauses. 
# In FROM clauses they create "derived" tables.
# ORDER BY phrases cannot be used within subqueries.
# Subqueries in SELECT/WHERE clauses that return >1 row must 
# be used with operators that handle multiple values, i.e. IN 
# or they'll be limited to outputting 1 row.

# Example: Selecting values that are greater than average ...
%%sql
SELECT *
FROM exam_answers
WHERE test_name = 'Yawn Warm-Up'
AND TIMESTAMPDIFF(minute,start_time,end_time) > (
    SELECT AVG(TIMESTAMPDIFF(minute,start_time,end_time))
    FROM exam_answers
    WHERE TIMESTAMPDIFF(minute,start_time,end_time) > 0 
	AND test_name = 'Yawn Warm-Up'
);

# Examples with IN, NOT IN, EXISTS, NOT EXISTS...

%%sql
SELECT COUNT(*)
FROM exam_answers
WHERE subcategory_name IN ('Puzzles', 'Numerosity', 'Bark Game');








