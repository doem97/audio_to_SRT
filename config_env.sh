#!/bin/bash

apt-get -y update
apt-get install -y git
python3 -m pip install --user --upgrade pip
python3 -m pip install --user virtualenv
apt-get -y install python3-venv
python3 -m venv xunfei_venv
source xunfei_venv/bin/activate
pip install webapi
pip install requests

# python get-srt.py APPID SECRET-KEY