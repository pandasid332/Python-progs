import oracledb
import pandas as pd

class Data:
    def __init__(self, t_name):
        self.tname = t_name
        self.show_data(self.tname)

    def show_data(self, t):
        self.u = 'scott'
        self.p = 'tiger'
        self.d = 'localhost:1521/orclpdb'
        try:
            self.con = oracledb.connect(user=self.u, password=self.p, dsn=self.d)
            self.q = f'SELECT * FROM {t}'  # Correctly format the SQL query
            self.df = pd.read_sql(self.q, con=self.con)
        except oracledb.DatabaseError as er:
            print(er)
            self.df = None
        finally:
            self.con.close()
            if self.df is not None:
                print(self.df)
            else:
                print("Failed to retrieve data.")

# Create an instance of the class and call the db method with the table name as argument
t=input('Enter the table name: ')
d = Data(t)
