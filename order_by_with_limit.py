import pymysql as mq
mysql = mq.connect(host="localhost",user="root",database="schools")
mycursor = mysql.cursor()

#for label
print("{:<15} {:<20}".format("Student Id","Student Name"))

#queury all
try:
    #sql="Select * from students"
    #sql = "Select st_id,st_name from students order by st_id ASC"
    sql = "Select st_id,st_name from students order by st_id DESC LIMIT 0,3"
    mycursor.execute(sql)
    sdata = mycursor.fetchall()

    for s in sdata:
        print("{:<15} {:<20}".format(s[0],s[1]))
except:
    print("Error")

