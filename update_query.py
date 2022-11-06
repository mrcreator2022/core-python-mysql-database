import pymysql as mq
mysql = mq.connect(host="localhost",user="root",database="schools")
cursorobj = mysql.cursor()
name = input("Inter the name: ")
class_name = input("Inter the class name: ")
st_email = input("Inter the email: ")
st_id = input("Inter the student id: ")


sql = "UPDATE students set st_name=%s,st_class=%s,st_email=%s where st_id=%s"
data = (name,class_name,st_email,st_id)
try:
    cursorobj.execute(sql,data)
    mysql.commit()
    print("Data updated successfully")
except:
    print("Error...")
