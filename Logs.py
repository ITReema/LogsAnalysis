#!/usr/bin/env python3

import psycopg2

DBNAME = "news"

Question1 = "1. What are the most popular three articles of all time?"
query1 = '''SELECT title, COUNT(*) AS views
FROM articles, log
WHERE articles.slug = SUBSTR(log.path, 10) GROUP BY title
ORDER BY views DESC LIMIT 3;'''

Question2 = "2. Who are the most popular article authors of all time?"
query2 = '''SELECT name, COUNT(*) AS views
FROM authors, articles, log
WHERE articles.slug = SUBSTR(log.path,10) AND articles.author = authors.id
GROUP BY name
ORDER BY views DESC;'''

Question3 = "3. On which days did more than 1% of requests lead to errors?"
query3 = "SELECT date , percentage from rate WHERE percentage > 1;"


def get_query(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results

result1 = get_query(query1)
result2 = get_query(query2)
result3 = get_query(query3)


def print_query1(results):
    for i in range(len(results)):
        title = results[i][0]
        views = results[i][1]
        print("\t" + "%s - %d" % (title, views) + " views")
    print("\n")

print(Question1)
print_query1(result1)


def print_query2(results):
    for i in range(len(results)):
        name = results[i][0]
        views = results[i][1]
        print("\t" + "%s - %d" % (name, views) + "views")
    print("\n")

print(Question2)
print_query2(result2)


def print_query3(results):
    for i in range(len(results)):
        date = results[i][0]
        errors = results[i][1]
        print("\t" + "%s - %.1f%%" % (date, errors) + " errors")
    print("\n")

print(Question3)
print_query3(result3)

