from src.PipelineModel import PipelineModel
from src.ErrorLogger import log_failure

from pandas import DataFrame, read_parquet
from sklearn.preprocessing import PolynomialFeatures, QuantileTransformer, StandardScaler
from sklearn.pipeline import Pipeline as scikit_pipe

class PipelineModelScikitLearn(PipelineModel):
    class PipelineScikitLearn(PipelineModel.Pipeline):
        # implement the scikit learn preprocessing as needed
        transformer_mapping = {
            "reduce_dim": PolynomialFeatures,
            "qtransf": QuantileTransformer,
            "poly_feature": PolynomialFeatures,
            "stdscaler": StandardScaler,
        }

        def __init__(self, pipeline_file_path) -> None:
            super().__init__(pipeline_file_path)
            self.transformers = []

        def fit_transform(self, pandas_df) -> DataFrame:
            for step_name, step_params in self.pipeline.pipeline_config["steps"].items():
                transformer_class = self.pipeline.transformer_mapping.get(step_name)
                if transformer_class:
                    transformer = transformer_class(**step_params)
                    # pandas_df = transformer.fit_transform(pandas_df)
                    self.pipeline.transformers.append((step_name, transformer))
            
            pipe = scikit_pipe(self.pipeline.transformers)
            pandas_transfmd_df = pipe.fit_transform(pandas_df)
            return pandas_transfmd_df

    def __init__(self, pipeline_file_path) -> None:
        super().__init__(pipeline_file_path)

    def load_data(self, data_file_path) -> DataFrame:
        pandas_input_df = read_parquet(data_file_path)
        return pandas_input_df
