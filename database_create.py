import pymysql as mq
conn = mq.connect(host="localhost",user="root",database="schools")
mysql = conn.cursor()
try:
    db = "create database colleges"
    mysql.execute(db)
    print("Database created successfully")
except:
    print("Database error or already exist")