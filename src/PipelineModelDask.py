import PipelineModel
from ErrorLogger import log_failure

from dask_ml.preprocessing import PolynomialFeatures, QuantileTransformer, StandardScaler
from dask import dataframe as dask_df

"""_summary_
This class implements specific methods for preprocessing pipeline and load data.
It aims to be fast in big data scenarios
"""
class PipelineModelDask(PipelineModel):
    class PipelineDask(PipelineModel.Pipeline):
        # implement the dask preprocessing as needed
        transformer_mapping = {
            "reduce_dim": PolynomialFeatures,
            "qtransf": QuantileTransformer,
            "poly_feature": PolynomialFeatures,
            "stdscaler": StandardScaler,
        }

        def __init__(self, pipeline_file_path) -> None:
            super().__init__(pipeline_file_path)
            self.transformers = []

        def fit_transform(self, pandas_df) -> bool:
            ret = True
            try:
                ddf = dask_df(pandas_df)
                # Apply each step in the pipeline configuration
                for step_name, step_params in self.pipeline.pipeline_config[
                    "steps"
                ].items():
                    transformer_class = self.pipeline.transformer_mapping.get(step_name)
                    if transformer_class:
                        transformer = transformer_class(**step_params)
                        ddf = transformer.fit_transform(ddf)
                        self.pipeline.transformers.append((step_name, transformer))
            except Exception as e:
                ret = False
                log_failure(e)
            return ret

    def __init__(self, pipeline_file_path) -> None:
        super().__init__(pipeline_file_path)

    def load_model() -> object:
        return

    @staticmethod
    def load_data(data_file_path) -> bool:
        dask_input_df = dask_df.read_parquet(data_file_path)
        return dask_input_df
