import oracledb
def cr_t():
    un='scott'
    ps='tiger'
    dn='localhost:1521/orclpdb'
    try:
        con=oracledb.connect(user=un,password=ps,dsn=dn)
        # cur=con.cursor()
        # qr="create table std_4(sn  varchar2(10),sno number(5))"
        # cur.execute(qr)
    except oracledb.DatabaseError as er:
        print(er)
    else:
        print('Table created sucessfully..')
    finally:
        # cur.close()
        con.close()
# Main prog
# t_name=input('Enter table name: ')
cr_t()