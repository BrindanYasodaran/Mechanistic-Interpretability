#!/bin/bash
set -eo pipefail

conda config --remove channels defaults
conda config --add channels conda-forge
conda config --set channel_priority strict

env >> /etc/environment

echo "Conda channels configured"
