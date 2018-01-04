#!/usr/lib python2.7

import psycopg2
import datetime

db = psycopg2.connect("dbname=news")

cur = db.cursor()

# Question 1
cur.execute("SELECT REPLACE(REPLACE(path, 'article', ''), '/', ''), count(*) as topthings \
            FROM log WHERE path != '/' \
            GROUP BY path \
            ORDER BY topthings \
            DESC LIMIT(3);")
logs = cur.fetchall()
print '\nQuestion 1\n'
for l in logs:
    print l[0] + ' - ' + str(l[1]) + ' views'

# Question 2
cur.execute("SELECT authors.name, count(log.path) \
            AS reads FROM articles \
            INNER JOIN log \
            ON articles.slug=REPLACE \
            (REPLACE(log.path, 'article', ''), '/', '') \
            INNER JOIN authors on articles.author = authors.id \
            WHERE log.path != '/' \
            GROUP BY authors.name, articles.author \
            ORDER BY reads DESC;")
topAuthors = cur.fetchall()
print '\nQuestion 2\n'
for author in topAuthors:
    print author[0] + ' - ' + str(author[1]) + ' views'

# Question 3
cur.execute("SELECT date_trunc('day', time) AS day, \
            ROUND((TotErrors.errors*100/TotRequests.requests::numeric), 2) \
            AS percent_req_err FROM log, \
            (SELECT date_trunc('day', log.time) \
                AS timestamp, count(date_trunc('day', log.time)) \
                    AS requests FROM log GROUP BY timestamp) \
            AS TotRequests, \
            (SELECT date_trunc('day', log.time) \
                AS timestamp, count(date_trunc('day', log.time)) \
                    AS errors FROM log \
                        WHERE status != '200 OK' GROUP BY timestamp) \
            AS TotErrors \
            WHERE date_trunc('day', log.time) = TotRequests.timestamp \
            AND \
            date_trunc('day', log.time) = TotErrors.timestamp \
            AND \
            TotErrors.errors/TotRequests.requests::float >= 0.01 \
            GROUP BY day, TotErrors.errors, TotRequests.requests \
            ORDER BY day;")
errorPercentages = cur.fetchall()
print '\nQuestion 3\n'
for error in errorPercentages:
    print error[0].strftime("%B %d, %Y") + ' - ' + str(error[1]) + '% errors'

cur.close()
db.close()
