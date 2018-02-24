from utils.ml_templates import MLModel, MLData
from utils.general_utils import format_dataframe

class PowerModel(MLModel):
    
    def __init__(self):
        super().__init__()
        pass

    def extract_from_source(self, source, dst=None):
        "Extract data from a datasource."
        df = source.get_data()
        return MLData.set_destination(df, dst)

    def preclean(self, input_data, dst=None):
        

        df = input_data.get()
        df = format_dataframe(df)
        return MLData.set_destination(df, dst)
     