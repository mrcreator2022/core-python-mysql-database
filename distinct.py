import pymysql as mq
mysql = mq.connect(host="localhost",user="root",database="schools")
mycursor = mysql.cursor()

#for label
print("{:<15}".format("Employee Department"))

#queury all
try:
    sql = "Select distinct(dname) from employees"
    mycursor.execute(sql)
    sdata = mycursor.fetchall()

    for s in sdata:
        print("{:<15}".format(s[0]))
except:
    print("Error")
