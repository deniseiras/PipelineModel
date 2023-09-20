from src.PipelineModel import PipelineModel


class PipelineModelConstructor:
    """_summary_
    This class is a Constructor of Pipeline and PipelineModel subclasses.

    Args:
        pipe_model_class (PipelineModel) : a subclass of PipelineModel to be constructed
        pipe_class (Pipeline) : a subclass of Pipeline to be constructed and used in the
                                PipelineModel
        pipe_file_path (str) : the path of the pipeline.jsonc which defines the pipeline
                                and model

    It uses the class definition to mount the objects
    """

    def __init__(self, pipe_model_class, pipe_class, pipeline_file_path: str):
        self.pipe_class = pipe_class
        self.pipe_model_class = pipe_model_class
        self.pipe_file_path = pipeline_file_path

    def construct(self) -> PipelineModel:
        pipeline = self.pipe_class(self.pipe_file_path)
        pipe_model = self.pipe_model_class(pipeline)
        return pipe_model
