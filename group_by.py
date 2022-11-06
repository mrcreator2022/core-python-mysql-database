import pymysql as mq
mysql = mq.connect(host="localhost",user="root",database="schools")
mycursor = mysql.cursor()

#for label
print("{:<15} {:<15}".format("Employee Count","Employee Department"))

#queury all
try:
    sql = "Select count(*),dname from employees group by dname"
    mycursor.execute(sql)
    sdata = mycursor.fetchall()

    for s in sdata:
        #print(s)
        print("{:<15} {:<15}".format(s[0],s[1]))
except:
    print("Error")
