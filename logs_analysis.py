#!/usr/bin/env python3
import psycopg2


# database name declared as a constant
DBNAME = 'dbname=news'
# creates and opens a text file called output
output = open('output.txt', 'w')


# takes a query and returns the results
def get_query_results(query):
    # connecting to the news database, prints error if connection fails
    try:
        connection = psycopg2.connect(DBNAME)
    except psycopg2.Error as e:
        print e.pgerror
        print 'Unable to connect'
    else:
        print 'Connected'
    # creating a cursor
    cursor = connection.cursor()
    # executing the passed query
    cursor.execute(query)
    # getting the results
    results = cursor.fetchall()
    # closing the connection
    connection.close()
    # returning results of query
    return results


# PART ONE:  What are the most popular three articles of all time?
article_views = 'SELECT * FROM article_views;'
most_popular_articles = get_query_results(article_views)
output.write('The most popular three articles of all time are: \n')
output.write('* "' + most_popular_articles[0][0] + '" - ')
output.write(str('{:,}'.format(most_popular_articles[0][1])) + ' views\n')
output.write('* "' + most_popular_articles[1][0] + '" - ')
output.write(str('{:,}'.format(most_popular_articles[1][1])) + ' views\n')
output.write('* "' + most_popular_articles[2][0] + '" - ')
output.write(str('{:,}'.format(most_popular_articles[2][1])) + ' views\n')

# PART TWO: Who are the most popular article authors of all time?
author_views = 'SELECT * FROM author_views;'
most_popular_authors = get_query_results(author_views)
output.write('\nThe most popular article authors of all time are: \n')
output.write('* ' + most_popular_authors[0][0] + ' - ')
output.write(str('{:,}'.format(most_popular_authors[0][1])) + ' views\n')
output.write('* ' + most_popular_authors[1][0] + ' - ')
output.write(str('{:,}'.format(most_popular_authors[1][1])) + ' views\n')
output.write('* ' + most_popular_authors[2][0] + ' - ')
output.write(str('{:,}'.format(most_popular_authors[2][1])) + ' views\n')
output.write('* ' + most_popular_authors[3][0] + ' - ')
output.write(str('{:,}'.format(most_popular_authors[3][1])) + ' views\n')

# PART THREE: On which days did more than 1% of requests lead to errors?
error_percentage = ('SELECT TO_CHAR(day, \'fmMonth dd, YYYY\'), percentage'
                    ' FROM error_percentage WHERE percentage > 1;')
most_error_days = get_query_results(error_percentage)
output.write('\nThe days on which more than 1% of requests')
output.write('lead to errors are: \n')
output.write('* ' + str(most_error_days[0][0]) + ' - ')
output.write(str(round(most_error_days[0][1], 1)) + '% errors')

# closes the output text file
output.close()
