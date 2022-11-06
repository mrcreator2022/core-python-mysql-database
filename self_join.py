import pymysql as mq
mysql = mq.connect(host="localhost",user="root",database="schools")
mycursor = mysql.cursor()

#for label
#print("{:<15} {:<20} {:<20}".format("Category Id","Category Name"))

#queury all
try:
    #sql="Select * from students"
    sql = "Select * from categories as c1,categories as c2 where c1.cat_id=c2.parent_id"
    mycursor.execute(sql)
    sdata = mycursor.fetchall()

    for s in sdata:
        print(s)
       # print("{:<15} {:<20} {:<20}".format(s[0],s[1],str(s[2])))
except:
    print("Error")
