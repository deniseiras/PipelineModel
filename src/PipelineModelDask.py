from src.PipelineModel import PipelineModel, Pipeline
from dask_ml.preprocessing import PolynomialFeatures, QuantileTransformer, StandardScaler
from dask import dataframe as dask_df
from dask import compute


class PipelineDask(Pipeline):
    """_summary_
    This class is a implementation of a Pipeline using Dask - Big data purposes
    It uses pipeline in dask to transform

    Args:
        input_ddf (dask.dataframe) : a dask data frame as input
    """
    def fit_transform(self, input_ddf: dask_df) -> dask_df:
        transfmd_ddf = input_ddf
        for step_name, step_params in self.pipeline_config["steps"].items():
            if step_name == 'model':
                continue
            transformer_class_name, steps = step_params.popitem()
            # TODO will raise exception if class not found or continue without exception?
            transformer_class = globals()[transformer_class_name]
            transformer = transformer_class(**steps)
            transfmd_ddf = transformer.fit_transform(transfmd_ddf)
            # needs to compute every step to not generate rechunking errors when running in parallel
            # ex: Failure: Chunking is only allowed on the first axis. Use 'array.rechunk({1: array.shape[1]})'
            # to rechunk to a single block along the second axis.
            transfmd_ddf = compute(transfmd_ddf)[0]
            self.transformers.append((step_name, transformer))

        return transfmd_ddf


class PipelineModelDask(PipelineModel):
    """_summary_
    This class is a implementation of a PipelineModel Dask. Should be used in Big Data scenarios
    - loads data using dask dataframe

    Args:
        data_file_path (str) : the input path of input data

    """
    def load_data(self, data_file_path: str) -> bool:
        dask_input_df = dask_df.read_parquet(data_file_path)
        return dask_input_df
