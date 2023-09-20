import pickle
import json

from abc import abstractmethod, ABC


class Pipeline(ABC):
    """_summary_
    This class purpose is loading the pipeline and forcing the override of
    fit_transform method, which must be customized by the subclasses.

    Args:
        pipeline_file_path (str) : the pipeline.jsonc file path, which defines
                                    the pipeline and model at PipelineModel
   # TODO : Separate the preprocessing and model at pipeline.jsonc , to reuse configurations
   """

    def __init__(self, pipeline_file_path) -> None:
        self.pipeline_file_path = pipeline_file_path
        self.pipeline_config = None
        self.load_pipeline()
        self.transformers = []

    def load_pipeline(self):
        with open(self.pipeline_file_path, "r") as f:
            str_json = "\n".join(f.readlines()[3:])
        self.pipeline_config = json.loads(str_json)

    @abstractmethod
    def fit_transform(self, data):
        "Must be overriden"
        pass


class PipelineModel(ABC):
    """_summary_
    This class is composed by the Pipeline class and model, which is generic for all subclasses.
    Abstracts the data load, which must be overriden.

    Args:
        pipeline (Pipeline) : the preprocessor Pipeline subclass instance
    """

    def __init__(self, pipeline: Pipeline) -> None:
        self.pipeline = pipeline
        self.model = None
        self.load_model()

    def load_model(self):
        # Load the trained model (scikit-learn or other implementation)
        model_path = self.pipeline.pipeline_config["steps"]["model"]
        with open(model_path, "rb") as model_file:
            # TODO use JSON object instead of pickle, which is python version dependent.
            self.model = pickle.load(model_file)

    @abstractmethod
    def load_data(self, data_file_path):
        "Must be overriden"
        pass
