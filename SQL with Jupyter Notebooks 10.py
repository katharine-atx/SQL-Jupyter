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










