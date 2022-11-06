import pymysql as mq
mysql = mq.connect(host="localhost",user="root",database="schools")
mycursor = mysql.cursor()
st_id = input("Enter the student id: ")
sql = "DELETE From students where st_id=%s"
try:
    mycursor.execute(sql,st_id)
    mysql.commit();
    print("Student Deleted successfully")
except:
    print("Error...")