PRJ_NAME="PipelineModel"
VERSION="1.0"
ENV_NAME="${PRJ_NAME}_env"

python3.8 -m venv ${ENV_NAME}
source ${ENV_NAME}/bin/activate
python setup.py sdist
pip install ./dist/${PRJ_NAME}-${VERSION}.tar.gz

echo -e "Now execute to load environment:\nsource ${ENV_NAME}/bin/activate"