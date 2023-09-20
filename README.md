# PipelineModel

This project aims to preprocess and predict Big data Machine Learn models, which model configuration is stored as pickle file and the preprocessing as a JSON file.

~~~
author: Denis M. A. Eiras
Last revision: 20-sep-2023
~~~

--- 

## Instructions

Installation on linux:
- install.sh: Creates an environment, the distribution package at dist directoty and installs it.

Running:
- run_main.sh: Executes the implemented main code
- run_tests.sh: Executes the tests

## Implementation strategy

The main strategy was to use the Dask for preprocessing instead of the ScikitLearn. It was used the similar methods as PolynomialFeatures, QuantileTransformer and StandardScaler.
It was used Oriented Object Paradigm to abstract implementation for Dask and Scikit Learn.

Then, two tests were created. First using the ScikitLearn Pipeline and another using the Dask, using the dataset.parquet provided. 

After all, a data augmentation was created, using augment_data.py to test the performance of the main method job_test_challenge.py using ScikitLearn and Dask.
Was created 4 tests:
- medium sized file (100Mb) - 1 partition
- medium sized file (100Mb) - 10 partition
- big data sized file (1Gb) - 1 partition
- big data sized file (1Gb) - 10 partition 

## Results and Conclusion

The tests showed that the results of preprocessing made by Scikit Learn and Dask were diferent, mainly due to the difent implementations of QuantileTransform. When removing QuantileTransformer, the results were identical

The use of Dask using diferent parquet partitions over the medium sized files didn't shown any major performance in contrast to Scikit Learn.

## Future

There's a need for better understanding of the Dask package and what are the real benefits. 

A big data sized computer is needed to do more tests and check the performance using parquet files and Dask.

## Other information

It was used the formmater "black" to format the document.
