from setuptools import setup, find_packages

prj_name='PipelineModel'
setup(
    name=prj_name,
    version='1.0',
    description='Pipeline preprocessing and model prediction',
    author='Denis Eiras',
    author_email='denis.eiras@gmail.com',
    url=f'https://github.com/deniseiras/{prj_name}',
    packages=find_packages(),
    python_requires='>=3.8.13, <3.9',  # pickle gen at 3.8.13 version
    install_requires=[
        'scikit-learn==1.0.2',
        'pandas',
        'datetime',
        'numpy',
        'dask-ml',
        'pyarrow'
    ],
)