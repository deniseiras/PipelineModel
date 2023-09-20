from src.PipelineModel import Pipeline, PipelineModel
from pandas import DataFrame, read_parquet
from sklearn.preprocessing import PolynomialFeatures, QuantileTransformer, StandardScaler
from sklearn.pipeline import Pipeline as ScikitPipeline


class PipelineScikitLearn(Pipeline):
    """_summary_
    This class is a implementation of a Pipeline using scikit-learn
    Should be used in small data file scenarios

    Args:
        pandas_df (pandas.DataFrame) : a pandas dataframe input file
    """
    def fit_transform(self, pandas_df: DataFrame) -> DataFrame:
        for step_name, step_params in self.pipeline_config["steps"].items():
            if step_name == 'model':
                continue
            transformer_class_name, steps = step_params.popitem()
            # TODO will raise exception if class not found or continue without exception?
            transformer_class = globals()[transformer_class_name]
            transformer = transformer_class(**steps)
            self.transformers.append((step_name, transformer))

        pipe = ScikitPipeline(self.transformers)
        pandas_transfmd_df = pipe.fit_transform(pandas_df)
        return pandas_transfmd_df


class PipelineModelScikitLearn(PipelineModel):
    """_summary_
    This class is a implementation of a PipelineModel ScikitLearn.
    Should be used in small data file scenarios
    Loads datas using pandas

    Args:
        data_file_path (str) : the input path of input data
    """
    def load_data(self, data_file_path) -> DataFrame:
        pandas_input_df = read_parquet(data_file_path)
        return pandas_input_df
