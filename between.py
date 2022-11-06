import pymysql as mq
mysql = mq.connect(host="localhost",user="root",database="schools")
mycursor = mysql.cursor()

#for label
print("{:<15} {:<20}".format("State Id","State Name"))

#queury all
try:
    #sql="Select * from students"
    sql = "Select * from states where state_id between 2 and 5"
    mycursor.execute(sql)
    sdata = mycursor.fetchall()

    for s in sdata:
        #print(s)
        print("{:<15} {:<20}".format(s[0],s[1]))
except:
    print("Error")
