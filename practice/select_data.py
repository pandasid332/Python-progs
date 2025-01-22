import oracledb
u='scott'
p='tiger'
d='localhost:1521/orclpdb'
try:
    con=oracledb.connect(user=u,password=p,dsn=d)
    # print('Connection sucessful')
    cur=con.cursor()
    q="""select * from emp e
            where e.sal > (select avg(sal) from emp e1
            group by DEPTNO
            having e.deptno=e1.deptno)"""
    cur.execute(q)
    data=cur.fetchall()
    for rec in data:
        for rec1 in rec:
            print('\t{}'.format(rec1),end=' ')
    print()
except oracledb.DatabaseError as er:
    print(er)