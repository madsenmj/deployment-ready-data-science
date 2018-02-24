import logging
import pandas as pd
import re


def set_logger(logfile):

    logging.basicConfig(filename=logfile, level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
    # Add the stream handler to print to console as well
    logging.getLogger().addHandler(logging.StreamHandler())

def format_dataframe(input_df):
    input_df['date'] = pd.to_datetime(input_df['Text.Date'],format="%b_%Y")
    input_df['zip'] = input_df['Zip.Code'].apply(lambda x: x.split('\r')[0])
    return input_df[['date','zip','Power.Use']]