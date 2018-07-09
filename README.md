# Logs Analysis
_This project was made specifically for Udacity’s Full Stack Web Developer Nanodegree._
This project uses Python and SQL in order to answer three analytical questions about a fictional newspaper's logs.

# Before Running the Program
You must have Python installed on your machine. Check your Python version by running `python -V`.

# Running the Program
1. Install [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
2. Install [Vagrant](https://www.vagrantup.com)
3. Download [this config file](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip) named `FSND-Virtual-Machine`
4. Navigate to the `vagrant` directory inside of `FSND-Virtual-Machine`
5. Open the terminal app on your Mac or the command prompt on your Windows machine and run `vagrant up`
6. Run `vagrant ssh`
7. Navigate to `/vagrant` by running `cd /vagrant`
8. Run `psql news`
9. Create a view by running the following query:
`CREATE VIEW article_views AS
SELECT title AS article_title, COUNT(*) AS views
FROM articles a
JOIN log l
ON l.path LIKE concat('%', a.slug)
GROUP BY title
ORDER BY views DESC
LIMIT 3;`
10. Create a view by running the following query:
`CREATE VIEW author_views AS
SELECT authors.name, COUNT(log.path) AS total_views
FROM authors
JOIN articles
ON authors.id = articles.author
JOIN log
ON log.path LIKE concat('%', articles.slug)
GROUP BY authors.name
ORDER BY COUNT(log.path) DESC;`
11. Create a view by running the following query:
`CREATE VIEW all_requests AS
SELECT DATE_TRUNC('day', time) AS day, COUNT(*)
FROM log
WHERE status = '200 OK' OR status = '404 NOT FOUND'
GROUP BY day;`
12. Create a view by running the following query:
`CREATE VIEW failed_requests AS
SELECT DATE_TRUNC('day', time) AS day, COUNT(*)
FROM log
WHERE status = '404 NOT FOUND'
GROUP BY day;`
13. Create a view by running the following query:
`CREATE VIEW error_percentage AS
SELECT a.day, (f.count::double precision/a.count::double precision) * 100 AS percentage
FROM all_requests a, failed_requests f
WHERE a.day = f.day;`
14. Clone this repository to your local machine by clicking on the green `Clone or Download` button and place it inside `FSND-Virtual-Machine/vagrant`
15. Run `python logs-analysis.py`

# After Running the Program
Running the program will create a new text file (or modify an existing one if found) called `output.txt` in `/vagrant`. This file contains the answers to the three questions in plain text.

# Acknowledgements
The news database was supplied to me by Udacity. Everything else is my work.
