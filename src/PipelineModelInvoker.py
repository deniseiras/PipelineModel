from src.PipelineModel import PipelineModel
from src.ErrorLogger import log_failure


class PipelineModelInvoker:
    """_summary_
    This class uses PipelineModel instances for preprocessing and model prediction 
    
    Args:
        pipe_model (PipelineModel) : the PipelineModel instance
        input_dataset_path: the input dataset path 
    """

    def __init__(self, pipe_model: PipelineModel, input_dataset_path: str) -> None:
        self.pipe_model = pipe_model
        self.dataset_path = input_dataset_path

    def pipe_model(self):
        return self.pipe_model

    def execute(self):
        if not self.pipe_model or not self.dataset_path:
            log_failure(Exception("Undefined model or data set at ModelInvoker."))
        try:
            # data load and transform
            input_data = self.pipe_model.load_data(self.dataset_path)
            input_data = input_data[["vibration_x", "vibration_y", "vibration_z"]]
            input_data.fillna(0)
            transfmd_data = self.pipe_model.pipeline.fit_transform(input_data)

            # model predicting
            if not len(transfmd_data):
                raise RuntimeError("No data to score")
            if not hasattr(self.pipe_model.model, "predict"):
                raise Exception("Model does not have a score function")
            predicted_value = self.pipe_model.model.predict(transfmd_data)

            return predicted_value

        except Exception as e:
            log_failure(e)
