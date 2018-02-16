"""
Extract the raw data from the data source.
"""

import pandas as pd
import sqlalchemy as sql
import pyodbc
from urllib.parse import quote_plus
import logging

def data_extractor():

    params = quote_plus("DRIVER={SQL Server};SERVER=ALLNB220;DATABASE=LAUtility;trusted_connection=yes")
    engine = sql.create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)

    myQuery = "select * from HistoricalData"
    df = pd.read_sql_query(myQuery, engine)
    
    return df

if __name__ == "__main__":
    df = data_extractor()
    df.to_csv('input_data.csv',index=False, quoting=1, encoding='utf-8')