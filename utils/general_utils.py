import logging

def set_logger(logfile):

    logging.basicConfig(filename=logfile, level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
    # Add the stream handler to print to console as well
    logging.getLogger().addHandler(logging.StreamHandler())