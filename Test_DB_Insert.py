import sqlite3
conn = sqlite3.connect('MuDB2.db')
c = conn.cursor()

t = ('Cevap1',)
try:
    c.execute('INSERT INTO Cevap (cevapADI) VALUES (?)', t)
except sqlite3.IntegrityError as e:
    print('sqlite error: ', e.args[0]) # column name is not unique
c.commit()
print(c.insert_id())
conn.close()
