import mysql.connector, random,string
from datetime import datetime
#thread
from threading import Thread
import threading,time


global e
e =False

# INFO ===============================================
def th1(co):
    cnx = mysql.connector.connect  (host='192.168.112.130',user='client1',password='clientpass', database='clustertest', auth_plugin='caching_sha2_password')
    cursor = cnx.cursor(buffered=True)

    while 1:

        print("*"*20);
        mySql_Create_Table_Query = "select count(*)  as 'records Fish' from fishcontrol.fish;"
        cursor.execute(mySql_Create_Table_Query)
        record = cursor.fetchone()
        print("\tQR:",mySql_Create_Table_Query,"\n\tRS: ", record)

        mySql_Create_Table_Query = "select count(*)  as 'records MyGuests' from clustertest.MyGuests;"
        cursor.execute(mySql_Create_Table_Query)
        record = cursor.fetchone()
        print("\tQR:",mySql_Create_Table_Query,"\n\tRS: ", record)
        print("*"*20);
        if e:exit()
        time.sleep(3)


# WRITE 1 ===============================================

def th2():
    print("~"*20);
    cnx = mysql.connector.connect  (host='192.168.112.130',user='client1',password='clientpass', database='clustertest', auth_plugin='caching_sha2_password')
    cursor = cnx.cursor(buffered=True)

    for i in range(1,50000):
        mySql_Create_Table_Query = "INSERT INTO clustertest.MyGuests ( firstname, lastname, email) VALUES ('nguyen','vo phuoc', 'email@') ;"
        cursor.execute(mySql_Create_Table_Query)
        if (i % 500) == 0 :
            cnx.commit()

        if (i/50000*100 % 0.5) ==0 : print(i/50000*100 )

    global e
    e=True
    exit()

try:

	t1 = threading.Thread(target=th1 ,args=("",)).start()
	t2 = threading.Thread(target=th2 ,args=()).start()
	t3 = threading.Thread(target=th2 ,args=()).start()
	t5 = threading.Thread(target=th2 ,args=()).start()
	t6 = threading.Thread(target=th2 ,args=()).start()
	t7 = threading.Thread(target=th2 ,args=()).start()
	t4 = threading.Thread(target=th2 ,args=()).start()



    #t3.start()
	#print ("done in ", time.time()- t)
except:
	print("error")
