import sqlite3
conn = sqlite3.connect('MuDB2.db')
c = conn.cursor()


t = ('Cevap1',)
try:
    c.execute('INSERT INTO Cevap (cevapADI) VALUES (?)', t)
except sqlite3.IntegrityError as e:
    print('sqlite error: ', e.args[0]) # column name is not unique
print(c.lastrowid)
k = ('Komut1','1',c.lastrowid,)
try:
    c.execute('INSERT INTO Komut (komutADI,komutTuruID,cevapID) VALUES (?,?,?)', k)
except sqlite3.IntegrityError as e:
    print('sqlite error: ', e.args[0]) # column name is not unique

conn.commit()
conn.close()
