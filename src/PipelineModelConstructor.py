from src.PipelineModel import PipelineModel

"""_summary_
This class is an Invoker that invokes ModelExecutod received
"""
class PipelineModelConstructor:

    def __init__(self, pipe_model_class, pipeline_file_path: str):
        self.pipe_model_class = pipe_model_class
        self.pipe_file_path = pipeline_file_path

    def construct(self) -> PipelineModel:
        return self.pipe_model_class(self.pipe_file_path)
