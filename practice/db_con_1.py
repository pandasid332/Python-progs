import oracledb
uname='scott'
pwd='tiger'
dn='localhost:1521/orclpdb'
   # 'localhost:1521/orclpdb'
try:
    con=oracledb.connect(user=uname,password=pwd,dsn=dn)
except oracledb.DatabaseError as er:
    print(er)
else:
    print('Database connection successfully...{}'.format(con.version))
finally:
    con.close()
    print('Connection closed')