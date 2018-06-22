# Logs Analysis 
_This project was made specifically for Udacity’s Full Stack Web Developer Nanodegree._
This project uses python and SQL to analyze the news database, a database supplied to me by Udacity.

# Running the Program
1. Install VirtualBox
2. Install vagrant
3. Download this config file
4. Run `vagrant up`
5. Run `vagrant ssh`
6. Create a view by running the following query:
`SELECT title AS article_title, COUNT(*) AS views
FROM articles a
JOIN log l
ON l.path LIKE concat('%', a.slug) 
GROUP BY title
ORDER BY views DESC
LIMIT 3;`
7. Create a second view by running the following query:
``
8. Create a final view by running the following query:
``
9. Open the terminal app on your mac or the command prompt on your Windows machine and 