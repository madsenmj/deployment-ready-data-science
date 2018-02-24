import pandas as pd
import sqlalchemy as sql
import pyodbc
import os
from urllib.parse import quote_plus

from utils.ml_templates import MLSource, MLData

class SQLSource(MLSource):
    
    def __init__(self, sql_configuration):
        if all(
            k in sql_configuration.keys() for k in [
                'connection_string','query'
                ]
            ):
            self._sql_configuration = sql_configuration
        else:
            raise ValueError('Could not find correct keys in configuration')
    
    def get_data(self):
        connection_string = self._sql_configuration['connection_string']
        query = self._sql_configuration['query']
        params = quote_plus(connection_string)
        engine = sql.create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)

        df = pd.read_sql_query(query, engine)
        
        return df

class CSVSource(MLSource):
    
    def __init__(self, csv_file_location):
        if os.path.isfile(csv_file_location):
            self._csv_file_location = csv_file_location
        else:
            raise OSError("{} not found.".format(csv_file_location))

    def get_data(self):
        df = pd.read_csv(self._csv_file_location, encoding='utf-8')
        return df


class CSVStoreData(MLData):
    def __init__(self,location):
        super().__init__()
        self._location = location
    def get(self):
        df = pd.read_csv(self._location, encoding='utf-8')
        return df
    def set(self, data):
        data.to_csv(self._location, encoding='utf-8', quoting=1, index=False)
    def get_location(self):
        return self._location
 