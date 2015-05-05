
import sqlite3

conn = sqlite3.connect('atm.db')
conn.execute('''CREATE TABLE atminit
       (START_MONEY  REAL,COMB_OF20 REAL,COMB_OF50 REAL)''')


  # an assumption that an ATM everyday starts with 6000$.
  # initialize the 20$ dollar notes , with the half starting money.
  # initialize the 50$ dollar notes with the rest of the starting money.

try:
    conn.execute("INSERT INTO atminit VALUES (6000,150,60)")      
    conn.commit()
except sqlite3.Error as e1:
    raise e1
conn.close()
