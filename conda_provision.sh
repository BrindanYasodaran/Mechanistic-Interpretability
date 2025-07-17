#!/bin/bash
set -eo pipefail

conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r

conda config --remove channels defaults
conda config --add channels conda-forge
conda config --set channel_priority strict

env >> /etc/environment
echo "Conda channels and ToS acceptance configured"
