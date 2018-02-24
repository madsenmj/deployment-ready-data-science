"""
Deployment-Ready Machine Learning Template Classes

Classes:
    MLData
    MLSource
    MLStore
    MLRecord
    MLModel

"""
class MLData:
    """
    The abstract parent class to handle data formats and translations.
    The default is to store the data in memory.

    """
    def __init__(self):
        self._data = None

    def get(self):
        return self._data
    
    def set(self, data):
        self._data = data

    @staticmethod
    def set_destination(data, dst):
        if isinstance(dst,MLData):
            dst.set(data)
            return dst
        else:
            in_memory = MLData()
            in_memory.set(data)
            return in_memory

class MLSource:
    """
    The source for the initial data load. Base class uses in in-memory source.

    Methods:
        get_data()

    """

    def __init__(self):
        pass

    def get_data(self, dst=None):
        """
        Retrieves the data from the source system.
        """
        return "To Be Implemented"


class MLRecord:
    """
    The abstract parent class to handle recording information about the model.
    """
    def __init__(self):
        pass

class MLModel:
    """
    Abstract machine learning model class.

    Methods:
        extract_from_source()
    
    """

    def __init__(self):
        self._data_dictionary = dict()
        self._model = None
            
    def extract_from_source(self):
        """Extract data from a datasource."""
        return "source data"

    def preclean(self, input_data):
        return "precleaned data"

    def validate(self, input_json):
        return "validate data"

    def transform(self, input_data, validate=False):
        return "transformed (and validated) data"

    def split(self, input_data):
        return "training data", "testing data"

    def train_model(self, train_data):
        return "model"

    def predict(self, input_data):
        return "predictions"

    def evaluate(self, test_data):
        return "model evaluation is here"
    
    def score(self, input_data):
        return "scored data"

    