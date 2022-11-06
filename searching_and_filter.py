import pymysql as mq
mysql = mq.connect(host="localhost",user="root",database="schools")
mycursor = mysql.cursor()

#for label
print("{:<15} {:<20} {:<20}".format("Student Id","Student Name" ,"Student Class"))

#queury all
try:
    #sql="Select * from students"
    #sql = "Select st_id,st_name from students order by st_id ASC"
    name = input("Enter the student name: ")
    classname = input("Enter the student class name: ")
    #sql = "Select * from students where st_name='"+name+"'"
    #sql = "Select * from students where st_name like'%"+name+"%'and st_class ='"+classname+"'"
    sql = "Select * from students where st_name like'%"+name+"%' or st_class ='"+classname+"'"
    mycursor.execute(sql)
    sdata = mycursor.fetchall()

    for s in sdata:
        print("{:<15} {:<20} {:<20}".format(s[0],s[1],s[2]))
except:
    print("Error")