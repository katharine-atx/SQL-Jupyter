# Jupyter notebooks with SQL queries
# Logical functions...

# Loading the SQL extension...
%load_ext sql

# Connecting to sample MySQL dataset via..
%sql mysql://studentuser:studentpw@mysqlserver/dognitiondb

# Designate this as the default database for queries this session...
%sql USE dognitiondb;

# Example: IF statement to create conditional "flags" and then count by flag category...
# User type flag: early user v. late user
%%sql
SELECT IF(cleaned_users.first_account < '2014-06-01','early_user','late_user') AS user_type,
	COUNT(cleaned_users.first_account)
FROM (
	SELECT user_guid, MIN(created_at) AS first_account 
	FROM users
	GROUP BY user_guid
	) AS cleaned_users
GROUP BY user_type;

# Pulling the count of distinct users for each country...
%%sql
SELECT country, count(DISTINCT user_guid) AS Users
FROM users
WHERE user_guid IS NOT NULL AND country IS NOT NULL
GROUP BY country
HAVING country != 'N/A'
ORDER BY Users DESC;

# Vast majority of users are in the U.S. 
# Structuring a query to compare U.S. v. Other user count...
%%sql
SELECT IF(
	country = 'US', 'United States', 'Other'
	) AS US_flag, 
	count(DISTINCT user_guid) AS Users
FROM users
WHERE user_guid IS NOT NULL AND country IS NOT NULL
	AND country != 'N/A'
GROUP BY US_flag;

# Nested IF to break out a third category for "N/A" country records:
%%sql
SELECT IF( 
	country = 'US', 'United States', IF(
		country = 'N/A', 'N/A', 'Other')
	) AS US_flag, 
	count(DISTINCT user_guid) AS Users
FROM users
WHERE user_guid IS NOT NULL AND country IS NOT NULL
GROUP BY US_flag
ORDER BY Users DESC;

# Another way to "fill" a flag column is with CASE WHEN. 
# Same output as above:
%%sql
SELECT CASE country 
	WHEN 'US' THEN 'United States'
	WHEN 'N/A' THEN 'N/A'
	ELSE 'Other'
	END AS US_Flag,
	COUNT(DISTINCT user_guid) AS Users
FROM users
WHERE country IS NOT NULL
GROUP BY US_Flag
ORDER BY Users DESC;

# Note: ELSE is optional and defaults to NULL.
# 'Neutered' outputs NULL values where dog_fixed column is NULL:
%%sql
SELECT dog_guid, dog_fixed, CASE dog_fixed
    WHEN 1 THEN 'Neutered'
    WHEN 0 THEN 'Not Neutered'
    END AS Neutered
FROM dogs
LIMIT 20;

# Adding a flag description field for 'Exclude' column...
%%sql
SELECT dog_guid, exclude, CASE exclude 
    WHEN 1 THEN 'Exclude'
    ELSE 'Keep'
    END AS exclude_flag
FROM dogs
LIMIT 20;
# Same as above, using an IF statement v. CASE WHEN:
%%sql
SELECT dog_guid, exclude, IF(
    exclude = 1, 'Exclude', 'Keep'
    )AS exclude_flag
FROM dogs
LIMIT 20;

# Creating a dog weight category field...
%%sql
SELECT dog_guid, weight, CASE
	WHEN weight>=1 AND weight<=10 THEN 'Very Small'
	WHEN weight>10 AND weight<=30 THEN 'Small'
	WHEN weight>30 AND weight<=50 THEN 'Medium'
	WHEN weight>50 AND weight<=85 THEN 'Large'
	WHEN weight>85 THEN 'Very Large'
	END AS Size
FROM dogs
LIMIT 20;

# Note: Order of operations is NOT > AND > OR when used together.
# For example - the () within the CASE WHEN are necessary here:
SELECT COUNT(DISTINCT dog_guid), 
CASE WHEN exclude!='1' AND (breed_group='Sporting' OR breed_group='Herding') THEN "group 1"
     ELSE "everything else"
     END AS group_name
FROM dogs
GROUP BY group_name;

# Summarizing the number of completed tests per dog...
%%sql
SELECT d.dog_guid, d.breed_type, COUNT(DISTINCT test_name) AS TestsComplete
FROM dogs d LEFT JOIN complete_tests ct ON d.dog_guid = ct.dog_guid
GROUP BY d.dog_guid, d.breed_type
ORDER BY TestsComplete DESC
LIMIT 50;
	
# Outputting the average for each breed group...
%%sql
SELECT TestsPerDog.breed_type, AVG(TestsPerDog.TestsComplete) AS AvgTestsComplete
FROM (
	SELECT d.dog_guid, d.breed_type, COUNT(DISTINCT test_name) AS TestsComplete
	FROM dogs d LEFT JOIN complete_tests ct ON d.dog_guid = ct.dog_guid
	GROUP BY d.dog_guid, d.breed_type
	LIMIT 1000) AS TestsPerDog
GROUP BY TestsPerDog.breed_type
ORDER BY AvgTestsComplete DESC;

# Reporting on users by US top regions v. "other"...
%%sql
SELECT CASE
    WHEN state IN ('NY', 'NJ') THEN 'New York/New Jersey'
    WHEN state IN ('NC', 'SC') THEN 'Carolinas'
    WHEN state = 'CA' THEN 'California'
    ELSE 'Other'
    END AS Region, 
    COUNT(DISTINCT user_guid) AS Users
FROM users
WHERE country = 'US' AND state IS NOT NULL
GROUP BY Region;







