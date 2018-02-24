from power_model import PowerModel as Model
from utils.powermodel_utils import SQLSource

if __name__ == "__main__":
    
    mo = Model()
    sql_connection = {
        'connection_string': "DRIVER={SQL Server};SERVER=ALLNB220;DATABASE=LAUtility;trusted_connection=yes",
        'query': "select * from HistoricalData"
    }
    sqlsource = SQLSource(sql_connection)
    source_data = mo.extract_from_source(sqlsource)
    precleaned_data = mo.preclean(source_data)
    transformed_data = mo.transform(precleaned_data)
    train_data, test_data = mo.split(transformed_data)
    mo.train_model(train_data)
    predictions = mo.predict(test_data)
    mo.evaluate(predictions)


    