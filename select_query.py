import pymysql as mq
mysql = mq.connect(host="localhost",user="root",database="schools")
mycursor = mysql.cursor()

#for label
print("{:<15} {:<20}".format("Student Id","Student Name"))

#queury all
try:
    #sql="Select * from students"
    sql = "Select st_id,st_name from students"
    mycursor.execute(sql)
    sdata = mycursor.fetchall()

    for s in sdata:
        print("{:<15} {:<20}".format(s[0],s[1]))
except:
    print("Error")

#single row data
print("{:<15} {:<20}".format("Student Id","Student Name"))
try:
    sql = "Select * from students where st_id=1"
    mycursor.execute(sql)
    sdata = mycursor.fetchone()
    print("{:<15} {:<20}".format(sdata[0],sdata[1]))
except:
    print("Error")