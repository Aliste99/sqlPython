import pandas as pd

class Companysearcher:
    
    def __init__(self, db_connection):
        self.db_connection = db_connection
    
    def find(self, name):
        query = "SELECT FullNameRu, HeadName, Founders FROM Minjust2018 WHERE FullNameRu LIKE         '%" + name + "%'"
        df = pd.read_sql_query(query, self.db_connection)
        return self.df_to_dict(df)
    
    def df_to_dict(self, df):
        companies = {}
        companies_list = df.values.tolist()
        print(companies_list)
        for company in companies_list:
            companies[company[0]] = company[-2:]
        return companies




