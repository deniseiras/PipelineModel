from setuptools import setup, find_packages

prj_name='ML_test'
setup(
    name=prj_name,
    version='0.1.0',
    description='Description of your project',
    long_description='Detailed project description',
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
        'pyarrow'
        'dask-ml'
    ],
)