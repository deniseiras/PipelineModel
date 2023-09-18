import pickle
import json

from abc import abstractmethod, ABC

"""_summary_
This class implements methods for loading preprocessor pipeline and model.
Also abstracts the preprocessor pipeline method and data load, which must be overriden.
"""
class PipelineModel(ABC):
    """_summary_
    This internal class purpose is loading the pipeline and forcing the override of 
    fit_transform method, which must be customized by the subclasses.
    """
    class Pipeline(ABC):
        def __init__(self, pipeline_file_path) -> None:
            self.pipeline_file_path = pipeline_file_path
            self.pipeline_config = None

        @abstractmethod
        def fit_transform(self, df) -> bool:
            pass

        def load_pipeline(self):
            with open(self.pipeline_file_path, "r") as f:
                str_json = "\n".join(f.readlines()[3:])
            self.pipeline_config = json.load(str_json)

    def __init__(self, pipeline_file_path) -> None:
        self.pipeline = PipelineModel.Pipeline(pipeline_file_path)
        self.model = None

    @abstractmethod
    def load_data(self, data_file_path) -> bool:
        pass
    
    def load_pipeline(self):
        self.pipeline.load_pipeline()

    def load_model(self):
        # Load the trained model (scikit-learn or other implementation)
        model_path = self.pipeline.pipeline_config["steps"]["model"]
        with open(model_path, "rb") as model_file:
            # TODO use JSON object instead. The model needs to be saved as JSON first
            self.model = pickle.load(model_file)

    def fit_transform(self):
        self.pipeline.fit_transform()

    
    