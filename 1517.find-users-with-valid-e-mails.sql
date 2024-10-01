-- https://leetcode.com/problems/find-users-with-valid-e-mails
SELECT *
FROM Users
-- WHERE mail LIKE '[a-z|A-Z][%a-z|A-Z|0-9|_|.|-]@leetcode.com'
-- WHERE mail REGEXP '^[:alpha:]([:alnum:]|_|\-|\.)*@leetcode\.com$'
WHERE mail REGEXP '^[:alpha:][A-Za-z0-9_\\-\\.]*@leetcode\\.com$'
-- WHERE mail REGEXP '^[A-Za-z][A-Za-z0-9_\.\-]*@leetcode\.com$'
-- WHERE mail REGEXP '^[:alpha:].*@leetcode.com$'
-- WHERE mail REGEXP '^[A-Za-z][A-Za-z0-9_\.\-]*@leetcode(\\?com)?\\.com$';