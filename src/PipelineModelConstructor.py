from PipelineModel import PipelineModel

"""_summary_
This class is an Invoker that invokes ModelExecutod received
"""
class PipeModelConstructor():

    def __init__(self, pipe_model_class: PipelineModel.__class__, pipeline_file_path: str) -> PipelineModel:
        self.pipe_model = pipe_model_class(pipeline_file_path)