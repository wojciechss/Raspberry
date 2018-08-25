#!/bin/bash

WORKSPACE_PATH=$1
LOCAL_PYGRADLE_REPO_PATH=${WORKSPACE_PATH}/pygradle_repo
IMPORTER_NAME=pivy-importer-0.8.7-all.jar

# Create local repository dir
mkdir ${LOCAL_PYGRADLE_REPO_PATH}

function download_pyvi_importer() {
    if [ ! -f $IMPORTER_NAME ]; then
        wget https://dl.bintray.com/linkedin/maven/com/linkedin/pygradle/pivy-importer/0.8.7/$IMPORTER_NAME
    fi
}

function import_dependencies_to_repo() {
    file='requirements.txt'
    while read -r requirement; do
        echo "Downloading ${requirement/==/:}"
        java -jar pivy-importer-0.8.7-all.jar --repo ${LOCAL_PYGRADLE_REPO_PATH} ${requirement/==/:} \
            --replace Babel:0.8=Babel:2.6,pytz:2004b.2=pytz:2018.5,sphinx_rtd_theme:0.1.0=sphinx_rtd_theme:0.4.1
    done < "$file"
}

download_pyvi_importer
import_dependencies_to_repo

