import pandas as pd
import sqlite3


df = pd.read_csv(r'C:\Users\keith\Desktop\GH\DS-Unit-3-Sprint-2-SQL-and-Databases\module1-introduction-to-sql\buddymove_holidayiq.csv')

connection = sqlite3.connect(r'C:\Users\keith\Desktop\GH\DS-Unit-3-Sprint-2-SQL-and-Databases\module1-introduction-to-sql\buddymove_holidayiq.sqlite3')

cursor = connection.cursor()

df.to_sql('reviews',connection)

df.head()

query = 'SELECT COUNT (*) FROM reviews;'
result2 = cursor.execute(query).fetchone()
print ('amount of rows:',result2[0])

query = '''SELECT COUNT('User Id')
FROM reviews
WHERE Nature > 100 and Shopping > 100;'''
result2 = cursor.execute(query).fetchone()
print ('amount of reviewers over 100 in nature and shopping:',result2[0])

query = '''
SELECT AVG(Shopping),
	   AVG(Sports),
	   AVG(Religious),
	   AVG(Nature),
	   AVG(Picnic),
	   AVG(Theatre)
FROM reviews;
'''
result2 = cursor.execute(query).fetchall()
print ('avg review per category:',result2)