import pymysql as mq
mysql = mq.connect(host="localhost",user="root",database="schools")
mycursor = mysql.cursor()

# try:
#     insertdata = "INSERT INTO students(st_name,st_class,st_email) values(%s,%s,%s)"
#     t = [('ram','12th','ram@gmaill.com'),('s','12th','s@gmaill.com')]
#     mycursor.executemany(insertdata,t)
#     mysql.commit();
#     print("Data inserted successfully")
# except:
#     print("Error...")

# try:
#     insertdata = "INSERT INTO countries(country_name) values(%s)"
#     t = [("India"),("Shri Lanka"),("Australia")]
#     mycursor.executemany(insertdata,t)
#     mysql.commit();
#     print("Data inserted successfully")
# except:
#     print("Error...")

try:
    insertdata = "INSERT INTO states(state_name,country_id) values(%s,%s)"
    t = [("Gujarat","4"),("Madhaya Pradesh","5"),("Uttar Pradesh","6")]
    mycursor.executemany(insertdata,t)
    mysql.commit();
    print("Data inserted successfully")
except:
    print("Error...")