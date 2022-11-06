import pymysql as mq
mysql = mq.connect(host="localhost",user="root",database="schools")
mysqlcursor = mysql.cursor()

try:
    insertdata = "INSERT INTO students(st_name,st_class,st_email)values(%s,%s,%s)"
    t = ('veer','12th','veer.workholics@gmaill.com')
    mysqlcursor.execute(insertdata,t)
    mysql.commit();
    print("Data inserted successfully")
except:
    print("Error...")