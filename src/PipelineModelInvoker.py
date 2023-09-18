from PipelineModel import PipelineModel
from ErrorLogger import log_failure
from datetime import datetime
 
    
class PipelineModelInvoker():
    
    def __init__(self) -> None:
        self.pipe_model = None
        self.dataset_path = None

    def set_model(self, model: PipelineModel):
        self.pipe_model = model

    def set_dataset(self, dataset: str):
        self.dataset_path = dataset
        
    def execute(self):
        if not self.pipe_model or not self.dataset_path:
            log_failure(Exception('Undefined model or data set at ModelInvoker.'))
        try:
            
            time_init = datetime.now()
            trained_model = self.pipe_model.load_model()
            data = self.pipe_model.load_data(self.dataset_path)
            pipeline = self.pipe_model.load_pipeline()
            
            data = data[["vibration_x", "vibration_y", "vibration_z"]]
            # tr_data["vibration_x"].replace({np.nan: 0}, inplace=True)
            data_transfmd = self.pipe_model.it_transform(data)

            if not len(data_transfmd):
                raise RuntimeError("No data to score")
            if not hasattr(trained_model, "predict"):
                raise RuntimeError("Model does not have a score function")]

            predicted_value = trained_model.predict(data_transfmd)
            time_end = datetime.now()
            print(f'Execution time: {time_end-time_init}')
            return predicted_value
            
        except Exception as e:
            log_failure(e)
