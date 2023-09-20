from src.PipelineModelDask import PipelineModelDask, PipelineDask
from src.PipelineModelInvoker import PipelineModelInvoker
from src.PipelineModelConstructor import PipelineModelConstructor
from ErrorLogger import log_failure

pipeline_json_path = "artifacts/pipeline.jsonc"
dataset_path = "data/dataset.parquet"


def score():
    """
    The main file job_test_challenge.py and score function was maitained due to production
    compatibility. This function should score the model on the test data and return the score.

    Dask was used to improve performance. Note that the Dask QuantileTransformer
    implementation differs from the scikit-learn implementation by using approximate quantiles.
    Even setting n_quantiles, the results are different. The random_state was fixed in pipeline.jsonc
    for reprodutibility
    https://ml.dask.org/modules/generated/dask_ml.preprocessing.QuantileTransformer.html

    TODO: find the best n_quantile to reach a balance between performance and accuracy
    """
    try:
        pipe_scikit_builder = PipelineModelConstructor(
            PipelineModelDask, PipelineDask, pipeline_json_path
        )
        pipeline_model = pipe_scikit_builder.construct()

        invoker = PipelineModelInvoker(pipeline_model, dataset_path)
        predicted_value = invoker.execute()

        return predicted_value

    except Exception as e:
        log_failure(e)


if __name__ == "__main__":
    print(score())
