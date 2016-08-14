# Jupyter notebooks with SQL queries
# Dognition data analysis - factors to boost test completion

# Loading the SQL extension...
%load_ext sql
# Connecting to sample MySQL dataset via..
%sql mysql://studentuser:studentpw@mysqlserver/dognitiondb
# Designate this as the default database for queries this session...
%sql USE dognitiondb;

# Taking a look at factors hypothesized to impact test completion...

# Factor 1: Dog Personality Dimension. Distinct values...
# There are 11 values (including 'None').
%sql SELECT DISTINCT dimension FROM dogs;

# Preliminary query to sum tests completed for each dog...
%%sql
SELECT COUNT(ct.dog_guid) AS CompleteTests, d.dog_guid, d.dimension
FROM dogs d LEFT JOIN complete_tests ct ON d.dog_guid = ct.dog_guid 
WHERE dimension IS NOT NULL
GROUP BY d.dog_guid, d.dimension
LIMIT 1000;

# Nesting that query to summarize the average completed tests by dimension...
# "Expert" personality has the most, with "Socialite" the least on average.
%%sql
SELECT DogTests.dimension, AVG(DogTests.CompleteTests) AS AvgTestsComplete
FROM (
	SELECT COUNT(ct.dog_guid) AS CompleteTests, d.dog_guid, d.dimension
	FROM dogs d LEFT JOIN complete_tests ct ON d.dog_guid = ct.dog_guid 
	WHERE dimension IS NOT NULL
	GROUP BY d.dog_guid, d.dimension
	LIMIT 1000
	) AS DogTests
GROUP BY DogTests.dimension
ORDER BY AvgTestsComplete DESC;




