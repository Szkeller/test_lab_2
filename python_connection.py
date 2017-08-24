import MySQLdb
 
try:
    conn=MySQLdb.connect(host='localhost',user='root',passwd='root',port=3306)
    cur=conn.cursor()
     
    conn.select_db('keller_test')
 
    count=cur.execute('select * from user_info')
    print 'there has %s rows record' % count
 
    
     
 
    conn.commit()
    cur.close()
    conn.close()
 
except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])
