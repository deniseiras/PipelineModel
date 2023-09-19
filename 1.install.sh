PRJ_NAME="PipelineModel"
ENV_NAME="${PRJ_NAME}_env"
VERSION="1.0"

python3.8 -m venv ${ENV_NAME}
source ${ENV_NAME}/bin/activate
pip install ./dist/${PRJ_NAME}-${VERSION}.tar.gz