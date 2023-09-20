from src.PipelineModelConstructor import PipelineModelConstructor
from src.PipelineModelScikitLearn import PipelineModelScikitLearn, PipelineScikitLearn
from src.PipelineModelDask import PipelineModelDask, PipelineDask
from src.PipelineModelInvoker import PipelineModelInvoker

import unittest
import numpy as np
from datetime import datetime


class PipelineModelTest(unittest.TestCase):
    """_summary_
    This class tests the PipelineModel subclasses, preprocessing and model prediction
    """
    # fixed pipeline for testing
    pipeline_json_path = "artifacts/pipeline.jsonc"
    dataset_path = "data/dataset.parquet"

    def setUp(self) -> None:
        self.time_init = datetime.now()
        return super().setUp()

    def tearDown(self) -> None:
        self.time_end = datetime.now()
        print(
            f"{self._testMethodName} : execution time: {self.time_end-self.time_init}"
        )
        return super().tearDown()

    def compare_prediction_np(self, predicted_np: np.array, true_file_path: str):
        """_summary_
        Auxiliary function for comparing
        """
        true_np = np.load(true_file_path)
        self.assertTrue(np.array_equal(predicted_np, true_np))

    def test_PipelineModelScikitLearn(self):
        """_summary_
        Tests the prediction made by the ScikitLearn Pipeline
        """
        pipe_scikit_builder = PipelineModelConstructor(
            PipelineModelScikitLearn, PipelineScikitLearn, PipelineModelTest.pipeline_json_path
        )
        pipe_scikit = pipe_scikit_builder.construct()

        invoker = PipelineModelInvoker(pipe_scikit, PipelineModelTest.dataset_path)
        predict_np = invoker.execute()
        self.compare_prediction_np(predict_np,'test/true_data/scikit_true_values.npy')

    def test_PipelineModelDask(self):
        """_summary_
        Tests the prediction made by the Dask Pipeline.
        """
        pipe_dask_builder = PipelineModelConstructor(
            PipelineModelDask, PipelineDask, PipelineModelTest.pipeline_json_path
        )
        pipe_dask = pipe_dask_builder.construct()

        invoker = PipelineModelInvoker(pipe_dask, PipelineModelTest.dataset_path)
        predict_np = invoker.execute()
        self.compare_prediction_np(predict_np, 'test/true_data/dask_true_values.npy')


if __name__ == "__main__":
    unittest.main()
