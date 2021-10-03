import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()
config = {
    'host':os.getenv("HOST"), 
    'user':os.getenv("USER"), 
    'password':os.getenv("PASSWORD"),
    'port':os.getenv("PORT"), 
    'database':os.getenv("DATABASE"), 
    'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

query = ("SELECT * FROM v_accounts")

cursor.execute(query)

for i in cursor:
    print (i)