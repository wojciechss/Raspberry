#!/bin/bash

WORKSPACE_PATH=$1
LOCAL_PYGRADLE_REPO_PATH=${WORKSPACE_PATH}/pygradle_repo

# Create local repository dir
mkdir ${LOCAL_PYGRADLE_REPO_PATH}

# Download pyvi-importer
wget https://dl.bintray.com/linkedin/maven/com/linkedin/pygradle/pivy-importer/0.8.7/pivy-importer-0.8.7-all.jar

# Import Python dependencies to local pygradle repo
REQUIREMENTS_FILES=`find . -name requirements.txt`
for file in ${REQUIREMENTS_FILES}; do
    while read -r requirement; do
        echo "Downloading ${requirement/==/:}"
        java -jar pivy-importer-0.8.7-all.jar --repo ${LOCAL_PYGRADLE_REPO_PATH} ${requirement/==/:} --replace Babel:0.8=Babel:2.6,pytz:2004b.2=pytz:2018.5
    done < "$file"
done

