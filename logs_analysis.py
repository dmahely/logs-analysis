import psycopg2

# database name declared as a constant
DBNAME = 'dbname=news'

# takes a query and returns the results
def get_query_results(query):
    # connecting to the news database
    connection = psycopg2.connect(DBNAME)
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
print('"{}" - {} views').format(most_popular_articles[0][0], most_popular_articles[0][1])
print('"{}" - {} views').format(most_popular_articles[1][0], most_popular_articles[1][1])
print('"{}" - {} views').format(most_popular_articles[2][0], most_popular_articles[2][1])
