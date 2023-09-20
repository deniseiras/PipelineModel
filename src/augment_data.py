from dask import dataframe as dask_df
import pandas as pd

# configuration to generate data augmented
# duplication_factor = 120000  # big data
duplication_factor = 12000  # medium data
partitions = 10

data_file_path = "data/dataset.parquet"
dask_input_df = pd.read_parquet(data_file_path)


def augment_partition(partition, duplication_factor):
    # Duplicate each row in the partition by the specified factor
    augmented_data = pd.concat([partition] * duplication_factor, ignore_index=True)
    return augmented_data

ddf_augmented = augment_partition(dask_input_df, duplication_factor)
print(len(ddf_augmented))

ddf = dask_df.from_pandas(pd.DataFrame(ddf_augmented), npartitions=partitions)  # Use the appropriate number of partitions
dask_df.to_parquet(ddf, f'data/mediumdataset_{partitions}part.parquet')
# Get memory usage of the Dask DataFrame in bytes
memory_usage_bytes = ddf.memory_usage(deep=True).sum().compute()
print(f"Memory usage of the Dask DataFrame: {memory_usage_bytes} bytes")
