import sqlite3

conn = sqlite3.connect("Artistc.db")
cursor = conn.cursor()  # cursor to interact with db
# Запитання 1. Інформація про скількох художників представлена у базі даних?
cursor.execute(''' SELECT * FROM artists''')
data = cursor.fetchall() # get tuple with db data (list  of tuples)
print(len(data))    # print data length

# Запитання 2. Скільки жінок (Female) у базі?

cursor.execute(''' SELECT * FROM artists WHERE Gender == "Female" ''')
data = cursor.fetchall()
print(len(data))


# Запитання 3. Скільки людей у базі даних народилися до 1900 року?
cursor.execute('''SELECT * FROM artists WHERE "Birth Year" < 1900''')
data = cursor.fetchall()
print(len(data))

# Запитання 4*. Як звати найстаршого художника?
cursor.execute('''SELECT name FROM artists ORDER BY "Birth Year" ''')
# < 1900 - щоб б було легше
data = cursor.fetchall()
print(data[0][0])

conn.commit()   # commit connection
conn.close()    # close connection 
