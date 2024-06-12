# MySQL advanced
## 0-uniq_users.sql
Write a SQL script that creates a table users following these requirements:

With these attributes:
* id, integer, never null, auto increment and primary key
* email, string (255 characters), never null and unique
* name, string (255 characters)
* If the table already exists, your script should not fail
* Your script can be executed on any database
Context: Make an attribute unique directly in the table schema will enforced your business rules and avoid bugs in your application
## 1-country_users.sql
In the above table add the following attribute
* country, enumeration of countries: US, CO and TN, never null (= default will be the first element of the enumeration, here US)
