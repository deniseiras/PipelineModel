from datetime import datetime
from sklearn.preprocessing import PolynomialFeatures, QuantileTransformer, StandardScaler
from ErrorLogger import log_failure
import pandas as pd

from sklearn.pipeline import Pipeline as scikitl_pipe

import pickle
import json
import numpy as np
import pyarrow


# Load any asset
def load(type, **kwargs):
    if type == "data":
        df = pd.read_parquet("./data/dataset.parquet")
        return df
    if type == "model":
        with open("./artifacts/pipeline.jsonc", "r") as f:
            str_json = "\n".join(f.readlines()[3:])
        import json

        with open(json.loads(str_json)["steps"]["model"], "rb") as f:
            return pickle.load(f)
    if type == "pipeline":
        return load_pipeline("./artifacts/pipeline.jsonc")

    else:
        return None


def load_pipeline(file_path: str) -> scikitl_pipe:
    # Load the pipeline configuration from JSON
    
    with open(file_path, "r") as f:
        str_json = "\n".join(f.readlines()[3:])
        # str_json = f.readlines()[3:]
        pipeline_config = json.loads(str_json)
    
    # Define the steps for the scikit-learn pipeline
    steps = []

    # Add PolynomialFeatures step
    if 'reduce_dim' in pipeline_config['steps']:
        degree = pipeline_config['steps']['reduce_dim']['PolynomialFeatures']['degree']
        steps.append(('reduce_dim', PolynomialFeatures(degree=degree)))

    # Add QuantileTransformer step
    if 'qtransf' in pipeline_config['steps']:
        output_distribution = pipeline_config['steps']['qtransf']['QuantileTransformer']['output_distribution']
        steps.append(('qtransf', QuantileTransformer(output_distribution=output_distribution)))

    # Add another PolynomialFeatures step
    if 'poly_feature' in pipeline_config['steps']:
        degree = pipeline_config['steps']['poly_feature']['PolynomialFeatures']['degree']
        steps.append(('poly_feature', PolynomialFeatures(degree=degree)))

    # Add StandardScaler step
    if 'stdscaler' in pipeline_config['steps']:
        with_mean = pipeline_config['steps']['stdscaler']['StandardScaler']['with_mean']
        with_std = pipeline_config['steps']['stdscaler']['StandardScaler']['with_std']
        steps.append(('stdscaler', StandardScaler(with_mean=with_mean, with_std=with_std)))

    pipeline = scikitl_pipe(steps)
    return pipeline


def score():
    """
    This function should score the model on the test data and return the score.
    """
    try:
        # pipeModel = PipelineModelScikitLearn()
        time_init = datetime.now()
        m = load("model")
        data = load("data")
        pipe = load("pipeline")

        data = data[["vibration_x", "vibration_y", "vibration_z"]]
        # tr_data["vibration_x"].replace({np.nan: 0}, inplace=True)
        tr_data = pipe.fit_transform(data)

        if not len(tr_data):
            raise RuntimeError("No data to score")
        if not hasattr(m, "predict"):
            raise Exception("Model does not have a score function")

        predicted_value = m.predict(tr_data)
        time_end = datetime.now()
        print(" The predicted values below are saved in th true_values.json, used as true value in tests")
        np.save('test/true_data/true_values.npy', predicted_value)
            
        print(f'Execution time: {time_end-time_init}')
        return predicted_value
        
    except Exception as e:
        print(e)
        log_failure(e)


if __name__ == "__main__":
    print(score())
