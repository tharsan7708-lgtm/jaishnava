import mysql.connector as t

host= 'jd-jaishnavadesigners.l.aivencloud.com'
user= 'avnadmin'
password= 'AVNS_MdgTDtpwxMHwJs4GSWk'
database= 'jaishnava'
port=27602

a = t.connect(host=host, password=password,user=user,database=database,port=port)
b=a.cursor()

b.execute("select * from users")
c=b.fetchall()
print(c)