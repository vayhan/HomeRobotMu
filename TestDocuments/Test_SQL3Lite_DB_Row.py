import sqlite3
conn = sqlite3.connect('MuDB.db')
c = conn.cursor()

t = ('merhaba',)
#c.execute('Select * from Komut as K Join Cevap as C where K.cevapID = C.cevapID and komutADI=?', t)
c.execute('Select * from Komut where komutADI=? ORDER BY RANDOM() LIMIT 1', t)
for row in c:
    t = (row[2],)        
c.execute('Select * from Cevap where cevapID=?', t)
for row in c:
    print ( row[1] )
conn.close()
