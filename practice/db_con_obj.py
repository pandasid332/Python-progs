import oracledb
def db_obj():
    u='scott'
    p='tiger'
    d='localhost:1521/orclpdb'
    con=oracledb.connect(user=u,password=p,dsn=d)
    return con