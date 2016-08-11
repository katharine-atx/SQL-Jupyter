# Jupyter notebooks with SQL queries
# Outer joins...JOIN..ON clause

# Loading the SQL extension...
%load_ext sql

# Connecting to sample MySQL dataset via..
%sql mysql://studentuser:studentpw@mysqlserver/dognitiondb

# Designate this as the default database for queries this session...
%sql USE dognitiondb;

# Here's how to write an INNER join with JOIN...ON syntax:
# NOTE: You can specify "INNER JOIN" for clarity but it's assumed.
%%sql
SELECT d.user_guid AS UID, d.dog_guid AS DID, d.breed
FROM dogs d JOIN complete_tests c ON d.dog_guid=c.dog_guid
WHERE test_name='Yawn Warm-up'
LIMIT 10;

# An outer join example with RIGHT to look at reviewed dogs missing from the dogs table...
%%sql
SELECT r.dog_guid AS rDogID, d.dog_guid AS dDogID, r.user_guid AS rUserID, d.user_guid AS dUserID, AVG(r.rating) AS AvgRating, COUNT(r.rating) AS NumRatings, d.breed, d.breed_group, d.breed_type
FROM dogs d RIGHT JOIN reviews r
  ON r.dog_guid=d.dog_guid AND r.user_guid=d.user_guid
WHERE d.dog_guid IS NULL
GROUP BY r.dog_guid
HAVING NumRatings >= 10
ORDER BY AvgRating DESC;